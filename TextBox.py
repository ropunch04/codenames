import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 800))
screen.fill([0, 0, 0])
FONT = pg.font.Font(None, 32)

class TextBox():
    def __init__(self, x, y , w, h, color, size, text = ''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.size = size
        self.text = text
        self.createText()
    
    def createText(self):
        pass
