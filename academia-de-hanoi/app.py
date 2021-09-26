import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

DISC_HEIGHT = 7
TOWER_HEIGHT = 50

# is_dragging = None

def col_mouse_disc(mx, my, x, y, w):
    if (x+w > mx > x) and (y+DISC_HEIGHT > my > y):
        return True

def col_tower_disc(tx, dx, dy, dw):
    if (dx+dw > tx > dx-dw) and (dy>SCREEN_HEIGHT-TOWER_HEIGHT-10):
        return True

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tower:
    def __init__(self, x, y):
        self.discs = []
        self.pos = Vec(x, y)

    def update(self):

        if self.discs != []:
            col_flag = self.discs[-1].update()
            return col_flag

    def draw(self):
        pyxel.rect(self.pos.x-1, self.pos.y-TOWER_HEIGHT, 3, TOWER_HEIGHT, 7)
        pyxel.rect(self.pos.x-10, self.pos.y, 21, 3, 7)

class Disc:
    
    def __init__(self, x, y, w, color):
        self.pos = Vec(x, y)
        self.last_pos = Vec(x, y)
        self.weight = w
        self.color = color
        self.dragging = False

    def update(self):
        
        # global is_dragging

        col_flag = 0
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            if col_mouse_disc(pyxel.mouse_x, pyxel.mouse_y, self.pos.x-self.weight-4, self.pos.y-3, self.weight*2+8):
                if not self.dragging: # and not is_dragging:
                    self.dragging = True
                    # is_dragging = True
                    self.last_pos.x = self.pos.x
                    self.last_pos.y = self.pos.y
        else:
            # print(self.dragging)
            # print(is_dragging)
            if self.dragging: # and is_dragging:
                # is_dragging = False
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

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)

        self.dragging_disc = True
        self.total_discs = 6

        self.towers = [] 
        self.towers.append(Tower(SCREEN_WIDTH/6, SCREEN_HEIGHT-5))
        self.towers.append(Tower((SCREEN_WIDTH/2), SCREEN_HEIGHT-5))
        self.towers.append(Tower((SCREEN_WIDTH/6)*5, SCREEN_HEIGHT-5))

        for i in range(0, self.total_discs):   
            self.towers[0].discs.append(Disc(self.towers[0].pos.x, 246-(8*i), (5*self.total_discs)-(i*5), 3+i))      

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.dragging_disc = False
        for tower in self.towers:
            if tower.discs != [] and tower.discs[-1].dragging:
                self.dragging_disc = True

        for tower in self.towers:
            if self.dragging_disc == False or tower.discs != [] and tower.discs[-1].dragging:
                if tower.update() == 1:
                    restore_pos = True
                    disc = tower.discs[-1]
                    if  col_tower_disc(self.towers[0].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        # print("Disco na Torre 0")
                        if self.towers[0].discs == [] or self.towers[0].discs[-1].weight > disc.weight:
                            restore_pos = False
                            tower.discs[-1].pos.x = self.towers[0].pos.x
                            tower.discs[-1].pos.y = 246-(8*len(self.towers[0].discs))
                            self.towers[0].discs.append(tower.discs.pop())
                    elif col_tower_disc(self.towers[1].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        # print("Disco na Torre 1")
                        if self.towers[1].discs == [] or self.towers[1].discs[-1].weight > disc.weight:
                            restore_pos = False
                            tower.discs[-1].pos.x = self.towers[1].pos.x
                            tower.discs[-1].pos.y = 246-(8*len(self.towers[1].discs))
                            self.towers[1].discs.append(tower.discs.pop())
                    elif col_tower_disc(self.towers[2].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        # print("Disco na Torre 2")
                        if self.towers[2].discs == [] or self.towers[2].discs[-1].weight > disc.weight:
                            restore_pos = False
                            tower.discs[-1].pos.x = self.towers[2].pos.x
                            tower.discs[-1].pos.y = 246-(8*len(self.towers[2].discs))
                            self.towers[2].discs.append(tower.discs.pop())

                    
                
                
                    if restore_pos:
                        tower.discs[-1].pos.x = tower.discs[-1].last_pos.x
                        tower.discs[-1].pos.y = tower.discs[-1].last_pos.y



    def draw(self):
        pyxel.cls(0)

        for tower in self.towers:
            tower.draw()

        for tower in self.towers:
            for disc in tower.discs:
                disc.draw()

App()

# organizar o posicionamento 
# so pode pegar um de cada vez