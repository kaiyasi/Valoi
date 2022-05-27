# 指令系統 
# 系統預設設定
import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
import os

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)

class Event(Cog_extension):
        
# 加入訊息
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome']))
        await channel.send(f'⇏ {member.mention} 加入塔爾小鎮 \n 歡迎歡迎') 

#離開訊息
    @commands.Cog.listener()
    async def on_member_remove(self,member): 
        channel = self.bot.get_channel(int(jdata['leave']))
        await channel.send(f'⇍ {member.mention} 遷出塔爾小鎮 \n 希望可以再度遷回')

# 觸發(文句)
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == '/verison':
            await msg.channel.send("當前運行版本: "+ jdata['verison'])

def setup(bot):
    bot.add_cog(Event(bot))