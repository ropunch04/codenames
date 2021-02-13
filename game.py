import pygame

class Game():
    def __init__(self, board):
        self.board = board
    def run(self):
        pygame.init()
        pygame.display.set_mode((800, 800))
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            pygame.display.flip()
        pygame.quit()