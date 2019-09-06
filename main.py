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

    def has_resource(self, square):
        check = False
        for obj in square:
            if type(obj) == Resource:
                check = True
            elif obj == self:
                return False
        return check

    def grow(self, map):
        for i in range(1, 5):
            for x in range(-i, i):
                for y in range(-i, i):
                    if self.has_resource(map[self.x+x][self.y+y]):
                        if self.x < self.x + x:
                            map[self.x + 1][self.y].append(Empire)
                            return
                        elif self.x > selfx + x:
                            map[self.x - 1][self.y].append(Empire)
                            return
                        elif self.y < self.y + y:
                            Yside = self.y + 1
                            map[Xside][Yside].append(Empire)
                            return
                        elif self.y > self.y + y:
                            Yside = self.y - 1
                            map[Xside][Yside].append(Empire)
                            return


class Resource:
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power

    def draw(self):
        pass


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
        self.map = [[[] for j in range(self.win_height // self.win_sqr)] for i in range(self.win_width // self.win_sqr)]

    def spawn_res(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if randint(1, 100) <= self.res_prob:
                    self.map[x][y].append(Resource(x, y, randint(1, 100)))

    def spawn_empires(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if not self.map[x][y] and randint(1, 100) <= self.res_imp:
                    self.map[x][y].append(Empire(x, y))

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
