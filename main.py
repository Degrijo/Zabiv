from random import randint, choice


width = 1000
height = 500
sqr = 25
res_prob = 10
res_imp = 10


class Imperia: # при захвате столицы прибовлять процент от мощи
    def __init__(self, capital_coor, color):
        self.power = 0
        self.capital_coor = capital_coor
        self.color = color


map = [['-' for j in range(height//sqr)] for i in range(width//sqr)]


def spawn():
    for x in range(len(map)):
        for y in range(len(map[x])):
            if randint(1, 100) <= res_prob:
                map[x][y] = randint(1, 100)

def location(imperia):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '-':
                map[x][y] = imperia
