from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json


class SpotifyAdd:
    def __init__(self):
        with open('spotify_login.json') as data_file:
            spotify_login = json.load(data_file)
        client_id = spotify_login['client_id']
        client_secret = spotify_login['client_secret']
        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_playlists(self, user_id, limit):
        user_id = str(user_id)
        playlists_data = self.sp.user_playlists(user_id, limit=limit)
        playlists = playlists_data['items']

        res = []
        i = 0
        for playlist in playlists:
            res.append([i + 1, playlist['name'], playlist['uri'], playlist['id']])
            i += 1

        return res

    def get_songs_from_playlist(self, uri):
        username = uri.split(':')[2]
        playlist_id = uri.split(':')[4]

        results = self.sp.user_playlist(username, playlist_id)

        tracks = results['tracks']['items']

        songs = []

        for track_info in tracks:
            track = track_info['track']
            track_name = track['name']
            artists = track['artists']
            artists_name = []
            for artist in artists:
                artist_name = artist['name']
                artists_name.append(artist_name)

            songs.append([track_name, artists_name])

        return songs

    def get_playlist(self, user_id, index):
        user_id = str(user_id)
        index = int(index)
        user_playlists = self.get_playlists(user_id, 50)

        if len(user_playlists) > index:
            playlist = user_playlists[index - 1]
            playlist_uri = playlist[2]
            return [playlist[1], self.get_songs_from_playlist(playlist_uri)]

            # def get_playlist(self, user_id, playlist_id, limit):
            #     user_id = str(user_id)
            #     playlist_id = int(playlist_id)
            #     limit = int(limit)
            #     user_playlists = self.get_playlists(user_id)
            #
            #     if len(user_playlists) > playlist_id:
            #         playlist = user_playlists[playlist_id - 1]
            #         playlist_spotify_id = playlist[3]
            #         # return [playlist[1], self.get_songs_from_playlist(playlist_uri)]
            #         tracks = self.sp.user_playlist_tracks(user_id, playlist_spotify_id, limit, market="PL")
            #         return [playlist[1], tracks]

# playlists_items = playlists['items']
# ps = playlists_items[0]
# uri = ps['uri']
#
# print(results['name'])


# spotify = SpotifyAdd()
#
# michal_id = 1198483266

# playlists = spotify.get_playlists(michal_id)
# playlist = spotify.get_playlist(michal_id, 2)

# print(playlists)
# print(playlist)
