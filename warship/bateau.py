from coord import Coord


class Bateau:
    def __init__(self, taille):
        self.taille = taille
        self.cases = []
        self.touches = []

    def __str__(self):
        s = ""
        for c in self.cases:
            s += str(c) + " ; "
        return s

    def placer_horizontal(self, coord):
        for i in range(self.taille):
            if i % 2 == 1:
                coord = Coord(coord.x + i, coord.y)
                self.cases.append(coord)
            else:
                coord = Coord(coord.x - i, coord.y)
                self.cases.append(coord)

    def placer_vertical(self, coord):
        for i in range(self.taille):
            if i % 2 == 1:
                coord = Coord(coord.x, coord.y + i)
                self.cases.append(coord)
            else:
                coord = Coord(coord.x, coord.y - i)
                self.cases.append(coord)

    def prev_horizontal(self, coord):
        prev = []
        for i in range(self.taille):
            if i % 2 == 1:
                coord = Coord(coord.x + i, coord.y)
                prev.append(coord)
            else:
                coord = Coord(coord.x - i, coord.y)
                prev.append(coord)
        return prev

    def prev_vertical(self, coord):
        prev = []
        for i in range(self.taille):
            if i % 2 == 1:
                coord = Coord(coord.x, coord.y + i)
                prev.append(coord)
            else:
                coord = Coord(coord.x, coord.y - i)
                prev.append(coord)
        return prev

    def is_horizontal(self):
        if len(self.cases) != 0:
            if self.cases[0].y == self.cases[1].y:
                return True
            return False
        print("Le bateau n'est pas placé")
        return False

    def collision(self, liste):
        for c in self.cases:
            if c in liste:
                return True
        return False

    def is_coule(self):
        return len(self.touches) == self.taille
