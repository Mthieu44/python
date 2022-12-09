from de import des
from liste_mots import dico
import random as rd

def entree():
    tab = [list(input("l1: ")), list(input("l2: ")), list(input("l3: ")), list(input("l4: "))]
    return tab

def gen_rdm():
    tab = [[None for i in range(4)] for j in range(4)]
    rd.shuffle(des)
    for d in range(16):
        tab[d//4][d%4] = des[d].lancer()
    for i in tab:
        print(i)
    return tab


def cherche(tab, x, y):
    mots = [[(x, y)]]
    for i in range(7):
        for m in range(len(mots)):
            vois = voisins(mots[m][-1][0], mots[m][-1][1])
            for v in vois:
                if v not in mots[m] and len(mots[m] + [v]) == i+2:
                    mots.append(mots[m] + [v])


    mots2 = []
    for m in mots:
        if len(m) > 2:
            s = ""
            for l in m:
                s += tab[l[1]][l[0]]
            mots2.append(s)
    return mots2

def voisins(x, y):
    v = []
    for i in range(x-1 if x > 0 else 0, x+2 if x < 3 else 4):
        for j in range(y-1 if y > 0 else 0, y+2 if y < 3 else 4):
            if (i, j) != (x, y):
                v.append((i, j))
    return v


def mots_dans_grille(tab):
    mots = []
    for i in range(4):
        for j in range(4):
            liste = cherche(tab, i, j)
            for m in liste:
                if m in dico and m not in mots:
                    mots.append(m)
    return sorted(list(set(mots)))
