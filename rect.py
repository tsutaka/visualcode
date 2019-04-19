import pyxel

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100

start_chk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tile_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]


def draw_rect1():

    value_x = 0
    value_y = 0
    
    #draw line
    for cnt in range(10):
        pyxel.line(
            value_x, 
            value_y + cnt * 10, 
            value_x + SCREEN_WIDTH, 
            value_y + cnt * 10, 
            1)

    for cnt in range(10):
        pyxel.line(
            value_x + cnt * 10, 
            value_y, 
            value_x + cnt * 10, 
            value_y + SCREEN_HEIGHT, 
            1)
    return

def draw_rect2():

    value_x = 0
    value_y = 0

    if(pyxel.frame_count % 10 == 0):
        for index, cnt in enumerate(start_chk):
            if(cnt == 0):
                start_chk[index] = 1
                break

    for cnt in range(10):
        if(start_chk[cnt] > 0):
            if(start_chk[cnt] > 0 and start_chk[cnt] <= SCREEN_WIDTH):
                start_chk[cnt] += 1

            pyxel.line(
                value_x, 
                value_y + cnt * 10, 
                value_x + start_chk[cnt], 
                value_y + cnt * 10, 
                pyxel.frame_count % 16)

    for cnt in range(10):
        if(start_chk[cnt] > 0):
            if(start_chk[cnt] > 0 and start_chk[cnt] <= SCREEN_WIDTH):
                start_chk[cnt] += 1

            pyxel.line(
                value_x + cnt * 10, 
                value_y, 
                value_x + cnt * 10, 
                value_y + start_chk[cnt], 
                pyxel.frame_count % 16)
    return

def draw_rect3():

    draw_rect1()
    
    if(pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)):
        if(pyxel.mouse_y // 10 >= 0 and pyxel.mouse_y // 10 < 10 and 
            pyxel.mouse_x // 10 >= 0 and pyxel.mouse_x // 10 < 10):
            if(tile_matrix[pyxel.mouse_y // 10][pyxel.mouse_x // 10] < 256):
                tile_matrix[pyxel.mouse_y // 10][pyxel.mouse_x // 10] += 20
    
    for index_y, row in enumerate(tile_matrix):
        for index_x in range(len(row)):

            if(tile_matrix[index_y][index_x] > 0):
                tile_matrix[index_y][index_x] -= 1

            pyxel.rect(
                index_x * 10 + 1, 
                index_y * 10 + 1,
                (index_x + 1) * 10 - 1, 
                (index_y + 1) * 10 - 1,
                tile_matrix[index_y][index_x] % 16)
            
    return

class App:

    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="art")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        draw_rect3()


App()