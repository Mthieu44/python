import sys
from solveur import *


h, w = 20, 20
size = (w*40, h*40)
screen = pygame.display.set_mode(size)
case0 = pygame.image.load("img/Case0.jpg")
case1 = pygame.image.load("img/Case1.jpg")
case2 = pygame.image.load("img/Case2.jpg")
case3 = pygame.image.load("img/Case3.jpg")
case4 = pygame.image.load("img/Case4.jpg")
case5 = pygame.image.load("img/Case5.jpg")
case6 = pygame.image.load("img/Case6.jpg")
case7 = pygame.image.load("img/Case7.jpg")
case8 = pygame.image.load("img/Case8.jpg")
casev = pygame.image.load("img/Case-1.jpg")
casem = pygame.image.load("img/CaseM.jpg")
cased = pygame.image.load("img/CaseD.jpg")
casel = pygame.image.load("img/CaseL.jpg")
timer = pygame.time.Clock()

n = random.randrange(int((h*w)*0.07), int((h*w)*0.2))
print(n)
tab = construction(h, w, n)
retourne = []
for i in range(h):
    retourne.append([])
    for j in range(w):
        retourne[i].append(0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                retourne = stats(tab, retourne)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                retourne = clicgauche((pos[1]//40, pos[0]//40), retourne, tab)
            elif event.button == 3:
                if retourne[pos[1]//40][pos[0]//40] != 1:
                    retourne = clicdroit((pos[1]//40, pos[0]//40), retourne)

    for ligne in range(h):
        for case in range(w):
            if retourne[ligne][case] == 0:
                screen.blit(case0, (case*40, ligne*40))
            elif retourne[ligne][case] == 2:
                screen.blit(cased, (case*40, ligne*40))
            else:
                if tab[ligne][case] == 0:
                    screen.blit(casev, (case * 40, ligne * 40))
                if tab[ligne][case] == 1:
                    screen.blit(case1, (case*40, ligne*40))
                if tab[ligne][case] == 2:
                    screen.blit(case2, (case*40, ligne*40))
                if tab[ligne][case] == 3:
                    screen.blit(case3, (case*40, ligne*40))
                if tab[ligne][case] == 4:
                    screen.blit(case4, (case*40, ligne*40))
                if tab[ligne][case] == 5:
                    screen.blit(case5, (case*40, ligne*40))
                if tab[ligne][case] == 6:
                    screen.blit(case6, (case*40, ligne*40))
                if tab[ligne][case] == 7:
                    screen.blit(case7, (case*40, ligne*40))
                if tab[ligne][case] == 8:
                    screen.blit(case8, (case*40, ligne*40))

                if tab[ligne][case] == -1:
                    while 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                        for r in range(h):
                            for c in range(w):
                                if tab[r][c] == -1:
                                    screen.blit(casem, (c * 40, r * 40))
                                screen.blit(casel, (case*40, ligne*40))
                        pygame.display.flip()

    win = [0, 0]
    for i in range(h):
        for j in range(w):
            if retourne[i][j] == 2:
                if tab[i][j] == -1:
                    win[0] += 1
                else:
                    win[1] += 1
    if win[0] == n and win[1] == 0:
        sys.exit()

    pygame.display.flip()

