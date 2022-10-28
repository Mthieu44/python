import pygame
import sys
from fonctions import *
pygame.init()

size = (360, 360)
screen = pygame.display.set_mode(size)
grille = generateur()


case0 = pygame.image.load("img/case0.jpg")
case1 = pygame.image.load("img/case1.jpg")
case2 = pygame.image.load("img/case2.jpg")
case3 = pygame.image.load("img/case3.jpg")
case4 = pygame.image.load("img/case4.jpg")
case5 = pygame.image.load("img/case5.jpg")
case6 = pygame.image.load("img/case6.jpg")
case7 = pygame.image.load("img/case7.jpg")
case8 = pygame.image.load("img/case8.jpg")
case9 = pygame.image.load("img/case9.jpg")
transp = pygame.image.load("img/transp.png")

grosses_lignes = [pygame.Rect(118, 0, 4, 360), pygame.Rect(238, 0, 4, 360), pygame.Rect(0, 118, 360, 4), pygame.Rect(0, 238, 360, 4)]
depart = []
print("Saisissez les chiffres (clic gauche = +1, clic droit = -1), puis appuyez sur entrĂ©e pour afficher la solution")
print("Appuyez sur R pour tout effacer")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                depart = style(grille)
                grille, possib = soluce(grille)
                for i in possib:
                    print(i)
            if event.key == pygame.K_r:
                depart = []
                grille = generateur()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                grille = clic_gauche((pos[1]//40, pos[0]//40), grille)
            if event.button == 3:
                grille = clic_droit((pos[1]//40, pos[0]//40), grille)

    for ligne in range(9):
        for case in range(9):
            if grille[ligne][case] == 0:
                screen.blit(case0, (case * 40, ligne * 40))
            if grille[ligne][case] == 1:
                screen.blit(case1, (case * 40, ligne * 40))
            if grille[ligne][case] == 2:
                screen.blit(case2, (case * 40, ligne * 40))
            if grille[ligne][case] == 3:
                screen.blit(case3, (case * 40, ligne * 40))
            if grille[ligne][case] == 4:
                screen.blit(case4, (case * 40, ligne * 40))
            if grille[ligne][case] == 5:
                screen.blit(case5, (case * 40, ligne * 40))
            if grille[ligne][case] == 6:
                screen.blit(case6, (case * 40, ligne * 40))
            if grille[ligne][case] == 7:
                screen.blit(case7, (case * 40, ligne * 40))
            if grille[ligne][case] == 8:
                screen.blit(case8, (case * 40, ligne * 40))
            if grille[ligne][case] == 9:
                screen.blit(case9, (case * 40, ligne * 40))

    if depart:
        for pos in depart:
            screen.blit(transp, (pos[1] * 40, pos[0] * 40))

    for lignes in grosses_lignes:
        pygame.draw.rect(screen, "black", lignes)

    pygame.display.flip()