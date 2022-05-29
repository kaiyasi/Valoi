import datetime
import discord
from discord.ext import commands
from core.classes import Cog_extension
import json,asyncio,datetime

class Task(Cog_extension):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

def setup(bot):
    bot.add_cog(Task(bot))