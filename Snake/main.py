import pygame
import sys
from fonctions import *

size = 1000, 1000
screen = pygame.display.set_mode(size)
serpent = Serpent()
pomme = Pomme()
pomme.spawn(serpent)
dir_list = serpent.track2(pomme.pos)
fps = pygame.time.Clock()
r, g, b = 255, 255, 255

while 1:
    fps.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if serpent.dir != 2:
                    serpent.dir = 0
            if event.key == pygame.K_LEFT:
                if serpent.dir != 3:
                    serpent.dir = 1
            if event.key == pygame.K_DOWN:
                if serpent.dir != 0:
                    serpent.dir = 2
            if event.key == pygame.K_RIGHT:
                if serpent.dir != 1:
                    serpent.dir = 3
            if event.key == pygame.K_p:
                pause = 1
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                pause = 0


    screen.fill("black")

    dir_list = serpent.track2(pomme.pos)

    if dir_list:
        serpent.dir = dir_list[0]
        del dir_list[0]

    if serpent.testcolli(serpent.dir):
        if serpent.testcolli((serpent.dir + 1) % 4):
            serpent.dir = (serpent.dir - 1) % 4
        elif serpent.testcolli((serpent.dir - 1) % 4):
            serpent.dir = (serpent.dir + 1) % 4
        else:
            serpent.dir = random.choice([(serpent.dir - 1) % 4, (serpent.dir + 1) % 4])

    serpent.queue()
    serpent.avance()
    if serpent.collision():
        print(serpent.long-5)
        serpent = Serpent()
        pomme.spawn(serpent)
        dir_list = serpent.track2(pomme.pos)

    if serpent.tete == pomme.pos:
        serpent.long += 1
        pomme.spawn(serpent)

    pygame.draw.rect(screen, "red", pygame.Rect(pomme.pos[0]*20, pomme.pos[1]*20, 20, 20))


    if r == 255:
        if b != 0:
            b -= 15
        elif g != 255:
            g += 15
    if g == 255:
        if r != 0:
            r -= 15
        elif b != 255:
            b += 15
    if b == 255:
        if g != 0:
            g -= 15
        elif r != 255:
            r += 15


    pygame.draw.rect(screen, (r, g, b), pygame.Rect(serpent.tete[0] * 20, serpent.tete[1] * 20, 20, 20))
    for rect in serpent.corps:
        pygame.draw.rect(screen, (r, g, b), pygame.Rect(rect[0]*20, rect[1]*20, 20, 20))
    pygame.display.flip()
