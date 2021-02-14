# Integrate Twitch API
1. Register Twitch Application
- https://dev.twitch.tv/docs/authentication/

2. Get ClientID & Client Secret
- Sample Code -> Replace `client-id`
```
cd twitch
source .env/bin/activate
CLIENT_ID=<client-id> CLIENT_SECRET=<client-secret> python main.py
```

# Rate Limits
- Token bucket algorithm - token (aka point) counts for a request
- 800 points per minute per user and a bucket size of 800 points
- Limit is across all Twitch API queries. If this limit is exceeded, an error is returned: HTTP 429 (Too Many Requests).