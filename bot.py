import discord
from discord.ext import commands
import json 

with open('setting.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    print(bot.user)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome']))
    await channel.send(f'{member} joined!') 

@bot.event
async def on_member_remove(member): 
    channel = bot.get_channel(int(jdata['leave']))
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')


bot.run(jdata['Token']) 