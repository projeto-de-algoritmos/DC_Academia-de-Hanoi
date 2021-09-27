from typing import Tuple
import pyxel

from utils import SCREEN_HEIGHT, SCREEN_WIDTH, calc_hanoi_solution, transfer_disc, col_tower_disc, align_text
from tower import Tower
from disc import Disc
import buttons as bt
   
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Academia de Hanoi")
        pyxel.mouse(True)

        self.bt_start = bt.CircleButton(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "Start!", 25)
        self.bt_minus = bt.PushButton(SCREEN_WIDTH/2-20, SCREEN_HEIGHT/2-60, "-", 5)
        self.bt_plus  = bt.PushButton(SCREEN_WIDTH/2+20, SCREEN_HEIGHT/2-60, "+", 5)
        self.bt_solve = bt.RectButton(25, 35, "Solve", 40, 15)
        self.moves = 0
        self.dragging_disc = True
        self.total_discs = 5
        self.is_solving = False
        self.win = False
        self.timer = 0
        self.step = 0
        self.solution = []
        self.minimin_moves = 2**self.total_discs - 1

        self.state = "MENU"

        self.towers = [] 
        self.towers.append(Tower(SCREEN_WIDTH/6, SCREEN_HEIGHT-5, 0, "A"))
        self.towers.append(Tower((SCREEN_WIDTH/2), SCREEN_HEIGHT-5,  1, "B"))
        self.towers.append(Tower((SCREEN_WIDTH/6)*5, SCREEN_HEIGHT-5, 2, "C"))

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.state == "MENU":
            self.bt_start.update()
            if self.bt_plus.update():
                if self.total_discs < 7:
                    self.total_discs += 1
            if self.bt_minus.update():
                if self.total_discs > 3:
                    self.total_discs -= 1

            if self.bt_start.is_on:
                self.bt_start.is_on = False
                self.bt_start.text = "Restart"
                self.state = "GAME"

                self.minimin_moves = 2**self.total_discs - 1
                self.moves = 0
                self.timer = 0
                self.is_solving = False
                self.win = False
                self.step = 0
                self.solution = []

                for tower in self.towers:
                    tower.reset(self.total_discs)
        
        elif self.state == "GAME":
            if not self.win:
                if pyxel.frame_count % 30 == 0:
                    self.timer += 1
            else:
                self.bt_start.update()

            if self.bt_start.is_on:
                self.bt_start.is_on = False
                self.bt_start.text = "Start"
                self.bt_solve.text = "Solve"
                self.total_discs = 5
                self.state = "MENU"


            if len(self.towers[2].discs) == self.total_discs:
                self.win = True
                

            if not self.bt_solve.is_on:
                self.bt_solve.update()
            else:
                self.bt_solve.is_on = False
                self.is_solving = True
                self.bt_solve.text = "Solving"

                self.step = -1
                self.moves = 0
                self.timer = 0

                for tower in self.towers:
                    tower.reset(self.total_discs)

                calc_hanoi_solution(self.total_discs, self.towers[0], self.towers[2], self.towers[1], self.solution)

            if self.is_solving:
                if not self.win and pyxel.frame_count%30 == 0:
                    
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

        if self.state == "MENU":
            self.bt_start.draw()
            pyxel.text(align_text(SCREEN_WIDTH/2, "Discs"), SCREEN_HEIGHT/2-80, "Discs", 7)
            self.bt_plus.draw()
            pyxel.text(align_text(SCREEN_WIDTH/2, f"{self.total_discs}"), SCREEN_HEIGHT/2-60, f"{self.total_discs}", 7)
            
            self.bt_minus.draw()
        elif self.state == "GAME":
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
                pyxel.text(align_text(SCREEN_WIDTH/2, text1), SCREEN_HEIGHT/2, text1, 7)        
                pyxel.text(align_text(SCREEN_WIDTH/2, text2), SCREEN_HEIGHT/2+6, text2, 7)        

            
            if self.win:
                self.bt_start.draw()
                if not self.is_solving:
                    pyxel.text(align_text(SCREEN_WIDTH/2,'CONGRATULATIONS :)'), SCREEN_HEIGHT/2-50, 'CONGRATULATIONS :)', 7)
            
            self.bt_solve.draw()

            for tower in self.towers:
                tower.draw()

            for tower in self.towers:
                for disc in tower.discs:
                    disc.draw()

App()