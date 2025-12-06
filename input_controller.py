from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController

import time

class InputController:
    def __init__(self, speed=5):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.speed = speed # pixels per step

    # mouse movement
    def move_left(self):
        self.mouse.move(-self.speed, 0)

    def move_right(self):
        self.mouse.move(self.speed, 0)

    def move_up(self):
        self.mouse.move(0, -self.speed)

    def move_down(self):
        self.mouse.move(0, self.speed)

    # diagonal movement
    def move_up_left(self):
        self.mouse.move(-self.speed, -self.speed)

    def move_up_right(self):
        self.mouse.move(self.speed, -self.speed)

    def move_down_left(self):
        self.mouse.move(-self.speed, self.speed)

    def move_down_right(self):
        self.mouse.move(self.speed, self.speed)

    # click
    def click(self, button="left"):
        btn = Button.left if button == "left" else Button.right
        self.mouse.click(btn)

    # typing
    def type_text(self, text):
        for c in text:
            self.keyboard.press(c)
            self.keyboard.release(c)
            time.sleep(0.01)

    # press a single key
    def press_key(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    # change speed
    def set_speed(self, value):
        self.speed = value