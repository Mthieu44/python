from fonctions import *

dico = [""]
l1 = "abcd"
l2 = "efgh"
l3 = "ijkl"
l4 = "mnop"
g = Grille(l1, l2, l3, l4)

p = parcours(g, 0, 0, ["djfghjyf", "aioge", "abc", "aejk", "afghl", "nokgh"])
print(p)
