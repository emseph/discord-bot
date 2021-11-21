import discord
import random
import time

# insert bot token here
TOKEN = ''

client = discord.Client()

# functions start
autoreply = ['Hi',
             'Hello',
             'How are you?']

test = ["1", "2", "3"]
# functions end


@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Game('Tite'))
    # bot activity,in this case he's watching a movie called movie
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Movie'))
    print('{0.user} is now online!'.format(client))  # bot status on discord


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send(f'This can be used anywhere!')
        return

    if message.author.id == 312524560224223233:  # server owner, REPLACE ID WITH YOUR OWN ID
        await message.channel.send(f'Hello master')
        return
    # if message sender is not server owner, REPLACE ID WITH YOUR OWN ID
    if message.author.id != 312524560224223233:
        if user_message == '<@!911156799040786432>':
            await message.channel.send(random.choice(test))
        return

    ''' If you want the bot to send autoreplies in a specific channel
    if message.channel.name == 'channel_name':  # replace the channel name you want the bot to be in


    '''

client.run(TOKEN)
