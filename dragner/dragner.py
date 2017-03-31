import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('Co powiesz o chelenie?'):
        await client.send_message(message.channel, 'Hm...')
        await asyncio.sleep(4)
        await client.send_message(message.channel, 'To jest szmata kurwa.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Podłogi bym nią nie wytarł bo bym się kurwa brzydził.')
    elif message.content.startswith('Co powiesz o grzesiu?'):
        await client.send_message(message.channel, 'Na zawołanie macha ogonem.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'I naucz się kurwo od niego albo zginiesz.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Rozumiesz to?')


client.run('Mjk3NDA5NTM2NTAyMDA1NzYw.C8AYNQ.HBd5e_Q2pYLBzz6iSGOqw9YhyuU')
