# 指令系統 
# 系統預設設定
from cmd import IDENTCHARS
import datetime
from http import client
from logging.config import IDENTIFIER
from ssl import CHANNEL_BINDING_TYPES
from xml.dom.minidom import Identified
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

class Embed(Cog_extension):



# 崁入(更新)
    @commands.command()
    async def update(self,ctx):
        embed=discord.Embed(title="Varoi Bot ", description="更新日誌", color=0x70cdf5,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/979994389021618198/980001844644446218/D2FDFA74-B5A2-4C2C-9C3E-204F04F22E55.jpg")
        embed.add_field(name="✚ 新增", value="• 機器人狀態系統 \n• 異步協成系統 \n• 指令大全 ", inline=True)
        embed.add_field(name="⟳ 更新", value="• 成員進出訊息 \n• Bot code程式碼 ", inline=False)
        #embed.add_field(name="━  移除", value="•  ", inline=False)
        embed.set_footer(text="Varoi " + jdata['version'])
        await ctx.send(embed=embed)
        await ctx.message.delete()

#崁入(男版圖片)
    @commands.command()
    async def bp(self,ctx):
        embed=discord.Embed(title="Varoi Bot ", description="男版圖片", color=0x70a7f0,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        random_boy = random.choice(jdata['boy'])
        embed.set_image(url=f'{random_boy}')
        embed.set_footer(text="Varoi " + jdata['version'])

        await ctx.send(embed=embed)
        await ctx.message.delete()

#崁入(女版圖片)
    @commands.command()
    async def gp(self,ctx):
        embed=discord.Embed(title="Varoi Bot ", description="女版圖片", color=0xf45786,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi開發團隊", icon_url="https://i.imgur.com/br7SNUs.jpg")
        random_girl = random.choice(jdata['girl'])
        embed.set_image(url=f'{random_girl}')
        embed.set_footer(text="Varoi " + jdata['version'])

        await ctx.send(embed=embed)
        await ctx.message.delete()

#崁入(指令大全)
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="Varoi 指令表", description="紀錄指令的使用方式", color=0xecfb7e,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi 開發團隊", icon_url="https://cdn.discordapp.com/attachments/979997119689682958/980632278747217950/OIP_1.jpg")
        embed.add_field(name=".help", value="獲得指令大全", inline=True)
        embed.add_field(name=".ping", value="查看當前延遲", inline=True)
        embed.add_field(name=".version", value="察看當前運行版本", inline=True)
        embed.add_field(name=".date", value="查看當天日期", inline=True)
        embed.add_field(name=".time", value="查看當前時間", inline=True)
        embed.add_field(name=".ne", value="隨機產生一句負面語錄", inline=True)
        embed.add_field(name=".po", value="隨機產生一句正面語錄", inline=True)
        embed.add_field(name=".say", value="讓機器人說話", inline=True)
        embed.add_field(name=".clear", value="清除訊息", inline=True)
        embed.add_field(name=".update", value="查看當前版本更新", inline=True)
        embed.add_field(name=".gp", value="隨機產生女版圖片", inline=True)
        embed.add_field(name=".bp", value="隨機產生男版圖片", inline=True)
        embed.set_footer(text="Varoi 開發團隊提供")

        await ctx.send(embed=embed)
        await ctx.message.delete()

#崁入(成員離開)
    @commands.Cog.listener()
    async def on_member_remove(self,member,):
        channel = self.bot.get_channel(int(jdata['leave']))
        embed=discord.Embed(title="居民紀錄", description="成員狀態:遷出", color=0xf54747,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi 開發團隊", icon_url="https://cdn.discordapp.com/attachments/979997119689682958/980632278747217950/OIP_1.jpg")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="成員:", value=f'{member.mention}', inline=True)
        embed.set_footer(text=f'{member.guild.name}')

        await channel.send(embed=embed)

#崁入(成員加入)
    @commands.Cog.listener()
    async def on_member_join(self,member): 
        channel = self.bot.get_channel(int(jdata['Welcome']))
        chanel = self.bot.get_channel(976093688210006116)
        embed=discord.Embed(title="居民紀錄", description="成員狀態:居住中", color=0x7ff467,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Varoi 開發團隊", icon_url="https://cdn.discordapp.com/attachments/979997119689682958/980632278747217950/OIP_1.jpg")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="成員:", value=f'{member.mention}', inline=False)
        embed.add_field(name=f'歡迎來到 **{member.guild.name}**',value=f'請先至 {chanel.mention} 詳閱規章喔',inline=False)
        embed.set_footer(text=f'{member.guild.name}')

        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Embed(bot))
