import discord
import re
import os
import csv
import threading
import datetime
from discord.ext import commands

text_channel_list = []
bot = commands.Bot(command_prefix = '')

@bot.event
async def on_message(message):
    if message.content.find("슷칼봇 주식 정보") != -1:
       chat = message.content.replace("`", "").split()

       date = chat[4] + ' ' + chat[5] + ' ' + chat[6] + ' ' + chat[7] + ' ' + chat[8]
       #19 24 29 34 39 44 49 54 59 64 69 74 79 84 89
       
       f = open('SkileBotData.csv','r', encoding = 'utf-8')
       rdr = csv.reader(f)
 
       for line in rdr:
           if line[0].find(date) != -1:
               print("중복!")
               return None
 
       f.close()

       f = open('SkileBotData.csv', 'a', newline='')
       wr = csv.writer(f)
       wr.writerow([date, chat[19], chat[24], chat[29], chat[34], chat[39], chat[44], chat[49], chat[54], chat[59], chat[64], chat[69], chat[74], chat[79], chat[84], chat[89], 0])
       f.close()
       print("기록!")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('데이터 수집 중'))
    print('시작')
    
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
