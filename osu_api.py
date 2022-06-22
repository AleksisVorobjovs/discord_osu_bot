from email.mime import application
from multiprocessing.spawn import import_main_path
from urllib import response
from aiohttp import request
import json
import requests
from decouple import config


osu_client_id = config('OSU_CLIENT_ID')
osu_client_secret = config('OSU_CLIENT_SECRET')

osu_api_url = "https://osu.ppy.sh/api/v2"
osu_token_url = "https://osu.ppy.sh/oauth/token"
user_id = "14392873"

#gets token
def get_token():
    data = {
        'client_id': osu_client_id,
        'client_secret': osu_client_secret,
        'grant_type': 'client_credentials',
        'scope': 'public'
        }
    response = requests.post(osu_token_url, data=data)
    return response.json().get('access_token')

#returns user's best score
def best_score(id):
    token = get_token()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    params = {
        'mode': 'osu',
        'limit': 1
    }
    response = requests.get(f'{osu_api_url}/users/{id}/scores/best', params=params, headers=headers)
    #beatmapset_data = response.json()[0].get('beatmapset')
    with open('sample.json', 'w') as f:
        json.dump(response.json(), f)

best_score(user_id)

