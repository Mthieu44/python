import pygame
from mecanique import *

def stats(tab, retourne):
    h = len(tab)
    w = len(tab[0])
    tab_stat = []
    for i in range(h):
        tab_stat.append([])
        for j in range(w):
            tab_stat[i].append(1)
    for ligne in range(h):
        for case in range(w):
            x = tab[ligne][case]
            if retourne[ligne][case] == 1 and x > 0:
                voisin = voisins(retourne, ligne, case)
                x = x - voisin.count(2)
                if x>0:
                    proba = 1 - (x/voisin.count(0))
                    if voisin[0] == 0:
                        tab_stat[ligne-1][case-1] = tab_stat[ligne-1][case-1] * proba
                    if voisin[1] == 0:
                        tab_stat[ligne-1][case] = tab_stat[ligne-1][case] * proba
                    if voisin[2] == 0:
                        tab_stat[ligne-1][case+1] = tab_stat[ligne-1][case+1] * proba
                    if voisin[3] == 0:
                        tab_stat[ligne][case-1] = tab_stat[ligne][case-1] * proba
                    if voisin[4] == 0:
                        tab_stat[ligne][case+1] = tab_stat[ligne][case+1] * proba
                    if voisin[5] == 0:
                        tab_stat[ligne+1][case-1] = tab_stat[ligne+1][case-1] * proba
                    if voisin[6] == 0:
                        tab_stat[ligne+1][case] = tab_stat[ligne+1][case] * proba
                    if voisin[7] == 0:
                        tab_stat[ligne+1][case+1] = tab_stat[ligne+1][case+1] * proba
                elif x == 0:
                    if voisin[0] == 0:
                        retourne[ligne-1][case-1] = 1
                        if tab[ligne-1][case-1] == 0:
                            retourne = vide((ligne-1, case-1), tab, retourne)
                    if voisin[1] == 0:
                        retourne[ligne-1][case] = 1
                        if tab[ligne-1][case] == 0:
                            retourne = vide((ligne-1, case), tab, retourne)
                    if voisin[2] == 0:
                        retourne[ligne-1][case+1] = 1
                        if tab[ligne-1][case+1] == 0:
                            retourne = vide((ligne-1, case+1), tab, retourne)
                    if voisin[3] == 0:
                        retourne[ligne][case-1] = 1
                        if tab[ligne][case-1] == 0:
                            retourne = vide((ligne, case-1), tab, retourne)
                    if voisin[4] == 0:
                        retourne[ligne][case+1] = 1
                        if tab[ligne][case+1] == 0:
                            retourne = vide((ligne, case+1), tab, retourne)
                    if voisin[5] == 0:
                        retourne[ligne+1][case-1] = 1
                        if tab[ligne+1][case-1] == 0:
                            retourne = vide((ligne+1, case-1), tab, retourne)
                    if voisin[6] == 0:
                        retourne[ligne+1][case] = 1
                        if tab[ligne+1][case] == 0:
                            retourne = vide((ligne+1, case), tab, retourne)
                    if voisin[7] == 0:
                        retourne[ligne+1][case+1] = 1
                        if tab[ligne+1][case+1] == 0:
                            retourne = vide((ligne+1, case+1), tab, retourne)
                else:
                    print("erreur en", ligne, case)
            pygame.display.flip()
    nbr = 0
    min = 0.01
    while nbr == 0 and min < 0.2:
        for ligne in range(h):
            for case in range(w):
                if tab_stat[ligne][case] < min:
                    retourne[ligne][case] = 2
                    nbr += 1
                    tab_stat[ligne][case] = 1
        min += 0.01

    return retourne


def voisins(retourne, ligne, case):
    voisin = []
    if ligne != 0:
        if case !=0:
            voisin.append(retourne[ligne-1][case-1])
        else:
            voisin.append(1)
        voisin.append(retourne[ligne-1][case])
        if case != len(retourne[0])-1:
            voisin.append(retourne[ligne-1][case+1])
        else:
            voisin.append(1)
    else:
        voisin.append(1)
        voisin.append(1)
        voisin.append(1)

    if case != 0:
        voisin.append(retourne[ligne][case-1])
    else:
        voisin.append(1)

    if case != len(retourne[0])-1:
        voisin.append(retourne[ligne][case+1])
    else:
        voisin.append(1)

    if ligne != len(retourne)-1:
        if case !=0:
            voisin.append(retourne[ligne+1][case-1])
        else:
            voisin.append(1)
        voisin.append(retourne[ligne+1][case])
        if case != len(retourne[0])-1:
            voisin.append(retourne[ligne+1][case+1])
        else:
            voisin.append(1)
    else:
        voisin.append(1)
        voisin.append(1)
        voisin.append(1)

    return voisin


