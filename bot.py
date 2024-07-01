import discord
from discord.ext import commands
import vgamepad as vg
import my_gamepad
import my_token

TOKEN = my_token.myToken
CHENNAL_ID = my_token.myChannel

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
D_LEFT = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
D_RIGHT = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

command_counter = 0

@bot.event
async def on_ready():
    print(f'{bot.user}로 로그인 완료')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Controller for Darkest Dungeon"))

@bot.event
async def on_message(message):
    global command_counter

    if message.author == bot.user:
        return

    command_counter += 1

    if command_counter == 5:
        await execute_command(message)
        command_counter = 0

    await bot.process_commands(message)

async def execute_command(message):
    content = message.content.lower()
    if content.startswith('!a'):
        my_gamepad.Press_Btn(A_BTN)
    elif content.startswith('!b'):
        my_gamepad.Press_Btn(B_BTN)
    elif content.startswith('!x'):
        my_gamepad.Press_Btn(X_BTN)
    elif content.startswith('!y'):
        my_gamepad.Press_Btn(Y_BTN)
    elif content.startswith('!start'):
        my_gamepad.Press_Btn(Start_BTN)
    elif content.startswith('!back'):
        my_gamepad.Press_Btn(Back_BTN)
    elif content.startswith('!+u'):
        my_gamepad.Press_Btn(D_UP)
    elif content.startswith('!+d'):
        my_gamepad.Press_Btn(D_DOWN)
    elif content.startswith('!+l'):
        my_gamepad.Press_Btn(D_LEFT)
    elif content.startswith('!+r'):
        my_gamepad.Press_Btn(D_RIGHT)
    elif content.startswith('!lb'):
        my_gamepad.Press_Btn(LB)
    elif content.startswith('!rb'):
        my_gamepad.Press_Btn(RB)
    elif content.startswith('!lt'):
        my_gamepad.Press_LT()
    elif content.startswith('!rt'):
        my_gamepad.Press_RT()
    elif content.startswith('!lsl'):
        my_gamepad.LStickL()
    elif content.startswith('!lsr'):
        my_gamepad.LStickR()
    elif content.startswith('!rsu'):
        my_gamepad.RStickU()
    elif content.startswith('!rsd'):
        my_gamepad.RStickD()
    elif content.startswith('!rsl'):
        my_gamepad.RStickL()
    elif content.startswith('!rsr'):
        my_gamepad.RStickR()

    else:
        await message.channel.send(f"{message.content}은(는) 없거나 올바르지 않은 명령입니다.")

bot.run(TOKEN)