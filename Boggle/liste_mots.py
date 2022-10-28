import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    only_ascii = only_ascii.decode("utf-8")
    return only_ascii

def lire(file):
    ALPHA = [chr(c) for c in range(65, 91)]
    with open(file) as liste:
        l = ['a']
        for mot in liste:
            if '-' not in mot and mot[0] not in ALPHA and ' ' not in mot and 2 < len(mot) < 10:
                mot = remove_accents(mot).rstrip()
                if mot != l[-1]:
                    l.append(mot)
    return l[1:]


dico = lire("liste_francais.txt")
