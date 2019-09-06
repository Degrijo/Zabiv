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

    def grow(self, map, imperia, SweetPussy):
        p = 1
        z = 1
        for x in map:
            for y in map:
                if map[x][y] == imperia:

                    for i in range(-p, p):
                        for j in range(-z, z):
                            if map[x + i][y + j] == SweetPussy:
                                if x+i > 0:
                                    PussyCordsX = x+1
                                elif x+i < 0:
                                    PussyCordsX = x-1
                                else:
                                    PussyCordsX = x
                                if y+i > 0:
                                    PussyCordsY = y+1
                                elif y+i < 0:
                                    PussyCordsY = y-1
                                else:
                                    PussyCordsY = y
                                map[PussyCordsX][PussyCordsY] == imperia
                                return
                            else:
                                p += 1
                                z += 1
                                continue


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
