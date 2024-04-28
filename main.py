import pygame
import evdev
import time

class ControlGamepad():
    def __init__(self, BUTTON, TRIGGER, STICK):
        self.Button = BUTTON
        self.Trigger = TRIGGER
        self.Stick = STICK

    def Btn(self, BUTTON_KEY, joystick):
        joystick.set_button(BUTTON_KEY, 1)
        time.sleep(0.1)
        joystick.set_button(BUTTON_KEY, 0)


pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()