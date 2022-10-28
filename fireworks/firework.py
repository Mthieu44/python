from particule import Particule
import random as rd
from color import Color
from math import pi
from math import sin
from math import cos


class Firework:
    def __init__(self, fuse, color=(0, 0, 0)):
        self.particules = []
        self.fusee = None
        self.proba = 0
        self.fuse = fuse
        self.color = Color(color[0], color[1], color[2])
        if color == (0, 0, 0):
            self.color.randomize_color()

    def launch(self, x):
        p = Particule(x, 999, rd.random()*2-1, -3, 3, color=Color(100, 30, 30))
        self.particules.append(p)
        self.fusee = p

    def life(self, screen):
        for p in self.particules:
            p.move()
            p.draw(screen)
            if p.is_dead():
                self.particules.remove(p)
                if p == self.fusee:
                    self.fusee = None

        self.fuse -= 1

        if self.fusee:
            if self.fusee.y < 600:
                if rd.random() < self.proba or self.fusee.y < 100:
                    self.explose()
                self.proba += 0.0003

    def explose(self):
        for i in range(150):
            d = rd.random()*2
            p = Particule(self.fusee.x,
                          self.fusee.y,
                          cos(d*pi)*(rd.random()),
                          sin(d*pi)*(rd.random()),
                          1,
                          color=self.color.close_color(),
                          lifespan=rd.randrange(200, 400))
            self.particules.append(p)
        self.particules.remove(self.fusee)
        self.fusee = None
