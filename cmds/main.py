# 指令系統 
# 系統預設設定
import datetime
import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
from datetime import datetime as dt
import time

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

class Main(Cog_extension):
        
# 觸發(ping)
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'當前ping值: {round(self.bot.latency*1000)} /毫秒')

# 觸發(網址圖片)
    @commands.command()
    async def pic(self,ctx):
        random_pic = random.choice(jdata['pic-url'])
        await ctx.send(random_pic)

# 觸發(版本)
    @commands.command()
    async def verison(self,ctx):
        await ctx.send("當前運行版本: "+jdata['verison'])

# 觸發(時間)
    @commands.command()
    async def time(self,ctx):
        await ctx.send(dt.now().strftime("當前時間:%H:%M:%S"))

# 觸發(日期)
    @commands.command()
    async def date(self,ctx):
        await ctx.send(dt.now().strftime("當前日期:%Y/%m/%d"))

# 觸發(負語錄)
    @commands.command()
    async def ne(self,ctx):
        random_ne = random.choice(jdata['negative'])
        await ctx.send(random_ne)

# 觸發(正語錄)
    @commands.command()
    async def po(self,ctx):
        random_po = random.choice(jdata['positive'])
        await ctx.send(random_po)

# 觸發(機器人訊息)
    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

# 觸發(清理訊息)
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'```diff\n+ 已刪除{num}則訊息\n' + '```')

def setup(bot):
    bot.add_cog(Main(bot))