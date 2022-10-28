from fonctions import *
import pygame
import sys

pygame.init()
taille = int(input("taille"))
tab = [[0 for i in range(taille)] for j in range(taille)]
spawn(tab)
dir = ""
screen = pygame.display.set_mode((100*taille, 100*taille))
myfont = pygame.font.SysFont("Clear Sans", 80)
fps = pygame.time.Clock()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = "h"
            if event.key == pygame.K_LEFT:
                dir = "g"
            if event.key == pygame.K_DOWN:
                dir = "b"
            if event.key == pygame.K_RIGHT:
                dir = "d"
            if event.key == pygame.K_r:
                tab = [[0 for i in range(taille)] for j in range(taille)]
                spawn(tab)

    if dir != "":
        if not mouv(tab, dir):
            spawn(tab)
        dir = ""

    screen.fill("#BBAD9F")
    for i in range(len(tab)):
        for j in range(len(tab)):
            rect = pygame.Rect(j*100+5, i*100+5, 90, 90)
            pygame.draw.rect(screen, couleur(tab[i][j]), rect)
            if tab[i][j]:
                screen.blit(myfont.render(str(tab[i][j]), False, "white"), (j*100+55-myfont.size(str(tab[i][j]))[0]/2, i*100+55-myfont.size(str(tab[i][j]))[1]/2))


    pygame.display.flip()

