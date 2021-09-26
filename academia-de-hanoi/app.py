import math
import random

import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

BUBBLE_MAX_SPEED = 1.8
BUBBLE_INITIAL_COUNT = 50
BUBBLE_EXPLODE_COUNT = 11

def click_col(mx, my, x, y, w, h):
    if (x+w > mx > x) and (y+h > my > y):
        return True

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# class Tower:
#     def __init__()

class Disc:
    
    def __init__(self, x, y, w, color):
        self.pos = Vec(x, y)
        self.weight = w
        self.color = color
        self.dragging = False

    def update(self):

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            if click_col(pyxel.mouse_x, pyxel.mouse_y, self.pos.x-self.weight-1, self.pos.y-3, self.weight*2+1, 7):
                self.dragging = True
        else:
            self.dragging = False
        
        # if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
        
        if self.dragging:
            self.pos.x = pyxel.mouse_x
            self.pos.y = pyxel.mouse_y
            return True

    def draw(self):
        pyxel.circ(self.pos.x-self.weight, self.pos.y, 3, self.color)
        pyxel.circ(self.pos.x+self.weight, self.pos.y, 3, self.color)
        pyxel.line(self.pos.x+self.weight, self.pos.y, self.pos.x-self.weight, self.pos.y, self.color)
        pyxel.rect(self.pos.x-self.weight, self.pos.y-3, self.weight*2, 7, self.color)

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)

        self.discs = [] 
        self.total_discs = 6

        for i in range(0, self.total_discs):
            self.discs.append(Disc(128, 250-(8*i), (5*self.total_discs)-(i*5), 3))
            # self.discs.append(Disc(128-75, 250-(8*i), (5*self.total_discs)-(i*5), 3))
            # self.discs.append(Disc(128+75, 250-(8*i), (5*self.total_discs)-(i*5), 3))
      

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for i in range(0, self.total_discs):
            if(self.discs[i].update()): print("clicou no " + str(i))

    def draw(self):
        pyxel.cls(0)


        for i in range(0, self.total_discs):
            self.discs[i].draw()


App()