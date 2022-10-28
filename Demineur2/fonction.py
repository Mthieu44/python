import random


class Grille:
    def __init__(self, taille):
        self.taille = taille
        self.safe = None
        self.tab = None
        self.retourne = [[0 for j in range(taille)] for i in range(taille)]
        self.proba = [[1 for j in range(taille)] for i in range(taille)]

    def creation(self, x, y, d):
        self.tab = [[0 for j in range(self.taille)] for i in range(self.taille)]
        self.safe = [(x, y) for x in range(self.taille) for y in range(self.taille)]

        place = [i for i in range(self.taille*self.taille)]
        place.remove(y*self.taille+x)
        for v in self.voisin(x, y):
            place.remove(v[0]*self.taille+v[1])

        place = random.sample(place, int(int(random.randrange(d-3, d+4, 1))*(self.taille*self.taille)/100))
        for mine in place:
            self.tab[mine//self.taille][mine % self.taille] = -1
            self.safe.remove((mine//self.taille, mine % self.taille))

        for i in range(len(self.tab)):
            for j in range(len(self.tab)):
                if self.tab[i][j] == 0:
                    for v in self.voisin(j, i):
                        if self.tab[v[0]][v[1]] == -1:
                            self.tab[i][j] += 1

        for i in self.tab:
            print(i)
        return len(place)

    def voisin(self, x, y):
        v = []
        if y != 0:
            if x != 0:
                v.append((y-1, x-1))
            if x != len(self.tab)-1:
                v.append((y-1, x+1))
            v.append((y-1, x))
        if y != len(self.tab)-1:
            if x != 0:
                v.append((y+1, x-1))
            if x != len(self.tab)-1:
                v.append((y+1, x+1))
            v.append((y+1, x))

        if x != 0:
            v.append((y, x - 1))
        if x != len(self.tab) - 1:
            v.append((y, x + 1))
        return v

    def clicgauche(self, x, y):
        if self.retourne[y][x] == 0:
            self.retourne[y][x] = 1
            if self.tab[y][x] == 0:
                self.vide(x, y)

    def clicdroit(self, x, y, nbrMines):
        if self.retourne[y][x] == 2:
            self.retourne[y][x] = 0
            nbrMines += 1
        elif self.retourne[y][x] == 0:
            self.retourne[y][x] = 2
            nbrMines -= 1
        return nbrMines

    def clicmolette(self, x, y):
        if self.retourne[y][x] == 1:
            voisin = self.voisin(x, y)
            n = 0
            for v in voisin:
                if self.retourne[v[0]][v[1]] == 2:
                    n += 1
            if n >= self.tab[y][x]:
                for v in voisin:
                    if self.retourne[v[0]][v[1]] == 0:
                        self.retourne[v[0]][v[1]] = 1
                        if self.tab[v[0]][v[1]] == 0:
                            self.vide(v[1], v[0])

    def vide(self, x, y):
        voisins = self.voisin(x, y)
        self.retourne[y][x] = 1
        for v in voisins:
            if self.tab[v[0]][v[1]] == 0:
                if self.retourne[v[0]][v[1]] != 1:
                    self.vide(v[1], v[0])
            else:
                self.retourne[v[0]][v[1]] = 1

    def solveur_proba(self):
        retourne = False
        for i in range(self.taille):
            for j in range(self.taille):
                if self.retourne[i][j] == 1 and self.tab[i][j] != 0:
                    vois = self.voisin(j, i)
                    n = self.tab[i][j]
                    cases = 0
                    case_vide = []
                    for v in vois:
                        if self.retourne[v[0]][v[1]] == 2 or self.proba[v[0]][v[1]] == 0:
                            n -= 1
                        elif self.retourne[v[0]][v[1]] == 0:
                            cases += 1
                            case_vide.append((v[0], v[1]))
                    if n == 0:
                        for v in case_vide:
                            self.proba[v[0]][v[1]] = None
                    if cases != 0:
                        prob = 1-(n/cases)
                        if prob == 0:
                            retourne = True
                        for v in case_vide:
                            if self.proba[v[0]][v[1]]:
                                self.proba[v[0]][v[1]] = self.proba[v[0]][v[1]] * prob
        if retourne:
            self.solveur_proba()

    def solveur_auto(self):
        self.solveur_proba()
        for i in range(self.taille):
            for j in range(self.taille):
                if self.proba[i][j] is None:
                    self.retourne[i][j] = 1
                    if self.tab[i][j] == 0:
                        self.vide(j, i)
                elif self.proba[i][j] == 0:
                    self.retourne[i][j] = 2
                else:
                    self.proba[i][j] = 1

def zoom(size, grille, i, coord):
    size[0] += 20
    size[1] += 20
    while size[0] % grille.taille != 0:
        size[0] += 1
        size[1] += 1
    centre = [coord[0], coord[1]]
    fenetre = i + i - size[0]
    print("centre=", centre)
    if centre[0] < fenetre/2:
        print(1)
        centre[0] = fenetre/2
    elif centre[0] + size[0]/2 > i:
        print(3)
        centre[0] -= size[0]/2 - i + centre[0]
    else:
        pass
    if centre[1] < fenetre/2:
        print(2)
        centre[1] = fenetre/2
    elif centre[1] + size[1]/2 > i:
        print(4)
        centre[1] -= size[1]/2 - i + centre[1]
    print(size, centre)
    return size, centre

def dezoom(size, grille, i, coord):
    size[0] -= 20
    size[1] -= 20
    while size[0] % grille.taille != 0:
        size[0] -= 1
        size[1] -= 1
    if size[0] < i:
        size = [i, i]
    print(size)
    return size, coord