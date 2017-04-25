import json

from discord.ext import commands
from DragnerAI.music_player import Music, AdditionalCommands
from DragnerAI.spotify import Spotify

with open('discord_login.json') as data_file:
    data = json.load(data_file)

bot_token = data['bot_token']

bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'), description='A playlist example for discord.py')
bot.add_cog(Music(bot))
bot.add_cog(AdditionalCommands(bot))
bot.add_cog(Spotify(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))


bot.run(bot_token)
