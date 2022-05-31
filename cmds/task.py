from ast import Expression
import datetime
import discord
from discord.ext import commands
from core.classes import Cog_extension
import json,asyncio,datetime
from datetime import datetime as dt
import time

class Task(Cog_extension):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(979997119689682958)
            while not self.bot.is_closed():
                with open('setting.json','r',encoding='utf8') as jfile:
                        jdata = json.load(jfile)
                await self.channel.send('系統運行中...')
                await asyncio.sleep(int(jdata['settime']))

        self.bg_task = self.bot.loop.create_task(interval())

#指定時間做某某事件  (時間計算方式 : 下午04:26 = 1626)
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(979997119689682958)
            self.counter = 0
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json','r',encoding='utf8') as jfile:
                        jdata = json.load(jfile)
                if now_time == jdata['set_time'] and self.counter == 0:
                        await self.channel.send('Test Working')
                        self.counter = 1
                        await asyncio.sleep(1)
                else:
                        await asyncio.sleep(1)
                        pass

        self.bg_task = self.bot.loop.create_task(time_task())


    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'頻道設置完成 位置: {self.channel.mention}')

    @commands.command()
    async def set_time(self,ctx,time):
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)

        jdata['set_time'] = time
        with open('setting.json','w',encoding='utf8') as jfile:
            self.counter = 0
            json.dump(jdata,jfile,indent=4)

    @commands.command()
    async def settime(self,ctx,time):
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)

        jdata['settime'] = time
        with open('setting.json','w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)



def setup(bot):
    bot.add_cog(Task(bot))