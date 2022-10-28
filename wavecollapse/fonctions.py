from case import Case
from case import liste_case
import random as rd


def generate(size):
    grille = [[None for i in range(size)] for j in range(size)]
    grille[size//2][size//2] = liste_case[0]
    chemin = spiral(size)
    for pos in chemin[1:]:
        grille[pos[1]][pos[0]] = gen_case(grille, pos[0], pos[1])
    return grille


def gen_case(grille, x, y):
    l = liste_case.copy()
    lr = []
    if y == 0:
        pass
    elif grille[y-1][x] is not None:
        for c in l:
            if c.has_top_neighbour(grille[y-1][x]) is False:
                lr.append(c)

    if x == len(grille)-1:
        pass
    elif grille[y][x+1] is not None:
        for c in l:
            if c.has_right_neighbour(grille[y][x+1]) is False:
                lr.append(c)

    if y == len(grille)-1:
        pass
    elif grille[y+1][x] is not None:
        for c in l:
            if c.has_bottom_neighbour(grille[y+1][x]) is False:
                lr.append(c)

    if x == 0:
        pass
    elif grille[y][x-1] is not None:
        for c in l:
            if c.has_left_neighbour(grille[y][x-1]) is False:
                lr.append(c)

    for c in lr:
        if c in l:
            l.remove(c)

    return rd.choice(l)





def spiral(taille):
    x, y = taille//2, taille//2
    chemin = [(x, y)]
    val = 1
    while True:
        if val % 2 == 1:
            for i in range(val):
                x -= 1
                chemin.append((x, y))
            if len(chemin) >= taille**2:
                break
            for i in range(val):
                y -= 1
                chemin.append((x, y))
        else:
            for i in range(val):
                x += 1
                chemin.append((x, y))
            if len(chemin) >= taille**2:
                break
            for i in range(val):
                y += 1
                chemin.append((x, y))
        val += 1

    return chemin[:-1]

