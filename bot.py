import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio


prefix = "~"
token = "NTA3NjcxNjc2NDk5MjYzNTA4.Dr0FuA.mOh1-hmE0fbpjwx8EZq5va6WT8w"
bot = commands.Bot(command_prefix=prefix)

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')



@bot.command()
async def hello(ctx):
    '''
    : >Hey There!
    '''
    # Send it to the user
    hello = f"Hello there, {ctx.author}"
    hello = hello[:-5]
    hello += "!"
    filename = 'hellogifs\image'+str(random.randint(1,9))+'.gif'
    await ctx.send(hello,file=discord.File(filename))

bot.run(token)
