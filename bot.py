# 系統預設設定
import discord
from discord.ext import commands
import json 
import random
import os

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

#機器人上線
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@bot.event
async def on_ready():
    state = ("======== 機器人上線 =========\n"
    " 登錄系統端: " + str(bot.user) +"\n"
    " 系統端版本: " + (jdata['verson']) +"\n"
    "==========================")
    print(state)
    channel = bot.get_channel(int(jdata['data']))
    await channel.send(state)  

# 加入訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome']))
    await channel.send(f'{member} joined!') 

#離開訊息
@bot.event
async def on_member_remove(member): 
    channel = bot.get_channel(int(jdata['leave']))
    await channel.send(f'{member} leave!')

# 觸發(ping)
    await ctx.send(f'{round(bot.latency*1000)} ms')

# 觸發(網址圖片)
    random_pic = random.choice(jdata['pic-url'])
    await ctx.send(random_pic)

if __name__ == "__main__":
    bot.run(jdata['Token']) 