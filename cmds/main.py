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
client = discord.Client()

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

class Main(Cog_extension):
        
# 指令(ping)
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'當前ping值: {round(self.bot.latency*1000)} /毫秒')

# 指令(版本)
    @commands.command()
    async def version(self,ctx):
        await ctx.send("當前運行版本: "+jdata['version'])

# 指令(時間)
    @commands.command()
    async def time(self,ctx):
        await ctx.send(dt.now().strftime("當前時間:%H:%M:%S"))

# 指令(日期)
    @commands.command()
    async def date(self,ctx):
        await ctx.send(dt.now().strftime("當前日期:%Y/%m/%d"))

# 指令(負語錄)
    @commands.command()
    async def ne(self,ctx):
        random_ne = random.choice(jdata['negative'])
        await ctx.send(random_ne)

# 指令(正語錄)
    @commands.command()
    async def po(self,ctx):
        random_po = random.choice(jdata['positive'])
        await ctx.send(random_po)

# 指令(機器人訊息)
    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

# 指令(清理訊息)
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'```diff\n+ 已刪除 {num} 則訊息\n' + '```')


    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)



def setup(bot):
    bot.add_cog(Main(bot))