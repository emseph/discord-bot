import discord
import random

TOKEN = 'OTAxMzA0Mzk5Nzc3OTE5MDc3.YXN7Ig.TeBIDLonzoRB_2lsUFYdEiKEIRg'

client = discord.Client()

# functions start

# functions end


@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Game('Tite'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Bold'))
    print('{0.user} is now online!\nSanaol'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send(f'This can be used anywhere!')
        return
    # if user_message.content == 'dm':
    #     print(f'{username}: {user_message}')
    #     return
    # 312533659880259584 jorg id
    if message.channel.name == '✉｜shitposting':

        # SHITPOSTING CHANNEL FUNCTIONS START
        autoreply = random.choice(
            ['Sorry ganto lang ako!\nHuhubels :sob: :weary: :point_left: :ok_hand: :100: :cold_face:',
             '\'Pag di ako nagpopost sa nsfw, nanghihina ako :nail_care: :person_in_manual_wheelchair:',
             'Patapos na 2022 wala parin kumu :tired_face: :ok_hand: :microphone:',
             'VODs ko boring kasi nakamute discord ko hehe',
             'Mahilig ako sa milf kasi kulang ako sa pagmamahal ng nanay ko, ayaw ako payagan sa outing aw8',
             'Binan ko si Alice kasi inggiterong palaka ako',
             '\'Kumakain ako tae, mmm yum',
             'hey, just wanna ask something if kasama mo pa din sa room kanina si ash nung pauwi sya?',
             'Kung bibigyan ako no God ng isang wish ang wish ko ay makapiling siya',
             'Stop bitching sister!!!',
             'Why am I afraid to lose you when you are not even mine?',
             'I REALLY MISS HER TONIGHT!'])

        slur = []
        # SHITPOSTING CHANNEL FUNCTIONS END

        if message.author.id == 312524560224223233:
            if user_message == '<@!312533659880259584>':
                await message.channel.send('Bakla yang tanginang yan')
            if user_message == 'Hello':
                await message.channel.send('Hi pogi')
            if user_message == '<@!901304399777919077>':
                print(f'{username}: {user_message} ({channel})')
                await message.channel.send(autoreply)
            return

        if message.author.id == 690900203414224906:
            await message.channel.send('hey, just wanna ask something if kasama mo pa din sa room kanina si ash nung pauwi sya?')
            return

        # ID ni Jorg
        if message.author.id == 312533659880259584:
            await message.channel.send('Jakol')
            return

        if user_message == '<@!312533659880259584>':
            await message.channel.send('Bakla yang tanginang yan')
            return

        if user_message == '<@!901304399777919077>':
            print(f'{username}: {user_message} ({channel})')
            await message.channel.send(autoreply)
            return

        elif 'fuck' in user_message:
            print(f'{username}: {user_message} ({channel})')
            await message.channel.send('Tangina mo bakla!!!')
            return
        elif '<@!901304399777919077>' in user_message:
            if 'fuck' in user_message:
                print(f'{username}: {user_message} ({channel})')
                await message.channel.send('Tangina mo bakla!!!')
                return
        elif user_message.lower() == 'hello':
            await message.channel.send("Naol")
            return

    if message.channel.name != '✉｜shitposting':
        if user_message.lower() == 'hello':
            await message.channel.send("Naolss")
            return
        if user_message.lower() == '<@!901304399777919077>':
            print(f'{username}: {user_message} ({channel})')
            await message.channel.send(f'Dili nalang ako magtalk')
            return

client.run(TOKEN)
