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
        
# 觸發(/v)
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == '/v':
            await msg.channel.send("當前運行版本: ")+(jdata['verison'])

# 觸發(早/中/晚安) ps.如加清單可以使多個字串觸發同一句話(當前尚未使用) 語法:定義字串keyword for ... in keyword
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('晚安'):
            random_ni = random.choice(jdata['night'])
            await msg.channel.send(random_ni)

        if msg.content.endswith('午安') and msg.author != self.bot.user:
            random_no = random.choice(jdata['noon'])
            await msg.channel.send(random_no)

        if msg.content == '早安' and msg.author != self.bot.user:
            random_mo = random.choice(jdata['morning'])
            await msg.channel.send('早安')

def setup(bot):
    bot.add_cog(Event(bot))