from bateau import Bateau
import random as rd
from coord import Coord


class Grille:
    bats = [5, 4, 4, 3, 3, 2, 2, 2]

    def __init__(self, clicable):
        self.clicable = clicable
        self.bateaux = []
        self.tirs = {}

    def placer_bateau(self, hor, coord):
        b = Bateau(self.bats[len(self.bateaux)])
        if hor == 1:
            b.placer_horizontal(coord)
        else:
            b.placer_vertical(coord)
        self.bateaux.append(b)

        if len(self.bateaux) == len(self.bats):
            self.clicable = False

    def prev(self, hor, coord):
        b = Bateau(self.bats[len(self.bateaux)])
        if hor == 1:
            liste = b.prev_horizontal(coord)
        else:
            liste = b.prev_vertical(coord)

        possib = True
        for c in liste:
            if self.clicable:
                if c.x < 0 or c.x > 9 or c.y < 0 or c.y > 9:
                    possib = False
            else:
                if c.x < 10 or c.x > 19 or c.y < 0 or c.y > 9:
                    possib = False
        for b2 in self.bateaux:
            if b2.collision(liste):
                possib = False

        return liste, possib

    def placer_bateaux_random(self):
        for t in self.bats:
            hor = rd.choice([1, -1])
            choix = []
            for x in range(10, 20):
                for y in range(10):
                    _, possib = self.prev(hor, Coord(x, y))
                    if possib:
                        choix.append(Coord(x, y))

            c = rd.choice(choix)
            self.placer_bateau(hor, c)

    def tir(self, j, coord):
        self.tirs[coord] = False
        bt = j.cherche_bateau(coord)
        if bt:
            self.tirs[coord] = True
            bt.touches.append(coord)

    def cherche_bateau(self, coord):
        for b in self.bateaux:
            if coord in b.cases:
                return b
        return None

    def perdu(self):
        for b in self.bateaux:
            if not b.is_coule():
                return False
        return len(self.bateaux) != 0
