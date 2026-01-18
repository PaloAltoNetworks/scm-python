
#!/bin/bash

# Palo Alto Networks SCM Environment Configuration

export SCM_HOST="qa.api.sase.paloaltonetworks.com"
export SCM_AUTH_URL="https://auth.qa.appsvc.paloaltonetworks.com"
export SCM_CLIENT_ID="terraform-beta@1177241725.iam.panserviceaccount.com"

# REPLACE THE VALUE BELOW WITH YOUR ACTUAL SECRET
export SCM_CLIENT_SECRET="35e2b974-edec-4bb2-b2b5-49dde12bdbdc"

export SCM_TSG_ID="1177241725"
export SCM_LOG_LEVEL="DEBUG"

echo "SCM environment variables exported for TSG: $SCM_TSG_ID"