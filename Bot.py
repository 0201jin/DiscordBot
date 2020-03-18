import discord
import re
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = 'r!')
search = [""]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('통제! 검열!'))
    print('언론! 검열! 통제!')
    f = open("search.txt", 'r')
    while True:
        line = f.readline()
        if not line: break
        search[i] = line
    f.close()

@bot.event
async def on_message(message):
    print(message.content)

    for i in range(0, len(search), 1):
        if search[i] in message.content:
            await message.delete()
            return

    korean = re.compile('[\u3131-\u3163]+')
    chat = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》1234567890]', '', message.content.replace(" ", "").lower())
    chat = re.sub(korean, '', chat)

    for i in range(0, len(search), 1):
        if search[i] in chat:
            await message.delete()
            return

    chat = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》1234567890qwertyuiopasdfghjklzxcvbnm]', '', message.content.replace(" ", "").lower())

    for i in range(0, len(search), 1):
        if search[i] in chat:
            await message.delete()
            return

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)