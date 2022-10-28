def generateur():
    grille = []
    for i in range(9):
        grille.append([])
        for j in range(9):
            grille[i].append(0)
    return grille

def clic_gauche(pos, grille):
    grille[pos[0]][pos[1]] += 1
    if grille[pos[0]][pos[1]] == 10:
        grille[pos[0]][pos[1]] = 0
    return grille

def clic_droit(pos, grille):
    grille[pos[0]][pos[1]] -= 1
    if grille[pos[0]][pos[1]] == -1:
        grille[pos[0]][pos[1]] = 9
    return grille

def style(grille):
    depart = []
    for i in range(9):
        for j in range(9):
            if grille[i][j]:
                depart.append((i, j))
    return depart

def test_cube(ligne, case, possib):
    ligne = ligne // 3
    case = case // 3
    cube = []
    for i in range(3):
        for j in range(3):
            cube.append(possib[ligne*3 + i][case * 3 + j])
    return cube

def tab_possib(grille):
    possib = []
    for i in range(9):
        possib.append([])
        for j in range(9):
            possib[i].append(grille[i][j])

    for ligne in range(9):
        for case in range(9):
            if grille[ligne][case] == 0:
                possib[ligne][case] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for val in grille[ligne]:
                    if val in possib[ligne][case] and isinstance(val, int):
                        possib[ligne][case].remove(val)
                for i in range(9):
                    val = grille[i][case]
                    if val in possib[ligne][case] and isinstance(val, int):
                        possib[ligne][case].remove(val)
                cube = test_cube(ligne, case, grille)
                for val in cube:
                    if val in possib[ligne][case] and isinstance(val, int):
                        possib[ligne][case].remove(val)
    return possib

def soluce(grille):
    possib = tab_possib(grille)
    for ligne in range(9):
        for case in range(9):
            if isinstance(possib[ligne][case], list):
                if len(possib[ligne][case]) == 1:
                    grille[ligne][case] = possib[ligne][case][0]
                    grille, possib = soluce(grille)

    for ligne in range(9):
        nbr_apparition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for case in range(9):
            if isinstance(possib[ligne][case], list):
                for i in possib[ligne][case]:
                    nbr_apparition[i-1] += 1
        for i in range(9):
            if nbr_apparition[i] == 1:
                for case in range(9):
                    if isinstance(possib[ligne][case], list):
                        if i+1 in possib[ligne][case]:
                            grille[ligne][case] = i+1
                            grille, possib = soluce(grille)

    for colonne in range(9):
        nbr_apparition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for case in range(9):
            if isinstance(possib[case][colonne], list):
                for i in possib[case][colonne]:
                    nbr_apparition[i-1] += 1
        for i in range(9):
            if nbr_apparition[i] == 1:
                for case in range(9):
                    if isinstance(possib[case][colonne], list):
                        if i+1 in possib[case][colonne]:
                            grille[case][colonne] = i+1
                            grille, possib = soluce(grille)

    for ligne in range(3):
        for colonne in range(3):
            cube = []
            for i in range(3):
                for j in range(3):
                    cube.append(possib[ligne * 3 + i][colonne * 3 + j])
            nbr_apparition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for case in range(9):
                if isinstance(cube[case], list):
                    for i in cube[case]:
                        nbr_apparition[i-1] += 1
            for i in range(9):
                if nbr_apparition[i] == 1:
                    for case in range(9):
                        if isinstance(cube[case], list):
                            if i+1 in cube[case]:
                                grille[ligne * 3 + case // 3][colonne * 3 + case % 3] = i+1
                                grille, possib = soluce(grille)
    return grille, possib
