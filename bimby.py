import discord
import random

TOKEN = 'OTAxMzA0Mzk5Nzc3OTE5MDc3.YXN7Ig.v5CxgcbtBsBD4YxCqZCvA3a4pew'

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} is now online!'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '<@!901304399777919077>':
        # await message.channel.send(f'Sorry ganto lang ako @{username}!')
        await message.channel.send(f'Sorry ganto lang ako! Huhubels')
        return

client.run(TOKEN)
