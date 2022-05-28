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

# 觸發(版本)
    @commands.command()
    async def verison(self,ctx):
        await ctx.send("當前運行版本: "+jdata['verison'])

# 觸發(時間)
    @commands.command()
    async def time(self,ctx):
        await ctx.send(dt.now().strftime("當前時間:%H:%M:%S"))

# 觸發(日期)
    @commands.command()
    async def date(self,ctx):
        await ctx.send(dt.now().strftime("當前日期:%Y/%m/%d"))

# 觸發(負語錄)
    @commands.command()
    async def ne(self,ctx):
        random_ne = random.choice(jdata['negative'])
        await ctx.send(random_ne)

# 觸發(正語錄)
    @commands.command()
    async def po(self,ctx):
        random_po = random.choice(jdata['positive'])
        await ctx.send(random_po)

# 觸發(更新)
    @commands.command()
    async def update(self,ctx):
        embed=discord.Embed(title="Valoi Bot ", description="更新日誌", color=0x70cdf5,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="亞瑟王#1273", icon_url="https://i.imgur.com/br7SNUs.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/979994389021618198/980001844644446218/D2FDFA74-B5A2-4C2C-9C3E-204F04F22E55.jpg")
        embed.add_field(name="✚ 新增", value="• 幹話語錄 \n• 日期指令 \n• 傳送自訂訊息 \n• 刪除訊息", inline=True)
        embed.add_field(name="⟳ 修正", value="• 對話系統", inline=False)
        embed.set_footer(text="Varoi B-1.0.4")
        await ctx.send(embed=embed)


# 觸發(機器人訊息)
    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

# 觸發(清理訊息)
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'```diff\n+ 已刪除{num}則訊息\n' + '```')

def setup(bot):
    bot.add_cog(Main(bot))