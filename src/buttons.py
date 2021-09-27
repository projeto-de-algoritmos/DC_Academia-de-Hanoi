from math import dist
import pyxel

from utils import align_text, col_mouse_bt

class Button:

    def __init__(self, x, y, text):
        self.posx = x
        self.posy = y
        self.text = text
        self.offset = 4
        self.is_on = False

    def update(self):
        """Atualiza o estado do botão"""
        ...

    def draw(self):
        """Desenha o botão na tela"""
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
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4


    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, 5)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, 12)

        if self.is_on: txt_color = 8
        else: txt_color = 7
        
        pyxel.text(align_text(self.posx, self.text), self.posy-self.offset, self.text, txt_color)

class RectButton(Button):
    def __init__(self, x, y, text, w, h):
        super().__init__(x, y, text)
        self.width = w
        self.height = h
        
    def update(self):

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4
        

    def draw(self):
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width+self.offset, self.height+self.offset, 5)
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width, self.height, 12)

        if self.is_on: txt_color = 8
        else: txt_color = 7

        pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, txt_color)

class PushButton(Button):
    def __init__(self, x, y, text, r):
        super().__init__(x, y, text)
        self.radius = r
        self.offset = 2
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 2
            return True
        else:
            self.offset = 2

    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, 5)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, 12)
        
        pyxel.text(align_text(self.posx+1, self.text), self.posy-self.offset-1, self.text, 7)