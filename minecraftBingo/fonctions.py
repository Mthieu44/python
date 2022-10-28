import random as rd
from scap import lire

def generate():
    liste = lire("table1.txt")
    liste += lire("table2.txt")
    liste += lire("table3.txt")
    liste += lire("table4.txt")
    liste += lire("table5.txt")
    ac = rd.sample(liste, k=25)
    tab = [[ac[i+j*5] for i in range(5)] for j in range(5)]
    return tab
