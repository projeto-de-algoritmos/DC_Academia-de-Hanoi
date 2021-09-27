from math import dist
import pyxel

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True

class Button:
    def __init__(self, x, y, text):
        self.posx = x
        self.posy = y
        self.text = text
        self.offset = 4
        self.is_on = False

    def update(self):
        ...

    def draw(self):
        ...
        
class CircleButton(Button):
    def __init__(self, x, y, text, r):
        super().__init__(x, y, text)
        self.radius = r
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2

    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, 5)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, 12)

        if self.is_on: txt_color = 8
        else: txt_color = 7
        
        pyxel.text(align_text(self.posx, self.text), self.posy+17, self.text, txt_color)


class RectButton(Button):
    def __init__(self, x, y, text, w, h):
        super().__init__(x, y, text)
        self.width = w
        self.height = h
        
    def update(self):

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            self.offset = 0
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2
        

    def draw(self):
        pyxel.rect(self.posx-(self.width/2), self.posy-(self.height/2), self.width, self.height, 5)
        pyxel.rect(self.posx-(self.width/2), self.posy-(self.height/2)-self.offset, self.width, self.height, 12)

        if self.is_on: txt_color = 8
        else: txt_color = 7

        pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, txt_color)