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

class Load(Cog_extension):
    
    # 載入/重載/卸載
    @commands.command()
    async def load(self,ctx,extension):
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send("載入完成...")

    @commands.command()
    async def unload(self,ctx,extension):
        self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send("卸載完成...")

    @commands.command()
    async def reload(self,ctx,extension):
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send("重載完成...")

        

def setup(bot):
    bot.add_cog(Load(bot))