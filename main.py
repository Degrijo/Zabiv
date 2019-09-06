import pygame
from random import randint, choice
from time import sleep


class Empire:  # при захвате столицы прибовлять процент от мощи
    def __init__(self, x, y, parent):
        self.power = 0
        self.x = x
        self.y = y
        self.win_sqr = parent.win_sqr
        self.color = (255, 255, 255)
        self.win = parent.win

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x*self.win_sqr, self.y*self.win_sqr, self.win_sqr, self.win_sqr))


    def has_resource(self, square):
        check = False
        for obj in square:
            if type(obj) == Resource:
                check = True
            elif obj == self:
                return False
        return check

    def grow(self, map):
        steps = []
        for square in map:
            if self.has_self(square):
                for i in range(1, 5):
                    for x in range(-i, i):
                        for y in range(-i, i):
                            if self.has_resource(map[self.x+x][self.y+y]):
                                if self.x < self.x + x:
                                    steps.append({'map': map[self.x + 1][self.y], 'diff': x})
                                elif self.x > self.x + x:
                                    steps.append({'map': map[self.x - 1][self.y], 'diff': x})
                                elif self.y < self.y + y:
                                    steps.append({'map': map[self.x][self.y + 1][self.y], 'diff': y})
                                elif self.y > self.y + y:
                                    steps.append({'map': map[self.x][self.y - 1], 'diff': y})
                return sorted(steps, key=lambda k: k['diff'])


    def step(self, map, steps, power):
        for i in steps[:power]:
            i['map'].append(Empire)
            for j in steps:
                if j['map'] == i['map']:
                    steps.remove(j)
            return


class Resource:
    def __init__(self, x, y, power, parent):
        self.x = x
        self.y = y
        self.power = power
        self.win_sqr = parent.win_sqr
        self.win = parent.win

    def draw(self):
        pygame.draw.rect(self.win, (0, 255, 0), (self.x*self.win_sqr, self.y*self.win_sqr, self.win_sqr, self.win_sqr))


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
                    self.map[x][y].append(Resource(x, y, randint(1, 100), self))

    def spawn_empires(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if not self.map[x][y] and randint(1, 100) <= self.res_imp:
                    self.map[x][y].append(Empire(x, y, self))

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
            for x in range(len(self.map)):
                for y in range(len(self.map[x])):
                    for obj in self.map[x][y]:
                        obj.draw()
            pygame.display.update()
            sleep(5)


game = Game()
game.start()
pygame.quit()
