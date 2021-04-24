import random
import pygame as pg
from TextBox import TextBox


class Game:
    pg.init()
    pg.display.set_caption('Codenames')
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    # screen = pg.display.set_mode((1390,800))
    screen.fill([255, 255, 255])

    font1 = pg.font.SysFont('times', 30)
    font2 = pg.font.SysFont('times', 60)

    f = open("words.txt")

    def __init__(self, size = 5):
        self.size = size
        TextBox.set_size(TextBox, self.size)
        self.box_arr = []
        for x in range(0, size):
            for y in range(0, size):
                txt = TextBox([25 + (TextBox.get_width(TextBox) + 10) * x, 75 + (TextBox.get_height(TextBox) + 10) * y])
                self.box_arr.append(txt)
        random_c = self.randomize_array()
        self.assign_colors(random_c, self.box_arr)
        random_t = self.randomize_array()
        self.assign_text(random_t, self.box_arr)
        self.spymaster = pg.draw.rect(self.screen, [200, 200, 200], (1175, 25, 210, 40))
        text_obj = self.font1.render('Spymaster', True, (0,0,0))
        self.screen.blit(text_obj, (1220, 30))
        self.is_master = False


    def randomize_array(self):
        jumble = []
        for _ in range(self.size ** 2):
            while(True):
                index = random.randint(0, self.size ** 2 - 1)
                if index in jumble:
                    continue
                jumble.append(index)
                break
        return jumble
        
    def assign_colors(self, rand_arr, arr):
        red_bound = (self.size ** 2) // 3
        blue_bound = red_bound * 2 + 1
        num_bomb = self.size - 4
        for r in range(0, red_bound):
            arr[rand_arr[r]].set_real_color('red')
        for b in range(red_bound, blue_bound):
            arr[rand_arr[b]].set_real_color('blue')
        for n in range(blue_bound, len(rand_arr) - num_bomb):
            arr[rand_arr[n]].set_real_color('normal')
        for e in range(len(rand_arr) - num_bomb, len(rand_arr)):
            arr[rand_arr[e]].set_real_color('bomb')

    def assign_text(self, rand_arr, arr):
        words = open("words.txt").read().splitlines()
        for elem in rand_arr:
            arr[elem].set_text(random.choice(words))

    def confirmation(self):
        leave = False
        self.screen.fill([255, 255, 255])
        conf_text = self.font2.render('Are you sure you want to reveal all colors?', True, (0, 0, 0))
        self.screen.blit(conf_text, (185, 175))

        red = pg.draw.rect(self.screen, [255, 0, 0], (500, 300, 150, 150))
        red_text = self.font2.render('No', True, (0, 0, 0))
        self.screen.blit(red_text, (540, 340))

        green = pg.draw.rect(self.screen, [0, 255, 0], (800, 300, 150, 150))
        green_text = self.font2.render('Yes', True, (0, 0, 0))
        self.screen.blit(green_text, (825, 340))

        while (not leave):
            for event in pg.event.get():
                x, y = event.pos
                if (event.type == pg.MOUSEBUTTONDOWN):
                    if red.collidepoint(x, y):
                        returnVal = False
                        leave = True
                    elif green.collidepoint(x, y):
                        returnVal = True
                        leave = True
            pg.display.flip()
        self.screen.fill([255, 255, 255])
        return returnVal

    def show_spymaster(self):
        for box in self.box_arr:
            box.reveal_color()
        self.is_master = True

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_q):
                        running = False
                elif (event.type == pg.QUIT):
                    running = False
                elif (event.type == pg.MOUSEBUTTONDOWN):
                    x, y = event.pos
                    for box in self.box_arr:
                        if box.get_rect().collidepoint(x, y):
                            box.reveal_color()
                    if (self.spymaster.collidepoint(x, y) and self.is_master == False):
                        reveal = self.confirmation()
                        if (reveal):
                            self.show_spymaster()
                        else:
                            self.spymaster = pg.draw.rect(self.screen, [200, 200, 200], (1175, 25, 210, 40))
                            text_obj = self.font1.render('Spymaster', True, (0,0,0))
                            self.screen.blit(text_obj, (1220, 30))
                for x in self.box_arr:
                    if x.get_rect().collidepoint(pg.mouse.get_pos()):
                        x.large_text()
                    else:
                        x.small_text()
            pg.display.flip()
        pg.quit()

if __name__ == "__main__":
    g = Game(5)
    g.run()
