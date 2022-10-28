import random as rd
def afficher(tab):
    for i in tab:
        print(i)

def vides(tab):
    v = []
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == 0:
                v.append((i, j))
    return v

def spawn(tab):
    val = rd.choice([2, 2, 2, 2, 4])
    y, x = rd.choice(vides(tab))
    tab[y][x] = val

def mouv(tab, dir):
    copie = [[j for j in tab[i]] for i in range(len(tab))]
    if dir == "h":
        for col in range(len(tab)):
            for row in range(1, len(tab)):
                i = row-1
                while i > -1:
                    if tab[i][col] == tab[row][col]:
                        tab[i][col] *= 2
                        tab[row][col] = 0
                        break
                    elif tab[i][col] != 0 and tab[i][col] != tab[row][col]:
                        val = tab[row][col]
                        tab[row][col] = 0
                        tab[i+1][col] = val
                        break
                    if i == 0:
                        tab[0][col] = tab[row][col]
                        tab[row][col] = 0
                    i -= 1

    elif dir == "d":
        for row in range(len(tab)):
            for col in reversed(range(len(tab)-1)):
                i = col + 1
                while i < len(tab):
                    if tab[row][i] == tab[row][col]:
                        tab[row][i] *= 2
                        tab[row][col] = 0
                        break
                    elif tab[row][i] != 0 and tab[row][i] != tab[row][col]:
                        val = tab[row][col]
                        tab[row][col] = 0
                        tab[row][i - 1] = val
                        break
                    if i == len(tab)-1:
                        tab[row][len(tab)-1] = tab[row][col]
                        tab[row][col] = 0
                    i += 1
    elif dir == "b":
        for col in range(len(tab)):
            for row in reversed(range(len(tab)-1)):
                i = row + 1
                while i < len(tab):
                    if tab[i][col] == tab[row][col]:
                        tab[i][col] *= 2
                        tab[row][col] = 0
                        break
                    elif tab[i][col] != 0 and tab[i][col] != tab[row][col]:
                        val = tab[row][col]
                        tab[row][col] = 0
                        tab[i-1][col] = val
                        break
                    if i == len(tab)-1:
                        tab[len(tab)-1][col] = tab[row][col]
                        tab[row][col] = 0
                    i += 1
    elif dir == "g":
        for row in range(len(tab)):
            for col in range(1, len(tab)):
                i = col-1
                while i > -1:
                    if tab[row][i] == tab[row][col]:
                        tab[row][i] *= 2
                        tab[row][col] = 0
                        break
                    elif tab[row][i] != 0 and tab[row][i] != tab[row][col]:
                        val = tab[row][col]
                        tab[row][col] = 0
                        tab[row][i+1] = val
                        break
                    if i == 0:
                        tab[row][0] = tab[row][col]
                        tab[row][col] = 0
                    i -= 1
    return copie == tab

def couleur(val):
    if val == 0:
        return "#CAC0B4"
    elif val == 2:
        return "#EDE4DB"
    elif val == 4:
        return "#ECE0C8"
    elif val == 8:
        return "#F2B179"
    elif val == 16:
        return "#F59563"
    elif val == 32:
        return "#F57C60"
    elif val == 64:
        return "#F57C60"
    elif val == 128:
        return "#ECCE72"
    elif val == 256:
        return "#ECCE72"
    elif val == 512:
        return "#ECC750"
    elif val == 1024:
        return "#ECC440"
    elif val == 2048:
        return "#ECC12E"
    return "red"
