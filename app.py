# MTI0MjIwNDU1MjE3ODk2MjQ1Mg.GCcV9H.6tXa9cMnXAdjxjK9bD8vmsOKwJAFBppc1sRTfs
import discord
from discord.ext import commands

prefix = '!'
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix)


async def on_ready(self):
    print(f'{self.user} está online! !')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f':ping_pong: **Pong!** {round(bot.latency * 1000)}ms')

bot.run('MTI0MjIwNDU1MjE3ODk2MjQ1Mg.GCcV9H.6tXa9cMnXAdjxjK9bD8vmsOKwJAFBppc1sRTfs')