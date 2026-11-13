"""
Cloud NGFW helpers for the SCM Python SDK.

Wraps the generated NgfirewallsApi calls with the behaviour Cloud NGFW needs:
create_cloud_ng_firewall resolves the tenant LinkId, defaults the tier, translates the
customer-facing mode value to the value the API accepts and tags the request source;
list_cloud_ng_firewalls always requests the detailed listing with a bounded page size;
delete_cloud_ng_firewall tags the request source. NgfirewallsApi inherits these methods from NgfirewallsApiHelpers.
"""


# Canonical Source values sent on ngfirewall create requests to identify the
# originating client. Always use these constants rather than bare string literals.
CNGFW_SOURCE_SDK = "SCM-SDK"
CNGFW_SOURCE_TERRAFORM_PROVIDER = "Terraform-Provider-SCM"
_CNGFW_PARAM_DESCRIBE = "describe"
_CNGFW_PARAM_MAXRESULTS = "maxresults"
_CNGFW_PARAM_MAXRESULTS_VALUE = "100"
_CNGFW_PARAM_NEXT_TOKEN = "nexttoken"
_CNGFW_MAX_ERROR_BODY = 1024


def _cngfw_error_body(raw: str) -> str:
    """Backend response body as trimmed text for an error message, truncated so a large
    (e.g. HTML) error page cannot flood the output."""
    text = raw.strip()
    if len(text) > _CNGFW_MAX_ERROR_BODY:
        return text[:_CNGFW_MAX_ERROR_BODY] + "... (truncated)"
    return text


class _CngfwHttpErrorResponse:
    """Adapts a urllib HTTPError to the response shape ApiException.from_response expects."""

    def __init__(self, err, raw: str):
        self.status = err.code
        self.reason = err.reason
        self.data = raw.encode("utf-8")
        self._headers = list(err.headers.items()) if err.headers else []

    def getheaders(self):
        return self._headers


def _cngfw_open_json(req):
    """Send req and return the decoded JSON body.

    A non-2xx response is raised as the SDK's ApiException (BadRequestException,
    UnauthorizedException, ... as for the generated methods) carrying the HTTP status and
    the backend's own response body, so an error payload is never mistaken for a result.
    """
    import json as _json
    import urllib.error
    import urllib.request
    from scm.cloud_ngfw.exceptions import ApiException

    try:
        with urllib.request.urlopen(req) as resp:
            return _json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        raw = err.read().decode("utf-8", errors="replace")
        # from_response always raises the exception type matching the status code.
        ApiException.from_response(
            http_resp=_CngfwHttpErrorResponse(err, raw),
            body=_cngfw_error_body(raw),
            data=None,
        )


def retrieve_tenant_scm_link_id(api_client) -> str:
    """Fetch LinkId from GET /cngfw-aws/v2/mgmt/tenant.

    Uses the same ApiClient (and therefore the same Bearer token) as all other
    Cloud NGFW calls. The tenant URL is derived from configuration.host — the
    same base URL the SDK uses for all other calls — so any user-configured host
    override is automatically respected. Returns the LinkId string, or empty
    string if not found.
    """
    import urllib.request

    cfg = api_client.configuration
    # configuration.host already carries the full server URL (respects user overrides).
    # Replace the known config path suffix with the mgmt path.
    # configuration.host is an ORIGIN - operation paths are appended per call, so it never
    # contains "/cngfw-aws/v2/config" and a str.replace of that suffix is always a no-op,
    # leaving mgmt_url pointing at "/" which 404s on every tenant. Append instead.
    server_url = cfg.host.rstrip("/")
    config_suffix = "/cngfw-aws/v2/config"
    if server_url.endswith(config_suffix):
        server_url = server_url[: -len(config_suffix)]
    mgmt_url = server_url + "/cngfw-aws/v2/mgmt/tenant"

    req = urllib.request.Request(mgmt_url, method="GET")
    # Copy Bearer token from the api_client's default headers.
    for key, value in api_client.default_headers.items():
        req.add_header(key, value)
    # Also add the Authorization header if access_token is set on configuration.
    if cfg.access_token:
        req.add_header("Authorization", "Bearer " + cfg.access_token)

    body = _cngfw_open_json(req)

    link_id = (body.get("Response") or {}).get("ScmInfo", {}).get("LinkId", "")
    import logging as _logging
    _logging.getLogger(__name__).debug("Retrieved LinkId from tenant SCM API: %s", link_id)
    return link_id


