import discord
from discord.ext import commands
import vgamepad as vg
import my_gamepad
import my_token

TOKEN = my_token.myToken
CHENNAL_ID = my_token.myChennal

A_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
B_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
X_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
Y_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y

Start_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
Back_BTN = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK

LB = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
RB = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

D_UP = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
D_DOWN = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
D_LEFT = vg.XUSB_BUTTON.USB_GAMEPAD_DPAD_LEFT
D_RIGHT = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user}로 로그인 완료')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Controller for Dakest Dungeon"))

"""BUTTONS"""

@bot.command(aliases = ['A', 'a'])
async def press_a(ctx):
    my_gamepad.Press_Btn(A_BTN)

@bot.command(aliases = ['B', 'b'])
async def press_b(ctx):
    my_gamepad.Press_Btn(B_BTN)

@bot.command(aliases = ['X', 'x'])
async def press_x(ctx):
    my_gamepad.Press_Btn(X_BTN)

@bot.command(aliases = ['Y', 'y'])
async def press_y(ctx):
    my_gamepad.Press_Btn(Y_BTN)

@bot.command(aliases = ['start'])
async def press_start(ctx):
    my_gamepad.Press_Btn(Start_BTN)

@bot.command(aliases = ['back'])
async def press_back(ctx):
    my_gamepad.Press_Btn(Back_BTN)

@bot.command(aliases = ['+U', '+u'])
async def press_du(ctx):
    my_gamepad.Press_Btn(D_UP)

@bot.command(aliases = ['+D', '+d'])
async def press_dd(ctx):
    my_gamepad.Press_Btn(D_DOWN)

@bot.command(aliases = ['+L', '+l'])
async def press_dl(ctx):
    my_gamepad.Press_Btn(D_LEFT)

@bot.command(aliases = ['+R', '+r'])
async def press_dr(ctx):
    my_gamepad.Press_Btn(D_RIGHT)

@bot.command(aliases = ['LB', 'lb'])
async def press_lb(ctx):
    my_gamepad.Press_Btn(LB)

@bot.command(aliases = ['RB', 'rb'])
async def press_rb(ctx):
    my_gamepad.Press_Btn(RB)

"""TRIGGERS"""

@bot.command(aliases = ['LT', 'lt'])
async def press_lt(ctx):
    my_gamepad.Press_LT()

@bot.command(aliases = ['RT', 'rt'])
async def press_lt(ctx):
    my_gamepad.Press_RT()

bot.run(TOKEN)