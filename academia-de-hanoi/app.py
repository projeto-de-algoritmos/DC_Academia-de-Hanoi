import math
import random

import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

BUBBLE_MAX_SPEED = 1.8
BUBBLE_INITIAL_COUNT = 50
BUBBLE_EXPLODE_COUNT = 11


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Disc:
    def __init__(self):
        ...

    def update(self):
        ...

    def update(self):
        ...


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)


App()