class NgfirewallsApiHelpers:
    """Convenience methods mixed into NgfirewallsApi."""

    def create_cloud_ng_firewall(
        self,
        region: str,
        ngfirewall_create_request,
        **kwargs,
    ):
        """Creates a Cloud NGFW firewall. Use this instead of create_ngfirewalls."""
        # The outgoing request is built with model_copy(update=...) rather than by assigning to
        # the caller's model: the generated models validate on assignment, and the translated
        # mode value (see below) is one the model's enum rejects. A copy also leaves the
        # caller's request untouched.
        updates = {}
        if not ngfirewall_create_request.link_id:
            updates["link_id"] = retrieve_tenant_scm_link_id(self.api_client)
        # Respect a caller-supplied tier; otherwise create at "standard" so the server
        # never assigns its own default tier (base).
        if not getattr(ngfirewall_create_request, "tier", None):
            updates["tier"] = "standard"
        # Translate the customer-facing mode value to the value the API accepts.
        if getattr(ngfirewall_create_request, "mode", None) == "AIRSM":
            updates["mode"] = "AIRFM"
        # Track the origin: preserve the Terraform provider value if already set;
        # otherwise mark this as a direct SDK call.
        if getattr(ngfirewall_create_request, "source", None) != CNGFW_SOURCE_TERRAFORM_PROVIDER:
            updates["source"] = CNGFW_SOURCE_SDK
        return self.create_ngfirewalls(
            region=region,
            ngfirewall_create_request=ngfirewall_create_request.model_copy(update=updates),
            **kwargs,
        )

    def list_cloud_ng_firewalls(
        self,
        region: str = "",
        globalrulestackname: str = "",
        **kwargs,
    ):
        """Lists Cloud NGFW firewalls, following NextToken pagination transparently.
        Use this instead of list_ngfirewalls."""
        import urllib.request
        import urllib.parse
        import re
        from types import SimpleNamespace

        def _snake(key):
            s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", key)
            return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

        def _to_ns(obj):
            if isinstance(obj, dict):
                return SimpleNamespace(**{_snake(k): _to_ns(v) for k, v in obj.items()})
            if isinstance(obj, list):
                return [_to_ns(i) for i in obj]
            return obj

        cfg = self.api_client.configuration
        server_url = cfg.host.rstrip("/")
        config_suffix = "/cngfw-aws/v2/config"
        if server_url.endswith(config_suffix):
            server_url = server_url[: -len(config_suffix)]
        list_base_url = server_url + "/cngfw-aws/v2/config/ngfirewalls"

        all_firewalls = []
        next_token = None

        while True:
            params = {_CNGFW_PARAM_DESCRIBE: "true", _CNGFW_PARAM_MAXRESULTS: _CNGFW_PARAM_MAXRESULTS_VALUE}
            if region:
                params["region"] = region
            if globalrulestackname:
                params["globalrulestackname"] = globalrulestackname
            if next_token:
                params[_CNGFW_PARAM_NEXT_TOKEN] = next_token

            url = list_base_url + "?" + urllib.parse.urlencode(params)
            req = urllib.request.Request(url, method="GET")
            for key, value in self.api_client.default_headers.items():
                req.add_header(key, value)
            if cfg.access_token:
                req.add_header("Authorization", "Bearer " + cfg.access_token)

            body = _cngfw_open_json(req)

            response_body = body.get("Response") or {}
            all_firewalls.extend(response_body.get("FirewallsDescribe") or [])
            next_token = response_body.get("NextToken")
            if not next_token:
                break

        return _to_ns({"Response": {"FirewallsDescribe": all_firewalls}})

    def delete_cloud_ng_firewall(
        self,
        id: str,
        region: str,
        source: str = None,
        **kwargs,
    ):
        """Deletes a Cloud NGFW firewall. Use this instead of delete_ngfirewalls_by_id."""
        effective_source = CNGFW_SOURCE_SDK
        if source == CNGFW_SOURCE_TERRAFORM_PROVIDER:
            effective_source = CNGFW_SOURCE_TERRAFORM_PROVIDER
        return self.delete_ngfirewalls_by_id(
            id=id,
            region=region,
            source=effective_source,
            **kwargs,
        )
