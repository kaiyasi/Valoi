# 系統預設設定
from tkinter.filedialog import SaveFileDialog
import discord
from discord.ext import commands
import json 
import random
import os
from datetime import datetime as dt
client = discord.Client()

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)




#機器人上線
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all(),help_command=None)
@bot.event

async def on_ready():

    #狀態顯示系統
    state = ("=============================\n"
    "   當前狀態: :green_circle: 運行中..." + "\n"
    "   登錄系統端: " + str(bot.user) +"\n"
    "   系統端版本: " + (jdata['version']) +"\n"
    "   當前時間: " + dt.now().strftime("%Y/%m/%d %H:%M:%S")+"\n"
    "=============================")
    print(state)
    channel = bot.get_channel(int(jdata['data']))
    await channel.send(state)

    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.watching, name="程式撰寫中...")

    await bot.change_presence(status= status_w, activity=activity_w)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['Token']) 