import random
import pygame as pg
from TextBox import TextBox


class Game:
    pg.init()
    pg.display.set_caption('Codenames')
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen.fill([255, 255, 255])

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
    g = Game(5)
    g.run()
