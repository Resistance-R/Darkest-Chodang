import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

while True:
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

    time.sleep(0.1)

    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    
    time.sleep(1)

    print("Debug")