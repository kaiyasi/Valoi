# 系統預設設定
import discord
from discord.ext import commands
import json 

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

#機器人上線
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("====== 機器人上線 =======\n")
    print(" 登錄系統端: " + str(bot.user) +"\n")
    print(" 系統端版本: " + (jdata['verson']) +"\n")
    print("=========================")

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
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

# 觸發(圖片)
@bot.command()
async def pic(ctx):
    pic = discord.File('1d2426ba1a98b0d08d5cebb89d104656.png')
    await ctx.send(file= pic)



bot.run(jdata['Token']) 