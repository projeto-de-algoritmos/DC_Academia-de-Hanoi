import pyxel

from utils import Vec, TOWER_HEIGHT, pick_color
from disc import Disc

class Tower:
    def __init__(self, x, y, id, name):
        self.discs = []
        self.pos = Vec(x, y)
        self.id = id
        self.name = name

    def update(self):
        """Atualiza o estado da torre e de seus respectivos discos"""
        if self.discs != []:
            col_flag = self.discs[-1].update()
            return col_flag

    def draw(self):
        """Desenha a torre na tela"""
        pyxel.rect(self.pos.x-1, self.pos.y-TOWER_HEIGHT, 3, TOWER_HEIGHT, 7)
        pyxel.rect(self.pos.x-10, self.pos.y, 21, 7, 7)
        
        pyxel.text(self.pos.x-1, self.pos.y, self.name, 8)

    def reset(self, n):
        """
            Reinicia a torre para o estado inicial
            
            n: número de discos
        """
        self.discs = []
        if self.id == 0:
            for i in range(0, n):   
                self.discs.append(Disc(self.pos.x, 246-(8*i), (5*n)-(i*5), pick_color(i)))
