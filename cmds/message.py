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
        

# 觸發(文句)
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == '/v':
            await msg.channel.send("當前運行版本: ")+(jdata['verison'])

def setup(bot):
    bot.add_cog(Event(bot))