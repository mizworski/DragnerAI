from discord.ext import commands
from DragnerAI.music_player import Music, AdditionalCommands

bot_token = 'Mjk3NDA5NTM2NTAyMDA1NzYw.C8AYNQ.HBd5e_Q2pYLBzz6iSGOqw9YhyuU'

bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'), description='A playlist example for discord.py')
bot.add_cog(Music(bot))
bot.add_cog(AdditionalCommands(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))


bot.run(bot_token)
