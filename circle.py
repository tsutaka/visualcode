import pyxel
import random # for get random num

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100

start_chk = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
    ]

def draw_circle1():

    # generator
    if(pyxel.frame_count % 30 == 0):
        for index in range(len(start_chk)):
            if(start_chk[index][0] == 0):
                start_chk[index][0] = 1
                start_chk[index][1] = random.randint(0, SCREEN_WIDTH)
                start_chk[index][2] = random.randint(0, SCREEN_HEIGHT)
                start_chk[index][3] = pyxel.frame_count % 16
                break

    # gupdate circle
    if(pyxel.frame_count % 3 == 0):
        for circle in start_chk:
            if(circle[0] > 0):
                circle[0] += 1

            if(circle[0] > SCREEN_WIDTH / 2):
                circle[0] = 0

    # draw circle
    for circle in start_chk:
        if(circle[0] > 0):
            pyxel.circb(
                circle[1], 
                circle[2],
                circle[0], 
                circle[3]
            )
            if(circle[3] % 3 == 0):
                pyxel.circb(
                    circle[1], 
                    circle[2],
                    circle[0] + 2, 
                    circle[3]
                )

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

        draw_circle1()


App()