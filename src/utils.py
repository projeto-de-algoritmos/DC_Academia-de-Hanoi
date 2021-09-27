import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

DISC_HEIGHT = 7
TOWER_HEIGHT = 70
SOLVE_SPEED = 35

COLOR_LIST = [2, 5, 12, 3, 10, 9, 8,]

class Vec:
    # Classe para posição
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pick_color(id):
    return COLOR_LIST[id%len(COLOR_LIST)]

def align_text(x, str):
    """
        Centraliza o texto
    """
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True


def col_mouse_disc(mx, my, x, y, w):
    """
        Verifica o clique no disco
    """
    if (x+w > mx > x) and (y+DISC_HEIGHT > my > y):
        return True
    else:
        return False

def col_tower_disc(tx, dx, dy, dw):
    """
        Verifica a colisão do disco com a torre
    """
    if (dx+dw > tx > dx-dw) and (dy>SCREEN_HEIGHT-TOWER_HEIGHT-10):
        return True
    else:
        return False

def transfer_disc(t_out, t_in):
    """
        Transfere o discos entre as torres 

        t_out: torre de origem,    t_int: torre de destino
    """
    restore_pos = True
    
    if t_in.discs == [] or t_in.discs[-1].weight > t_out.discs[-1].weight:
        t_out.discs[-1].pos.x = t_in.pos.x
        t_out.discs[-1].pos.y = 246-(8*len(t_in.discs))
        t_in.discs.append(t_out.discs.pop())
        restore_pos = False

    return restore_pos

def calc_hanoi_solution(n, source, target, auxiliary, solution):
    """
        Calcula a solução para a Torre de Hanoi utilizando
        o template de dividir e conquistar

        n: número de discos,    
        source: torre inicial,   
        target: torre final,    
        auxiliary: torre intermediaria, 
        solution: lista da solução, 
    """
    if n > 0:
        calc_hanoi_solution(n - 1, source, auxiliary, target, solution)
        solution.append((source.id, target.id))
        calc_hanoi_solution(n - 1, auxiliary, target, source, solution)