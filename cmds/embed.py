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

class Embed(Cog_extension):

# 觸發(更新)
    @commands.command()
    async def update(self,ctx):
        embed=discord.Embed(title="Valoi Bot ", description="更新日誌", color=0x70cdf5,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Valoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/979994389021618198/980001844644446218/D2FDFA74-B5A2-4C2C-9C3E-204F04F22E55.jpg")
        embed.add_field(name="✚ 新增", value="• 圖片功能 \n•  \n•  \n•  \n• ", inline=True)
        embed.add_field(name="⟳ 修正", value="• 對話系統 ", inline=False)
        embed.add_field(name="━  移除", value="• .pic 指令 ", inline=False)
        embed.set_footer(text="Varoi B-1.0.4")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def bp(self,ctx):
        embed=discord.Embed(title="Valoi Bot ", description="男版圖片", color=0x70a7f0,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Valoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        random_boy = random.choice(jdata['boy'])
        embed.set_image(url=f'{random_boy}')
        
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def gp(self,ctx):
        embed=discord.Embed(title="Valoi Bot ", description="女版圖片", color=0xf45786,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Valoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        random_girl = random.choice(jdata['girl'])
        embed.set_image(url=f'{random_girl}')
        
        await ctx.send(embed=embed)
        await ctx.message.delete()




def setup(bot):
    bot.add_cog(Embed(bot))