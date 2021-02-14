import pygame

class Game():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill([0, 0, 0])

    def __init__(self, board):
        self.board = board

    def updateScreen(self, color):
        self.screen.fill(color)
        pygame.display.flip()

    def run(self):
        running = True
        r, g, b = 0, 0, 0
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
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
        pygame.quit()

