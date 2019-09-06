import pygame
from random import randint, choice
from time import sleep


class Empire:  # при захвате столицы прибовлять процент от мощи
    def __init__(self, x, y):
        self.power = 0
        self.x = x
        self.y = y
        self.color = (0, 0, 0)

    def draw(self):
        pass


class Resource:
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power

    def draw(self):
        pass
    def grow(self, map, imperia, SweetPussy):
        for x in map:
            for y in map:
                if map[x][y] == imperia:
                    for i in range(-5, 5):
                        for j in range(-5, 5):
                            if map[x + i][y + i] == SweetPussy:
                                if x+i > 0: PussyCordsX = x+1
                                elif x+i < 0: PussyCordsX = x-1
                                else: PussyCordsX = x
                                if y+i > 0: PussyCordsY = y+1
                                elif y+i < 0: PussyCordsY = y-1
                                else: PussyCordsY = y
                                map[PussyCordsX][PussyCordsY] == imperia
                                break
                            else: continue



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Zabiv")
        self.run = True
        self.win_width = 1000
        self.win_height = 500
        self.win_sqr = 25
        self.res_prob = 10
        self.res_imp = 10
        self.empires = []
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.map = [['-' for j in range(self.win_height // self.win_sqr)] for i in range(self.win_width // self.win_sqr)]

    def spawn_res(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if randint(1, 100) <= self.res_prob:
                    self.map[x][y] = Resource(x, y, randint(1, 100))

    def spawn_empires(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y] == '-' and randint(1, 100) <= self.res_imp:
                    self.map[x][y] = Empire(x, y)

    def draw_empires(self):
        empire_count = len(self.empires)
        for i in range(empire_count):
            pass

    def start(self):
        self.spawn_res()
        self.spawn_empires()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.win.fill((0, 0, 0))
            for empire in self.empires:
                empire.draw()


pygame.quit()
