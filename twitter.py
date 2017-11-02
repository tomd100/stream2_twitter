import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'RDfHr3HQD3Cnw3fT7pPDRFxe4'
CONSUMER_SECRET = 'q3Eh8JprRm8Y6mDioKb94XD2YCAmxrgYgEoGpRyM4B3AUyV7fI'
OAUTH_TOKEN = '16885170-4iE5wz5TJ1VoXKZe3MSralTLmrYyi1hC2ozhCfjkq'
OAUTH_TOKEN_SECRET = 'USVNmUl0gkI6XuJxdFi2MuTNS6x6CSNalv3hIXVWmIhnR'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)

api = get_api()


DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))