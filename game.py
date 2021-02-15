import pygame as pg

class Game():
    pg.init()
    screen = pg.display.set_mode((800, 800))
    screen.fill([0, 0, 0])

    def __init__(self, board):
        self.board = board

    def updateScreen(self, color):
        self.screen.fill(color)
        pg.display.flip()

    def run(self):
        running = True
        r, g, b = 0, 0, 0
        while running:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            for r in range(256):
                COLOR  = [r, g, b]
                self.updateScreen(COLOR)
            for g in range(256):
                COLOR = [r, g, b]
                self.updateScreen(COLOR)
            for b in range(256):
                COLOR  = [r, g, b] 
                self.updateScreen(COLOR)
            print("RED: ", r)
            print("GREEN: ", g)
            print("BLUE: ", b)
        pg.quit()

