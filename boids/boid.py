import pygame as pg
from math import cos, sin, pi, sqrt
import random as rd


class Boid:
    #img = pg.image.load("boid.png")

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.trail = []

    def life(self, liste):
        v1x, v1y = self.cohesion(liste)
        v2x, v2y = self.separation(liste)
        v3x, v3y = self.alignement(liste)
        self.dx += v1x + v2x + v3x #+ (rd.random()-0.5)
        self.dy += v1y + v2y + v3y #+ (rd.random()-0.5)
        if self.dx > 2 or self.dx < -2:
            self.dx = (self.dx / abs(self.dx)) * 2
        if self.dy > 2 or self.dy < -2:
            self.dy = (self.dy / abs(self.dy)) * 2

        self.x += self.dx
        self.y += self.dy
        self.proche_bord()
        self.trail.append((self.x, self.y))
        if len(self.trail) > 5:
            self.trail = self.trail[1:]

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.x, self.y), 3)
        for p in self.trail:
            pg.draw.circle(screen, "white", (p[0], p[1]), 1)
        #screen.blit(self.img, (self.x, self.y))

    def voisins(self, liste, rayon):
        l = []
        for v in liste:
            if sqrt((self.x - v.x)**2 + (self.y - v.y)**2) < rayon:
                l.append(v)
        l.remove(self)
        return l

    def cohesion(self, liste):
        voisins = self.voisins(liste, 40)
        if len(voisins) == 0:
            return 0, 0
        x, y = 0, 0
        for v in voisins:
            x += v.x
            y += v.y
        return (x/len(voisins) - self.x)/100, (y/len(voisins) - self.y)/100

    def separation(self, liste):
        voisins = self.voisins(liste, 20)
        x, y = 0, 0
        for v in voisins:
            x -= (v.x - self.x)
            y -= (v.y - self.y)
        return x/100, y/100

    def alignement(self, liste):
        voisins = self.voisins(liste, 40)
        if len(voisins) == 0:
            return 0, 0
        dx, dy = 0, 0
        for v in voisins:
            dx += v.dx
            dy += v.dy
        dx /= len(voisins)
        dy /= len(voisins)
        return (dx - self.dx)/15, (dy - self.dy)/15

    def proche_bord(self):
        if self.x < 50:
            self.dx += 0.3
        if self.x > 950:
            self.dx -= 0.3
        if self.y < 50:
            self.dy += 0.3
        if self.y > 950:
            self.dy -= 0.3
