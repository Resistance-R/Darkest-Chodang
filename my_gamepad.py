import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

def Press_Btn(btn):
    gamepad.press_button(button=btn)
    gamepad.update()

    time.sleep(0.1)

    gamepad.release_button(button=btn)
    gamepad.update()



def Press_LT():
    gamepad.left_trigger_float(value_float=1.0)
    gamepad.update()

    time.sleep(4)

    gamepad.left_trigger_float(value_float=0.0)
    gamepad.update()

def Press_RT():
    gamepad.right_trigger_float(value_float=1.0)
    gamepad.update()

    time.sleep(4)

    gamepad.right_trigger_float(value_float=0.0)
    gamepad.update()


def LStickL():
    gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
    gamepad.update()

    time.sleep(3)

    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()


def LStickR():
    gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
    gamepad.update()

    time.sleep(3)

    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def RStickU():
    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)
    gamepad.update()

    time.sleep(0.1)

    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def RStickD():
    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)
    gamepad.update()

    time.sleep(0.1)

    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def RStickL():
    gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)
    gamepad.update()

    time.sleep(0.1)

    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def RStickR():
    gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)
    gamepad.update()

    time.sleep(0.1)

    gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()