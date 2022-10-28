import random

def construction(h, w, n):
    tab = []
    for i in range(h):
        tab.append([])
        for j in range(w):
            tab[i].append(0)

    l = []
    for i in range(len(tab) * len(tab[0])):
        l.append(i)
    place = random.sample(l, n)
    for mine in place:
        y, x = mine // len(tab[0]), mine % len(tab[0])
        tab[y][x] = -1
        if y != 0:
            if tab[y-1][x] != -1:
                tab[y-1][x] += 1
            if x != 0:
                if tab[y - 1][x-1] != -1:
                    tab[y-1][x-1] += 1
            if x != len(tab[0])-1:
                if tab[y - 1][x + 1] != -1:
                    tab[y-1][x+1] += 1

        if y != len(tab)-1:
            if tab[y + 1][x] != -1:
                tab[y+1][x] += 1
            if x != 0:
                if tab[y + 1][x-1] != -1:
                    tab[y+1][x-1] += 1
            if x != len(tab[0])-1:
                if tab[y + 1][x + 1] != -1:
                    tab[y+1][x+1] += 1

        if x != 0 and tab[y][x-1] != -1:
                tab[y][x-1] += 1
        if x != len(tab[0])-1 and tab[y][x+1] != -1:
            tab[y][x+1] += 1
    return tab


def clicgauche(pos, retourne, tab):
    y, x = pos[0], pos[1]
    if retourne[y][x] == 0:
        retourne[y][x] = 1
        if tab[y][x] == 0:
            retourne = vide(pos, tab, retourne)
    return retourne


def clicdroit(pos, retourne):
    y, x = pos[0], pos[1]
    if retourne[y][x] == 0:
        retourne[y][x] = 2
    elif retourne[y][x] == 2:
        retourne[y][x] = 0
    return retourne


def vide(pos, tab, retourne):
    y, x = pos[0], pos[1]
    if y != 0:
        if retourne[y-1][x] == 0:
            retourne[y - 1][x] = 1
            if tab[y-1][x] == 0:
                vide((y-1, x), tab, retourne)
        voisingauche(y-1,x,tab,retourne)
        voisindroite(y-1,x,tab,retourne)

    if y != len(tab)-1:
        if retourne[y+1][x] == 0:
            retourne[y+1][x] = 1
            if tab[y+1][x] == 0:
                vide((y+1, x), tab, retourne)
        voisingauche(y+1, x, tab, retourne)
        voisindroite(y+1, x, tab, retourne)

    voisingauche(y, x, tab, retourne)
    voisindroite(y, x, tab, retourne)

    return retourne

def voisingauche(y, x, tab, retourne):
    if x != 0:
        if retourne[y][x-1] == 0:
            retourne[y][x-1] = 1
            if tab[y][x-1] == 0:
                vide((y, x-1), tab, retourne)


def voisindroite(y, x, tab, retourne):
    if x != len(tab[0])-1:
        if retourne[y][x+1] == 0:
            retourne[y][x+1] = 1
            if tab[y][x+1] == 0:
                vide((y, x+1), tab, retourne)