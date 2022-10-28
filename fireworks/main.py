from firework import Firework
import pygame as pg
import sys
import random as rd


size = (1000, 1000)
screen = pg.display.set_mode(size)
fireworks = []
fps = pg.time.Clock()
tick = 200

while 1:
    fps.tick(tick)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_y:
                for i in range(20):
                    f = Firework(i*200)
                    fireworks.append(f)
            if event.key == pg.K_t:
                f = Firework(0)
                fireworks.append(f)
            if event.key == pg.K_r:
                particules = []
            if event.key == pg.K_p:
                tick += 5
            if event.key == pg.K_m:
                tick -= 5

    screen.fill("#1A1A1A")
    for f in fireworks:
        if f.fuse == 0:
            f.launch(rd.random()*1000)
        f.life(screen)

    pg.display.flip()

