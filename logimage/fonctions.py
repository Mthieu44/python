import pygame
import sys


class Case:
    def __init__(self):
        self.color = "#ffffff"

    def change_couleur(self, couleur):
        self.color = couleur

    def inverse_couleur(self):
        if self.color == "#ffffff":
            self.color = "#000000"
        else:
            self.color = "#ffffff"


class Grille:
    def __init__(self, taille):
        self.tab = [[Case() for _ in range(taille)] for _ in range(taille)]

    def __str__(self):
        s = ""
        for i in self.tab:
            s += str(i)
        return s

    def ligne(self, i):
        return self.tab[i]

    def colonne(self, i):
        return [self.tab[j][i] for j in range(len(self.tab))]

class Chiffre:
    def __init__(self, val, couleur):
        self.val = val
        self.color = couleur

    def __str__(self):
        return "(" + str(self.val) + " : " + self.color + ")"



def chiffres_ligne(ligne):
    chiffres = []
    couleur = "#ffffff"
    cpt = 0
    for c in ligne:
        if c.color != couleur:
            if couleur != "#ffffff":
                chiffres.append(Chiffre(cpt, couleur))
            couleur = c.color
            cpt = 1
        else:
            cpt += 1

    return chiffres


def chiffres(grille):
    l = []
    c = []
    for i in range(len(grille.tab)):
        l.append(chiffres_ligne(grille.ligne(i)))
        c.append(chiffres_ligne(grille.colonne(i)))
    return l, c


def indice(l, c, taille):
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, int(500//taille*1.7))

    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        screen.fill("#ffffff")
        for ligne in range(taille):
            nbr = 0
            for chiffre in l[ligne]:
                img = font.render(str(chiffre.val), True, "#000000")
                screen.blit(img, ((500//taille*nbr), 500+(500//taille*ligne)))
                nbr += 1

        for colonne in range(taille):
            nbr = 0
            for chiffre in c[colonne]:
                img = font.render(str(chiffre.val), True, "#000000")
                screen.blit(img, (500+(500//taille*colonne+0.2*500//taille), (500//taille*nbr)))
                nbr += 1



        for i in range(taille):
            pygame.draw.line(screen, "#000000", (500 / taille * i + 500, 0), (500 / taille * i + 500, 1000))
            pygame.draw.line(screen, "#000000", (0, 500 / taille * i + 500), (1000, 500 / taille * i + 500))

        pygame.display.flip()