#!/bin/bash

# Palo Alto Networks SCM Environment Configuration
#
# IMPORTANT: Replace the placeholder values below with your actual credentials
# DO NOT commit this file with real credentials to version control

export SCM_HOST="api.sase.paloaltonetworks.com"
export SCM_AUTH_URL="https://auth.apps.paloaltonetworks.com"
export SCM_CLIENT_ID="your-client-id@1234567890.iam.panserviceaccount.com"

# REPLACE THE VALUE BELOW WITH YOUR ACTUAL SECRET
export SCM_CLIENT_SECRET="your-client-secret-uuid-here"

export SCM_TSG_ID="1234567890"
export SCM_LOG_LEVEL="DEBUG"

echo "SCM environment variables exported for TSG: $SCM_TSG_ID"
