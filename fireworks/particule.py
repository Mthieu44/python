import pygame as pg
import random as rd
from color import Color


class Particule:
    def __init__(self, x, y, dx, dy, size, color=Color(0, 0, 0), lifespan=-1):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.lifespan = lifespan

    def draw(self, surface):
        pg.draw.circle(surface, self.color(), (self.x, self.y), self.size)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.001
        self.lifespan -= 1

    def is_dead(self):
        return self.x < -20 or self.x > 1020 or self.y < -20 or self.y > 1020 or self.lifespan == 0

