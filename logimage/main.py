import random
from fonctions import *

pygame.init()
size = 500, 500
taille = 10
screen = pygame.display.set_mode(size)

grille = Grille(taille)
oui = True

while oui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oui = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                l, c = chiffres(grille)
                indice(l, c, taille)
            if event.key == pygame.K_r:
                for i in range(int(0.2*taille*taille)):
                    x = random.randrange(0, taille)
                    y = random.randrange(0, taille)
                    grille.tab[y][x].inverse_couleur()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= 500//taille
            y //= 500//taille
            grille.tab[y][x].inverse_couleur()

    for i in range(taille):
        for j in range(taille):
            pygame.draw.rect(screen, grille.tab[j][i].color, pygame.Rect(i*500/taille, j*500/taille, 500/taille, 500/taille))

    for i in range(taille):
        pygame.draw.line(screen, "#000000", (500/taille*i, 0), (500/taille*i, 500))
        pygame.draw.line(screen, "#000000", (0, 500 / taille * i), (500, 500 / taille * i))


    pygame.display.flip()


