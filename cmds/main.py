# 指令系統 
# 系統預設設定
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

class Main(Cog_Extension):
        
# 觸發(ping)
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

# 觸發(網址圖片)
    @commands.command()
    async def pic(self,ctx):
        random_pic = random.choice(jdata['pic-url'])
        await self.ctx.send(random_pic)


def setup(bot):
    bot.add_cog(Main(bot))