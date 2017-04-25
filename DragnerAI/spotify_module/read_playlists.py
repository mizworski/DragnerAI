import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("eefab349cb6b4df38df5245b67bd0eb4",
                                                      "212affa7c96c41b1a726665dd0a5cda9")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('1198483266')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        offset = playlists['offset']
        uri = playlist['uri']
        name = playlist['name']
        print("%4d %s %s" % (i + 1 + offset, uri, name ))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

dawid_laska = sp.user('1198551640')
izworski = sp.user('1198483266')
wardega = sp.user('1192427096')
