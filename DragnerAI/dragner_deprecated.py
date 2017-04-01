import discord
import asyncio
import sys

print(sys.version)
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
    elif message.content.lower().startswith('co powiesz o chelenie'):
        await client.send_message(message.channel, 'Hm...')
        await asyncio.sleep(4)
        await client.send_message(message.channel, 'To jest szmata kurwa.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Podłogi bym nią nie wytarł bo bym się kurwa brzydził.')
    elif message.content.lower().startswith('co powiesz o grzesiu'):
        await client.send_message(message.channel, 'Na zawołanie macha ogonem.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'I naucz się kurwo od niego albo zginiesz.')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Rozumiesz to?')
    elif message.content.lower().startswith('kto jest alkoholikiem'):
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'No jak to kto?')
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'XDD')
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'Janusz Wardęga')
    elif message.content.lower().startswith('bułke'):
        await client.send_message(message.channel, 'Bułe w ryj')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'śmieciu')
    elif message.content.lower().startswith('dupa'):
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'Dawid Laska zmienia poglądy')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'częściej niż studia')
        await asyncio.sleep(2)
        await client.send_message(message.channel, 'XDDDD')
    elif message.content.startswith('$cool'):
        await client.send_message(message.channel, 'Who is cool? Type $name namehere')

        def check(msg):
            return msg.content.startswith('$name')

        d = await client.wait_for_message(author=message.author, check=check)
        print(d)
        print(d.content)
        name = d.content[len('$name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))
    elif message.content.startswith('!embed_msg'):
        em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
        em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
    elif message.content.startswith('!usun_wiadomosci'):
        deleted = await client.purge_from(message.channel, limit=100, check=is_me)
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    elif message.content.startswith('!member_info'):
        print(message.author)
        print(message.author.nick)
        channel = client.get_channel(1)
        await client.send_message(channel, message.author)
    elif message.content.startswith('!channel_info'):
        await client.send_message(message.channel, message.channel.name)
        await client.send_message(message.channel, message.channel.server)
        await client.send_message(message.channel, message.channel.id)
        await client.send_message(message.channel, message.channel.topic)

    elif message.content.startswith('z ojcem nie gadasz.'):
        await client.send_message(message.channel, 'zamknij morde Ymeczka menelu pierdolony')
    elif message.content.startswith('!channels'):
        channels = client.get_all_channels()

        for channel in channels:
            await client.send_message(message.channel, channel.name)
            await client.send_message(message.channel, channel.id)


@client.event
async def on_member_update(before, after):
    channels = client.get_all_channels()
    print(before.status)
    print(after.status)
    if before.status == discord.Status.idle and after.status != discord.Status.idle:
        for channel in channels:
            if str(channel) == 'programistyczny':
                await asyncio.sleep(2)
                await client.send_message(channel, 'dobra ' + after.nick)
                await asyncio.sleep(2)
                await client.send_message(channel, 'wyppierdalaj')
                await asyncio.sleep(2)
                await client.send_message(channel, 'jesteś totalnym zjebem')


def is_me(m):
    return m.author == client.user


client.run('Mjk3NDA5NTM2NTAyMDA1NzYw.C8AYNQ.HBd5e_Q2pYLBzz6iSGOqw9YhyuU')
