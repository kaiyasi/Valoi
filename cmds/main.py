# 指令系統 
# 系統預設設定
import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json

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

# 觸發(對話 - Version)
    @commands.command()
    async def v(self,ctx):
        await ctx.send("當前運行版本: "+jdata['verison'])
    


def setup(bot):
    bot.add_cog(Main(bot))