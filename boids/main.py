import pygame as pg
import random as rd
import sys
from boid import Boid
from math import pi

pg.init()
size = 1000, 1000
screen = pg.display.set_mode(size)
boids = [Boid(rd.randrange(100, 900), rd.randrange(100, 900), (rd.random()-0.5)/2, (rd.random()-0.5)/2) for _ in range(100)]


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                boids += [Boid(rd.randrange(100, 900), rd.randrange(100, 900), (rd.random()-0.5)/3, (rd.random()-0.5)/3) for _ in range(20)]

    screen.fill("#1A1A1A")
    for b in boids:
        b.life(boids)
        b.draw(screen)
    pg.display.flip()
