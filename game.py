import pygame as pg
from TextBox import TextBox

class Game:
    pg.init()
    pg.display.set_caption('Codenames')
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen.fill([255, 255, 255])

    def __init__(self, size = 5):
        # TextBox.set_size([])
        self.box_arr = []
        for x in range(0, size):
            for y in range(0, size):
                txt = TextBox([25 + (TextBox.get_width(TextBox) + 10) * x, 25 + (TextBox.get_height(TextBox) + 10) * y], 'Test!')
                self.box_arr.append(txt)
        
    def assign_color(self, arr):
        


    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_SPACE):
                        running = False
                elif (event.type == pg.QUIT):
                    running = False
                elif (event.type == pg.MOUSEBUTTONDOWN):
                    x, y = event.pos
                    for z in self.box_arr:
                        if z.get_rect().collidepoint(x, y):
                            z.reveal_color()
                for x in self.box_arr:
                    if x.get_rect().collidepoint(pg.mouse.get_pos()):
                        x.large_text()
                    else:
                        x.small_text()
            pg.display.flip()
        pg.quit()

if __name__ == "__main__":
    g = Game()
    g.run()
