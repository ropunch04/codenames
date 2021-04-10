import pygame as pg

class TextBox:
    pg.init()
    box_width, box_height = 270, 152
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    font1 = pg.font.SysFont('times', 24)
    font_style1 = font1
    font_style1.set_underline(True)

    font2 = pg.font.SysFont('times', 36)
    font_style2 = font2
    font_style2.set_underline(True)
    font_style2.set_bold(True)

    original_color = [200, 200, 200]
    selected_color = [253, 245, 232]

    normal_color = [236, 217, 196]
    red_color = [220, 0, 0]
    blue_color = [65, 105, 225]
    bomb_color = [128, 128, 128]

    def __init__(self, coords, text=''):
        self.color = self.original_color
        self.real_color = ''
        self.text = text
        self.coords = coords
        self.revealed = False
        self.small_text()
        pg.display.flip()
    
    def reset(self):
        pg.draw.rect(self.screen, self.color, (self.coords[0], self.coords[1], self.box_width, self.box_height))
    
    def small_text(self):
        if not self.revealed:
            self.color = self.original_color
        self.reset()
        text_obj = self.font1.render(self.text, True, (0,0,0))
        self.screen.blit(text_obj, self.get_center(text_obj))

    def large_text(self):
        if not self.revealed:
            self.color = self.selected_color
        self.reset()
        text_obj = self.font2.render(self.text, True, (0,0,0))
        self.screen.blit(text_obj, self.get_center(text_obj))
    
    def get_center(self, text_obj):
        horizontal = (self.get_width()/2) + self.coords[0] - (text_obj.get_width()/2)
        vertical = (self.get_height()/2) + self.coords[1] - (text_obj.get_height()/2)
        return (horizontal, vertical)

    def get_width(self):
        return self.box_width

    def get_height(self):
        return self.box_height

    def get_rect(self):
        return pg.Rect(self.coords[0], self.coords[1], self.box_width, self.box_height)

    def set_size(self, board_size):
        TextBox.box_width = (1390 - ((board_size - 1) * 10)) // board_size
        TextBox.box_height = (800 - ((board_size - 1) * 10)) // board_size

    def set_real_color(self, txt):
        switcher = {
            'normal' : self.normal_color,
            'red' : self.red_color,
            'blue' : self.blue_color,
            'bomb' : self.bomb_color
        }
        self.real_color = switcher.get(txt.lower())
        return self.real_color

    def set_text(self, txt):
        self.text = txt

    def reveal_color(self):
        self.color = self.real_color
        self.revealed = True
        self.small_text()