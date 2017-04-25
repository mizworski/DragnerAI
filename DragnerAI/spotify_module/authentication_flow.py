import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util

username = "1198483266"
os.environ["SPOTIPY_CLIENT_ID"] = "eefab349cb6b4df38df5245b67bd0eb4"
os.environ["SPOTIPY_CLIENT_SECRET"] = "212affa7c96c41b1a726665dd0a5cda9"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost/"


scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
else:
    print("Can't get token for", username)