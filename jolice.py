import discord
import random

TOKEN = 'OTAxMTM3MTA5MjcwNzk0MzAw.YXLfVQ.eZ1Qxdv52LrTRonP7HjCS-74qT4'

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} is now online!'.format(client))


@client.event
async def on_message(message):
    # username = str(message.author).split('#')[0] <= no id tag
    username = str(message.author)  # with id tag
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # if message.channel.name == 'testing-area':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hellows {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hellows {username}!')
        return
    elif user_message.lower() == '<@!901137109270794300>':
        await message.channel.send(f'Holabels {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'Bye {username}!')
        return
    elif user_message.lower() == '!random':
        response = f'This is your random number: {random.randrange(1000000)}'
        await message.channel.send(response)
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return


client.run(TOKEN)
