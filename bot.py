import discord
from discord.ext import commands
import my_token

TOKEN = my_token.myToken
CHENNAL_ID = my_token.myChennal

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}로 로그인 완료')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Controller for Dakest Dungeon"))

@bot.command(aliases = ['hello', '인사', '안녕', '안녕하세요'])
async def greeting(ctx):
    await ctx.send("{}, 안녕하세요".format(ctx.author.mention))

@bot.command()
async def leave(ctx):
	await bot.voice_clients[0].disconnect()

bot.run(TOKEN)