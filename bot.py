import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(972718100019548203)
    await channel.send(f"{member} join!")    

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(972718100019548203)
    await channel.send(f"{member} leave!")    

bot.run('OTc5MTk4MjAwODY0OTk3Mzg3.Gx1bK8.hsgSnWGAGIs4ZzM_58XUKmpnNWrM_bxFiv_XGs')