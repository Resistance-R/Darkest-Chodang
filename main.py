import sys
import evdev
from evdev import InputDevice, categorize, ecodes

CENTER_TOLERANCE = 350
STICK_MAX = 65536
 
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
count = 0
 
for device in devices:
    #print(device.path, device.name, device.phys)
    if device.name.startswith('Microsoft X-Box 360 pad'):
        gamepad = InputDevice(device.path)
        count = 1
        break
if count < 1:
    print("No usb gamepad found.")
    sys.exit()

A_Btn = 304
B_Btn = 305
X_Btn = 307
Y_Btn = 308

L_Btn = 310
R_Btn = 311

Back_Btn = 314
Start_Btn = 315

axis = {
    ecodes.ABS_HAT0X: 'dpad_x',
    ecodes.ABS_HAT0Y: 'dpad_y',
    # ecodes.ABS_X: 'ls_x',
    # ecodes.ABS_Y: 'ls_y',
    # ecodes.ABS_RX: 'rs_x',
    # ecodes.ABS_RY: 'rs_y'
}

center = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}

last = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}

"""
Debug
"""

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == A_Btn:
                print("A Button Pressed.")
            elif event.code == B_Btn:
                print("B Button Pressed.")
            elif event.code == X_Btn:
                print("X Button Pressed.")
            elif event.code == Y_Btn:
                print("Y Button Pressed.")
            elif event.code == L_Btn:
                print("L Button Pressed.")
            elif event.code == R_Btn:
                print("R Button Pressed.")
            elif event.code == Back_Btn:
                print("Back Button Pressed.")
            elif event.code == Start_Btn:
                print("Start Button Pressed.")

        elif event.value == 0:
            print("Button Released.")    

    elif event.type == ecodes.EV_ABS:
        if event.code in axis:
            if axis[event.code] in ['ls_x', 'ls_y', 'rs_x', 'rs_y']:
                last[axis[event.code]] = event.value
                value = event.value - center[axis[event.code]]
                if abs(value) <= CENTER_TOLERANCE:
                    value = 0

                if axis[event.code] == 'rs_x':
                    if value < 0:
                        print('left')
                    else:
                        print('right')
                    print(value)

                elif axis[event.code] == 'ls_y':
                    if value < 0:
                        print('foreward')
                    else:
                        print('backward')
                    print(value)
