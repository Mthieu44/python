from grille import Grille
from coord import Coord
import pygame as pg
import sys
import random as rd


pg.init()
size = (1000, 500)
screen = pg.display.set_mode(size)
hor = True
possib = False
j1 = Grille(True)
j2 = Grille(False)
j2.placer_bateaux_random()
joue = True
print("Appuyez sur r pour tourner le bateau")

while 1:
    if j1.perdu():
        print("victoire de j2")
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
    if j2.perdu():
        print("victoire de j1")
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                hor = -hor

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pg.mouse.get_pos()
                x = x//50
                y = y//50
                if j1.clicable:
                    if x < 10:
                        if possib:
                            j1.placer_bateau(hor, Coord(x, y))
                else:
                    if joue:
                        c = Coord(x, y)
                        if x > 9 and c not in j1.tirs.keys():
                            j1.tir(j2, c)
                            if not j1.tirs[c]:
                                joue = False
                    while not joue:
                        c = Coord(rd.randrange(0, 10), rd.randrange(0, 10))
                        if c not in j2.tirs:
                            j2.tir(j1, c)
                            if not j2.tirs[c]:
                                joue = True

    fond1 = pg.Rect(0, 0, 500, 500)
    pg.draw.rect(screen, "#0055DD", fond1)

    fond2 = pg.Rect(500, 0, 500, 500)
    pg.draw.rect(screen, "#a1a1a1", fond2)

    # AFFICHAGE PREVIEW
    if j1.clicable:
        x, y = pg.mouse.get_pos()
        liste_coord_prev, possib = j1.prev(hor, Coord(x//50, y//50))
        for c in liste_coord_prev:
            r = pg.Rect(50 * c.x, 50 * c.y, 50, 50)
            col = "#66eeaa"
            if not possib:
                col = "#ee6644"
            pg.draw.rect(screen, col, r)

    # AFFICHAGE BATEAUX JOUEUR 1

    for b in j1.bateaux:
        if len(b.cases) == 1:
            c = b.cases[0]
            r = pg.Rect(50 * c.x, 50 * c.y, 50, 50)
            pg.draw.rect(screen, "#66ee66", r)
            pg.draw.line(screen, "black", (50*c.x, 50*c.y), (50*c.x+50, 50*c.y), 3)
            pg.draw.line(screen, "black", (50*c.x, 50*c.y+50), (50*c.x+50, 50*c.y+50), 3)
            pg.draw.line(screen, "black", (50 * c.x, 50 * c.y), (50 * c.x, 50 * c.y + 50), 3)
            pg.draw.line(screen, "black", (50 * c.x + 50, 50 * c.y), (50 * c.x + 50, 50 * c.y + 50), 3)

        else:
            for c in b.cases:
                r = pg.Rect(50*c.x, 50*c.y, 50, 50)
                pg.draw.rect(screen, "#66ee66", r)
                if b.is_horizontal():
                    pg.draw.line(screen, "black", (50*c.x, 50*c.y), (50*c.x+50, 50*c.y), 3)
                    pg.draw.line(screen, "black", (50*c.x, 50*c.y+50), (50*c.x+50, 50*c.y+50), 3)
                else:
                    pg.draw.line(screen, "black", (50*c.x, 50*c.y), (50*c.x, 50*c.y+50), 3)
                    pg.draw.line(screen, "black", (50*c.x+50, 50*c.y), (50*c.x+50, 50*c.y+50), 3)

            if len(b.cases) % 2 == 0:
                if b.is_horizontal():
                    pg.draw.line(screen, "black", (50*b.cases[-2].x, 50*b.cases[-2].y), (50*b.cases[-2].x, 50*b.cases[-2].y+50), 3)
                    pg.draw.line(screen, "black", (50*b.cases[-1].x+50, 50*b.cases[-1].y), (50*b.cases[-1].x+50, 50*b.cases[-1].y+50), 3)
                else:
                    pg.draw.line(screen, "black", (50*b.cases[-2].x, 50*b.cases[-2].y), (50*b.cases[-2].x+50, 50*b.cases[-2].y), 3)
                    pg.draw.line(screen, "black", (50*b.cases[-1].x, 50*b.cases[-1].y+50), (50*b.cases[-1].x+50, 50*b.cases[-1].y+50), 3)
            else:
                if b.is_horizontal():
                    pg.draw.line(screen, "black", (50*b.cases[-1].x, 50*b.cases[-1].y), (50*b.cases[-1].x, 50*b.cases[-1].y+50), 3)
                    pg.draw.line(screen, "black", (50*b.cases[-2].x+50, 50*b.cases[-2].y), (50*b.cases[-2].x+50, 50*b.cases[-2].y+50), 3)
                else:
                    pg.draw.line(screen, "black", (50*b.cases[-1].x, 50*b.cases[-1].y), (50*b.cases[-1].x+50, 50*b.cases[-1].y), 3)
                    pg.draw.line(screen, "black", (50*b.cases[-2].x, 50*b.cases[-2].y+50), (50*b.cases[-2].x+50, 50*b.cases[-2].y+50), 3)

    # AFFICHAGE TIRS
    for t in j1.tirs:
        col = "#0055DD"
        b = j2.cherche_bateau(t)
        if b:
            col = "#ee6644"
            if b.is_coule():
                col = "#cc4422"
        r = pg.Rect(50 * t.x, 50 * t.y, 50, 50)
        pg.draw.rect(screen, col, r)

    for t in j2.tirs:
        pg.draw.circle(screen, "black", (50*t.x+25, 50*t.y+25), 7, 20)

    # AFFICHAGE LIGNES
    for i in range(1, 20):
        pg.draw.line(screen, "black", (i*50-1, 0), (i*50-1, 500), 1)
    pg.draw.line(screen, "black", (500, 0), (500, 500), 5)
    for i in range(1, 10):
        pg.draw.line(screen, "black", (0, i*50), (1000, i*50), 1)



    pg.display.flip()
