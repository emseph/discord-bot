import discord
from discord.channel import VoiceChannel
from discord.ext import commands
# import os
# import requests
# import json

TOKEN = ''
client = discord.Client()

client = commands.Bot(command_prefix="%")


@client.event
async def on_ready():
    # await client.change_presence(activity=discord.ActivityType.listening, name='Music')
    await client.change_presence(activity=discord.Game('Music'))
    print('{0.user} is now online!\nSanaol'.format(client))

# @client.command()
# async def play(ctx, url: str):
#     voiceChannel = discord.utils.get(ctx.guild.voice_channel name='General')
#     voice = discord.utils.get(client.voice_clients, guild = ctx.)


client.run(TOKEN)
