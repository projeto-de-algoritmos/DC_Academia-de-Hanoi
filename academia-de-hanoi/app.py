import pyxel

import buttons as bt

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

DISC_HEIGHT = 7
TOWER_HEIGHT = 50

def col_mouse_disc(mx, my, x, y, w):
    if (x+w > mx > x) and (y+DISC_HEIGHT > my > y):
        return True
    else:
        return False

def col_tower_disc(tx, dx, dy, dw):
    if (dx+dw > tx > dx-dw) and (dy>SCREEN_HEIGHT-TOWER_HEIGHT-10):
        return True
    else:
        return False

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tower:
    def __init__(self, x, y, id, name):
        self.discs = []
        self.pos = Vec(x, y)
        self.id = id
        self.name = name

    def update(self):

        if self.discs != []:
            col_flag = self.discs[-1].update()
            return col_flag

    def draw(self):
        pyxel.rect(self.pos.x-1, self.pos.y-TOWER_HEIGHT, 3, TOWER_HEIGHT, 7)
        pyxel.rect(self.pos.x-10, self.pos.y, 21, 7, 7)
        
        pyxel.text(self.pos.x-1, self.pos.y, self.name, 8)

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

def transfer_disc(t_out: Tower, t_in: Tower):
    restore_pos = True
    
    if t_in.discs == [] or t_in.discs[-1].weight > t_out.discs[-1].weight:
        t_out.discs[-1].pos.x = t_in.pos.x
        t_out.discs[-1].pos.y = 246-(8*len(t_in.discs))
        t_in.discs.append(t_out.discs.pop())
        restore_pos = False

    return restore_pos

def calc_hanoi_solution(n, source, target, auxiliary, solution):

    if n > 0:
        calc_hanoi_solution(n - 1, source, auxiliary, target, solution)
        # print(f"Movendo disco da Torre {source.id}, para Torre {target.id}")
        solution.append((source.id, target.id))
        calc_hanoi_solution(n - 1, auxiliary, target, source, solution)
    
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)

        self.bt_solve = bt.RectButton(25, 35, "Solve", 40, 15)
        self.moves = 0
        self.dragging_disc = True
        self.total_discs = 3
        self.is_solving = False
        self.win = False
        self.timer = 0
        self.step = 0
        self.solution = []
        self.minimin_moves = 2**self.total_discs - 1

        self.towers = [] 
        self.towers.append(Tower(SCREEN_WIDTH/6, SCREEN_HEIGHT-5, 0, "A"))
        self.towers.append(Tower((SCREEN_WIDTH/2), SCREEN_HEIGHT-5,  1, "B"))
        self.towers.append(Tower((SCREEN_WIDTH/6)*5, SCREEN_HEIGHT-5, 2, "C"))

        for i in range(0, self.total_discs):   
            self.towers[0].discs.append(Disc(self.towers[0].pos.x, 246-(8*i), (5*self.total_discs)-(i*5), 3+i))      

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if not self.win:
            if pyxel.frame_count % 30 == 0:
                self.timer += 1

        if len(self.towers[2].discs) == self.total_discs:
            self.win = True

        if not self.bt_solve.is_on:
            self.bt_solve.update()
        else:
            if not self.is_solving:
                self.is_solving = True
                self.step = -1
                calc_hanoi_solution(self.total_discs, self.towers[0], self.towers[2], self.towers[1], self.solution)
            if not self.win and pyxel.frame_count%45 == 0:
                
                if self.step >= 0:
                    self.moves += not transfer_disc(self.towers[self.solution[self.step][0]], self.towers[self.solution[self.step][1]])

                if self.step < self.minimin_moves:
                    self.step+=1
            else:
                ... # Animação

        if not self.is_solving and not self.win:
            self.dragging_disc = False
            for tower in self.towers:
                if tower.discs != [] and tower.discs[-1].dragging:
                    self.dragging_disc = True

            for tower in self.towers:
                if self.dragging_disc == False or tower.discs != [] and tower.discs[-1].dragging:
                    if tower.update() == 1:
                        restore_pos = True
                        disc = tower.discs[-1]
                        if   col_tower_disc(self.towers[0].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                            restore_pos = transfer_disc(tower, self.towers[0])
                        elif col_tower_disc(self.towers[1].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                            restore_pos = transfer_disc(tower, self.towers[1])                  
                        elif col_tower_disc(self.towers[2].pos.x, disc.pos.x, disc.pos.y, disc.weight):
                            restore_pos = transfer_disc(tower, self.towers[2])                  
                    
                        if restore_pos:
                            tower.discs[-1].pos.x = tower.discs[-1].last_pos.x
                            tower.discs[-1].pos.y = tower.discs[-1].last_pos.y
                        self.moves += not restore_pos

    def draw(self):
        pyxel.cls(0)
        pyxel.text(SCREEN_WIDTH-45, 10, f"MOVES: {self.moves}", 7)
        pyxel.text(5, 10, f'TIMER: {(self.timer//60):02d}:{(self.timer%60):02d}', 7)

        if self.is_solving and not self.win and self.step < self.minimin_moves:

            if self.step < 0:
                step = self.step+1
            else:
                step = self.step

            tower_out = self.towers[self.solution[step][0]]
            tower_in  = self.towers[self.solution[step][1]]
            text1 = f'Movendo disco de peso {tower_out.discs[-1].weight}:'
            text2 = f'{tower_out.name} -> {tower_in.name}'
            pyxel.text(bt.align_text(SCREEN_WIDTH/2, text1), SCREEN_HEIGHT/2, text1, 7)        
            pyxel.text(bt.align_text(SCREEN_WIDTH/2, text2), SCREEN_HEIGHT/2+6, text2, 7)        

        
        if self.win and not self.is_solving:
            pyxel.text(bt.align_text(SCREEN_WIDTH/2,'CONGRATULATIONS :)'), SCREEN_HEIGHT/2, 'CONGRATULATIONS :)', 7)
        
        self.bt_solve.draw()

        for tower in self.towers:
            tower.draw()

        for tower in self.towers:
            for disc in tower.discs:
                disc.draw()

App()