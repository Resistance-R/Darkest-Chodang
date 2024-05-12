import sys, time
import evdev
from evdev import UInput, InputDevice, ecodes as e
import evdev.eventio

CENTER_TOLERANCE = 350
STICK_MAX = 65536
 
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
count = 0
ui = UInput()
 
for device in devices:
    #print(device.path, device.name, device.phys)
    if device.name.startswith('Microsoft X-Box 360 pad'):
        dev = InputDevice(device.path)
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

while True:
    ui.write(e.EV_KEY, e.BTN_A, 1)
    ui.syn()
    time.sleep(0.1)
    ui.write(e.EV_KEY, e.BTN_A, 0)
    ui.syn()
    time.sleep(1)
    print("Debug")