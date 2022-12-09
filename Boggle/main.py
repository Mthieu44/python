from fonctions import *

taba = [
['s', 'o', 'c', 'e'],
['n', 'i', 'u', 'h'],
['a', 'e', 's', 'a'],
['g', 's', 'n', 'a']]

tab = entree()
mots = mots_dans_grille(tab)
print(len(mots))
for i in range(len(mots)//10):
       print(mots[i*10:i*10+10])
print(mots[len(mots)//10*10:])
