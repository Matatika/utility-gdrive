import datetime
import json
import os

from httplib2 import Http


def proxy_refresh_handler(request, scopes):
        """google.oauth2.credentials.Credentials callback to refresh an expired token
        
        Returns:
            Makes an Auth2 'refresh_token' request to the 'oauth_credentials.refresh_url'.
            
            proxy_refresh_handler is only called when access_token is no longer valid.   
        """
        http = Http()
        del request, scopes
        headers = {}        
        if os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL_AUTH"):
            headers["authorization"] = os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL_AUTH")
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        request_body = {
            'grant_type': 'refresh_token',
            'refresh_token': os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_TOKEN")
        }
        print("Requesting token [%s], [%s], [%s]", os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL"), headers, request_body)
        (resp, content) = http.request(
            os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL"), 
            method="POST",
            body=json.dumps(request_body),
            headers=headers
        )
        print("Refresh token response [%s], [%s], [%s]", resp.status, resp.reason, content) 
        result = json.loads(content)
        token = result['access_token']
        seconds_delta = datetime.timedelta(0, result['expires_in'])
        expiry = datetime.datetime.now() + seconds_delta

        return token, expiry