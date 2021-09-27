import pyxel

from utils import Vec, align_text, col_mouse_disc, DISC_HEIGHT

class Disc: 
    def __init__(self, x, y, w, color):
        self.pos = Vec(x, y)
        self.last_pos = Vec(x, y)
        self.weight = w
        self.color = color
        self.dragging = False

    def update(self):

        col_flag = 0
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            if col_mouse_disc(pyxel.mouse_x, pyxel.mouse_y, self.pos.x-self.weight-4, self.pos.y-3, self.weight*2+8):
                if not self.dragging:
                    self.dragging = True
                    self.last_pos.x = self.pos.x
                    self.last_pos.y = self.pos.y
        else:
            if self.dragging: 
                self.dragging = False
                col_flag = 1 

        if self.dragging:
            self.pos.x = pyxel.mouse_x
            self.pos.y = pyxel.mouse_y

        return col_flag

    def draw(self):
        pyxel.circ(self.pos.x-self.weight, self.pos.y, (DISC_HEIGHT/2), self.color)
        pyxel.circ(self.pos.x+self.weight, self.pos.y, (DISC_HEIGHT/2), self.color)
        pyxel.rect(self.pos.x-self.weight, self.pos.y-(DISC_HEIGHT/2)+1, self.weight*2, DISC_HEIGHT, self.color)
        pyxel.text(align_text(self.pos.x, str(self.weight)), self.pos.y-2, str(self.weight), 0)
