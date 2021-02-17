import sys
import requests
import os
import json

URL = 'https://api.twitch.tv/helix'
TOKEN_URL = 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'

def authorize(client_id, client_secret):
    url = TOKEN_URL.format(client_id, client_secret)
    res = requests.post(url)
    return json.loads(res.text)

def query_channel(client_id, access_token):
    url = f'{URL}/search/channels?query=path of exile'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    res = requests.get(url, headers=headers)
    return json.loads(res.text)

if __name__ == "__main__":
    client_id = os.environ.get('CLIENT_ID') # Generate from Twitch Developer Console
    client_secret = os.environ.get('CLIENT_SECRET') # Generate from Twitch Developer Console
    ids = authorize(client_id, client_secret)
    print(ids.keys())
    channels = query_channel(client_id, ids['access_token'])
    print(channels['data'])
    for channel in channels['data']:
        print(f"{channel['title']} - {channel['display_name']}")