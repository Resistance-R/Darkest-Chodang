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


