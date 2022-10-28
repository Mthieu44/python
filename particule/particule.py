import pygame as pg


class Particule:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.dx = 0
        self.dy = 0

    def rect(self):
        return pg.Rect(self.x, self.y, self.size, self.size)

    def __eq__(self, other):
        if self.rect().colliderect(other.rect()):
            return True
        return False
