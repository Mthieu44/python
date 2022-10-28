import random
from fonction import *
import sys
import random as rd
from particule import *

pg.init()
size = (500, 500)
screen = pg.display.set_mode(size)

grille = Grille(size)
fps = pg.time.Clock()


def dessiner(p):
    r = pg.Rect(p.x, p.y, p.size, p.size)
    pg.draw.rect(screen, p.color, r)

def rdm_couleur():
    s = "#"
    for i in range(6):
        s += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])
    return s





while 1:
    fps.tick(60)
    bouge = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_k:
                for i in range(10):
                    grille.tab.append(Particule(rd.random()*screen.get_width(), rd.random()*screen.get_height(), rd.randrange(10, 20), rdm_couleur()))
            if event.key == pg.K_l:
                if len(grille.tab) > 0:
                    for i in range(len(grille.tab)//10+1):
                        del grille.tab[rd.randrange(0, len(grille.tab))]
            if event.key == pg.K_m:
                bouge = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            grille.tab.append(Particule(x, y, rd.randrange(10, 20), rdm_couleur()))

    x, y = pg.mouse.get_pos()
    screen.fill("#000000")

    for i, p in enumerate(grille.tab):
        if (p.x < x < p.x + p.size and p.y < y < p.y + p.size) or bouge:
            p.dx = rd.random() * 40 - 20
            p.dy = rd.random() * 40 - 20

        dessiner(p)

        if p.x + p.dx < 0:
            p.x = 0
            p.dx *= -0.6
        if p.y + p.dy < 0:
            p.y = 0
            p.dy *= -0.6
        if p.x + p.dx > screen.get_width()-p.size:
            p.x = screen.get_width()-p.size
            p.dx *= -0.6
        if p.y + p.dy > screen.get_height()-p.size:
            p.y = screen.get_height()-p.size
            p.dy *= -0.6
        p.x += p.dx
        p.y += p.dy

        p.dx *= 0.87
        p.dy *= 0.87


    pg.display.flip()

