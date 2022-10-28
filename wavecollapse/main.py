from fonctions import *
import pygame as pg
import sys

pg.init()
taille = 10
i = 1000
while i % taille != 0:
    i += 1
grille = generate(taille)

screen = pg.display.set_mode((i, i))
rect_size = i/taille

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_i:
                grille = generate(taille)

    for i in range(taille):
        for j in range(taille):
            case = grille[i][j]
            case.draw(screen, j, i, taille)

    '''
    for i in range(1, taille):
        pg.draw.line(screen, (0, 0, 0), (0, i*rect_size), (1000, i*rect_size), 1)
        pg.draw.line(screen, (0, 0, 0), (i*rect_size, 0), (i*rect_size, 1000), 1)'''

    pg.display.flip()
