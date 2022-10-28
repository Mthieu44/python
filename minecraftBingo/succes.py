class Succes:
    def __init__(self, nom, img, desc):
        self.nom = nom
        self.img = img
        self.desc = desc

    def __str__(self):
        return '\033[1m  \033[4m' + self.nom + '\033[0m\n' + self.desc

