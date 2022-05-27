# 系統預設設定
import discord
from discord.ext import commands
import json 
import random
import os
from datetime import datetime as dt

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

#機器人上線
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@bot.event
async def on_ready():
    state = ("===============================\n" 
    "    當前狀態: :green_circle: 運行中..." + "\n"
    "    登錄系統端: " + str(bot.user) +"\n"
    "    系統端版本: " + (jdata['verison']) +"\n"
    "    當前時間:" + dt.now().strftime("%Y/%m/%d %H:%M:%S")+"\n"
    "===============================")
    print(state)
    channel = bot.get_channel(int(jdata['data']))
    await channel.send(state)  

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
        


if __name__ == "__main__":
    bot.run(jdata['Token']) 