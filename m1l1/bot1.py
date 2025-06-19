import discord
from discord.ext import commands
from config import token
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def toplama (ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def carpma (ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)


@bot.command()
async def cikarma (ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def bölme (ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)


@bot.command()
async def mem1(ctx):
    with open("images/mem1.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open("images/mem2.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open("images/mem3.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir("images"))

bot.run(token)