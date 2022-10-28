class Grille:
    def __init__(self, l1, l2, l3, l4):
        self.tab = [[] for i in range(4)]
        for i in l1:
            self.tab[0].append(i)
        for i in l2:
            self.tab[1].append(i)
        for i in l3:
            self.tab[2].append(i)
        for i in l4:
            self.tab[3].append(i)

    def voisins(self, x, y):
        v = {}
        if x > 0:
            v[(x - 1, y)] = self.tab[y][x-1]
            if y > 0:
                v[(x - 1, y - 1)] = self.tab[y-1][x-1]
            if y < 3:
                v[(x - 1, y + 1)] = self.tab[y+1][x-1]

        if x < 3:
            v[(x + 1, y)] = self.tab[y][x+1]
            if y > 0:
                v[(x + 1, y - 1)] = self.tab[y-1][x+1]
            if y < 3:
                v[(x + 1, y + 1)] = self.tab[y+1][x+1]

        if y > 0:
            v[(x, y - 1)] = self.tab[y-1][x]
        if y < 3:
            v[(x, y + 1)] = self.tab[y+1][x]

        return {i:v[i] for i in v if v[i]}


'''
def parcours2(grille, x, y, dico, i):
    print(dico)
    if len(dico) == 0 or i == 8:
        return dico
    else:
        vois = grille.voisins(x, y)
        dico2 = []
        for m in dico:
            if i == len(m):
                print(m)
                continue
            if m[i] in vois.values():
                dico2.append(m)
        for v in vois:
            parcours2(grille, v[0], v[1], dico2, i+1)
'''

def parcours2(grille, x, y, dico, i, p):
    p += [(x, y)]
    vois = grille.voisins(x, y)
    for v in vois:
        print(parcours2(grille, v[0], v[1], [m for m in dico if m[i] == vois[v] and v not in p], i+1, p))



def parcours(grille, x, y, dico):
    dico = [m for m in dico if m[0] == grille.tab[y][x]]
    print(dico)
    print(parcours2(grille, x, y, dico, 1, []))


