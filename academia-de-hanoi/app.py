import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

DISC_HEIGHT = 7
TOWER_HEIGHT = 50

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
    def __init__(self, x, y, h):
        self.discs = []
        self.pos = Vec(x, y)
        self.height = h

    def update(self):
        ...

    def draw(self):
        pyxel.rect(self.pos.x-1, self.pos.y-self.height, 3, self.height, 7)
        pyxel.rect(self.pos.x-10, self.pos.y, 21, 3, 7)

     

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

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)

        self.towers = [] 
        self.towers.append(Tower(SCREEN_WIDTH/6, SCREEN_HEIGHT-5, TOWER_HEIGHT))
        self.towers.append(Tower((SCREEN_WIDTH/2), SCREEN_HEIGHT-5, TOWER_HEIGHT))
        self.towers.append(Tower((SCREEN_WIDTH/6)*5, SCREEN_HEIGHT-5, TOWER_HEIGHT))

        self.total_discs = 6

        for i in range(0, self.total_discs):   
            self.towers[0].discs.append(Disc(self.towers[0].pos.x, 246-(8*i), (5*self.total_discs)-(i*5), 3+i))      

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.towers[0].update()
        self.towers[1].update()
        self.towers[2].update()

        for i in range(0, 3):
            if self.towers[i].discs != []:
                disc = self.towers[i].discs[-1]
                if disc.update() == 1:
                    if  col_tower_disc(self.towers[0].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        print("Torre 0!!!")
                    elif col_tower_disc(self.towers[1].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        print("Torre 1!!!")
                    elif col_tower_disc(self.towers[2].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                        print("Torre 2!!!")
                    else:
                        self.towers[i].discs[-1].pos.x = self.towers[i].discs[-1].last_pos.x
                        self.towers[i].discs[-1].pos.y = self.towers[i].discs[-1].last_pos.y

                # check col with one of the towers
                    # col happened
                    # last pos = pos
                    # tower X add another disc IF disc is smaller than top



    def draw(self):
        pyxel.cls(0)

        self.towers[0].draw()
        self.towers[1].draw()
        self.towers[2].draw()

        for disc in self.towers[0].discs:
            disc.draw()

        # for i in range(0, self.total_discs):
        #     self.discs[i].draw()

App()