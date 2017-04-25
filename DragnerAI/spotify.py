from discord.ext import commands
from DragnerAI.spotify_module.SpotifyAdd import SpotifyAdd
from DragnerAI.database import get_user_id


class Spotify:
    def __init__(self, bot):
        self.bot = bot
        self.sp = SpotifyAdd()

    @commands.command(pass_context=True, no_pm=True)
    async def playlists(self, ctx, *, msg: str):
        params = msg.split()
        limit = 25

        user_id = get_user_id(params[0])
        if len(params) == 2:
            limit = int(params[1])

        if limit > 50:
            await self.bot.say("My limit is 50 playlists for now.")
            limit = 50

        playlists = self.sp.get_playlists(user_id, limit)
        message = ''

        for playlist in playlists:
            message += str(playlist[0]) + ': ' + playlist[1] + '\n'

        await self.bot.say(message)

    @commands.command(pass_context=True, no_pm=True)
    async def playlist(self, ctx, *, msg: str):
        params = msg.split()

        if len(params) != 2:
            await self.bot.say('Wrong number of parameters')
            return

        user_id = get_user_id(params[0])
        index = params[1]
        playlist_info = self.sp.get_playlist(user_id, index)
        name = playlist_info[0]
        songs = playlist_info[1]

        await self.bot.say('Listing songs in playlist: ' + name)

        i = 0
        message = ''
        for song in songs:
            artists = ''
            for artist in song[1]:
                artists += ' ' + artist

            message += str(i + 1) + ': ' + song[0] + ' -' + artists + '\n'
            i += 1

            if i % 50 == 0:
                await self.bot.say(message)
                message = ''

        if not message == '':
            await self.bot.say(message)
