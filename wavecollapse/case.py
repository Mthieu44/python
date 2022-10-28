import pygame as pg


class Case:
    def __init__(self, sides, img):
        self.top_left = sides[0]
        self.top_right = sides[1]
        self.right_top = sides[2]
        self.right_bottom = sides[3]
        self.bottom_right = sides[4]
        self.bottom_left = sides[5]
        self.left_bottom = sides[6]
        self.left_top = sides[7]
        self.image = img

    def has_top_neighbour(self, other):
        #if other is Case:
        if self.top_left == other.bottom_left and self.top_right == other.bottom_right:
            return True
        return False

    def has_right_neighbour(self, other):
        #if other is Case:
        if self.right_top == other.left_top and self.right_bottom == other.left_bottom:
            return True
        return False

    def has_bottom_neighbour(self, other):
        #if other is Case:
        if self.bottom_left == other.top_left and self.bottom_right == other.top_right:
            return True
        return False

    def has_left_neighbour(self, other):
        #if other is Case:
        if self.left_top == other.right_top and self.left_bottom == other.right_bottom:
            return True
        return False

    def draw(self, screen, x, y, taille):
        image = pg.transform.scale(self.image, (screen.get_size()[0] / taille, screen.get_size()[0] / taille))
        screen.blit(image, (x*screen.get_size()[0]/taille, y*screen.get_size()[0]/taille))

    def __str__(self):
        l0 = str(self.top_left) + str(self.top_right) + str(self.right_top) + str(self.right_bottom) + str(self.bottom_right) + str(self.bottom_left) + str(self.left_bottom) + str(self.left_top)
        l1 = "\n " + str(self.top_left) + str(self.top_right) + " \n"
        l2 = str(self.left_top) + "  " + str(self.right_top) + "\n"
        l3 = str(self.left_bottom) + "  " + str(self.right_bottom) + "\n"
        l4 = " " + str(self.bottom_left) + str(self.bottom_right) + " "
        return l0+l1+l2+l3+l4


case01_1 = Case((1, 1, 1, 1, 1, 1, 1, 1), pg.image.load("textures/case01_1.png"))
case01_2 = Case((1, 1, 1, 1, 1, 1, 1, 1), pg.image.load("textures/case01_2.png"))
case02_1 = Case((0, 0, 0, 0, 0, 0, 0, 0), pg.image.load("textures/case02_1.png"))
case02_2 = Case((0, 0, 0, 0, 0, 0, 0, 0), pg.image.load("textures/case02_1.png"))

case03_1 = Case((1, 0, 0, 0, 0, 0, 1, 1), pg.image.load("textures/case03_1.png"))
case03_2 = Case((1, 1, 1, 0, 0, 0, 0, 0), pg.image.load("textures/case03_2.png"))
case03_3 = Case((0, 0, 1, 1, 1, 0, 0, 0), pg.image.load("textures/case03_3.png"))
case03_4 = Case((0, 0, 0, 0, 1, 1, 1, 0), pg.image.load("textures/case03_4.png"))
case03_5 = Case((0, 0, 0, 1, 1, 1, 0, 0), pg.image.load("textures/case03_5.png"))
case03_6 = Case((0, 1, 1, 1, 0, 0, 0, 0), pg.image.load("textures/case03_6.png"))
case03_7 = Case((1, 1, 0, 0, 0, 0, 0, 1), pg.image.load("textures/case03_7.png"))
case03_8 = Case((0, 0, 0, 0, 0, 1, 1, 1), pg.image.load("textures/case03_8.png"))

case04_1 = Case((1, 0, 0, 0, 0, 0, 0, 1), pg.image.load("textures/case04_1.png"))
case04_2 = Case((0, 1, 1, 0, 0, 0, 0, 0), pg.image.load("textures/case04_2.png"))
case04_3 = Case((0, 0, 0, 1, 1, 0, 0, 0), pg.image.load("textures/case04_3.png"))
case04_4 = Case((0, 0, 0, 0, 0, 1, 1, 0), pg.image.load("textures/case04_4.png"))

case05_1 = Case((1, 1, 1, 1, 0, 0, 1, 1), pg.image.load("textures/case05_1.png"))
case05_2 = Case((1, 1, 1, 1, 1, 1, 0, 0), pg.image.load("textures/case05_2.png"))
case05_3 = Case((0, 0, 1, 1, 1, 1, 1, 1), pg.image.load("textures/case05_3.png"))
case05_4 = Case((1, 1, 0, 0, 1, 1, 1, 1), pg.image.load("textures/case05_4.png"))

case06_1 = Case((0, 0, 0, 0, 0, 0, 1, 1), pg.image.load("textures/case06_1.png"))
case06_2 = Case((1, 1, 0, 0, 0, 0, 0, 0), pg.image.load("textures/case06_2.png"))
case06_3 = Case((0, 0, 1, 1, 0, 0, 0, 0), pg.image.load("textures/case06_3.png"))
case06_4 = Case((0, 0, 0, 0, 1, 1, 0, 0), pg.image.load("textures/case06_4.png"))

case07_1 = Case((1, 1, 0, 1, 1, 0, 0, 1), pg.image.load("textures/case07_1.png"))
case07_2 = Case((0, 1, 1, 1, 0, 1, 1, 0), pg.image.load("textures/case07_2.png"))
case07_3 = Case((1, 0, 0, 1, 1, 1, 0, 1), pg.image.load("textures/case07_3.png"))
case07_4 = Case((0, 1, 1, 0, 0, 1, 1, 1), pg.image.load("textures/case07_4.png"))
case07_5 = Case((1, 0, 0, 1, 1, 0, 1, 1), pg.image.load("textures/case07_5.png"))
case07_6 = Case((0, 1, 1, 0, 1, 1, 1, 0), pg.image.load("textures/case07_6.png"))
case07_7 = Case((1, 0, 1, 1, 1, 0, 0, 1), pg.image.load("textures/case07_7.png"))
case07_8 = Case((1, 1, 1, 0, 0, 1, 1, 0), pg.image.load("textures/case07_8.png"))

case08_1 = Case((1, 1, 0, 0, 0, 1, 1, 1), pg.image.load("textures/case08_1.png"))
case08_2 = Case((1, 1, 1, 1, 0, 0, 0, 1), pg.image.load("textures/case08_2.png"))
case08_3 = Case((0, 1, 1, 1, 1, 1, 0, 0), pg.image.load("textures/case08_3.png"))
case08_4 = Case((0, 0, 0, 1, 1, 1, 1, 1), pg.image.load("textures/case08_4.png"))
case08_5 = Case((1, 1, 1, 1, 1, 0, 0, 0), pg.image.load("textures/case08_5.png"))
case08_6 = Case((1, 1, 1, 0, 0, 0, 1, 1), pg.image.load("textures/case08_6.png"))
case08_7 = Case((1, 0, 0, 0, 1, 1, 1, 1), pg.image.load("textures/case08_7.png"))
case08_8 = Case((0, 0, 1, 1, 1, 1, 1, 0), pg.image.load("textures/case08_8.png"))

case09_1 = Case((1, 1, 1, 1, 0, 1, 1, 1), pg.image.load("textures/case09_1.png"))
case09_2 = Case((1, 1, 1, 1, 1, 1, 0, 1), pg.image.load("textures/case09_2.png"))
case09_3 = Case((0, 1, 1, 1, 1, 1, 1, 1), pg.image.load("textures/case09_3.png"))
case09_4 = Case((1, 1, 0, 1, 1, 1, 1, 1), pg.image.load("textures/case09_4.png"))
case09_5 = Case((1, 1, 1, 1, 1, 0, 1, 1), pg.image.load("textures/case09_5.png"))
case09_6 = Case((1, 1, 1, 0, 1, 1, 1, 1), pg.image.load("textures/case09_6.png"))
case09_7 = Case((1, 0, 1, 1, 1, 1, 1, 1), pg.image.load("textures/case09_7.png"))
case09_8 = Case((1, 1, 1, 1, 1, 1, 1, 0), pg.image.load("textures/case09_8.png"))

case10_1 = Case((1, 1, 0, 0, 1, 1, 0, 0), pg.image.load("textures/case10_1.png"))
case10_2 = Case((0, 0, 1, 1, 0, 0, 1, 1), pg.image.load("textures/case10_2.png"))
case10_3 = Case((1, 1, 0, 0, 1, 1, 0, 0), pg.image.load("textures/case10_3.png"))
case10_4 = Case((0, 0, 1, 1, 0, 0, 1, 1), pg.image.load("textures/case10_4.png"))

case11_1 = Case((1, 1, 0, 0, 0, 0, 1, 1), pg.image.load("textures/case11_1.png"))
case11_2 = Case((1, 1, 1, 1, 0, 0, 0, 0), pg.image.load("textures/case11_2.png"))
case11_3 = Case((0, 0, 1, 1, 1, 1, 0, 0), pg.image.load("textures/case11_3.png"))
case11_4 = Case((0, 0, 0, 0, 1, 1, 1, 1), pg.image.load("textures/case11_4.png"))

case12_1 = Case((1, 1, 1, 0, 0, 1, 1, 1), pg.image.load("textures/case12_1.png"))
case12_2 = Case((1, 1, 1, 1, 1, 0, 0, 1), pg.image.load("textures/case12_2.png"))
case12_3 = Case((0, 1, 1, 1, 1, 1, 1, 0), pg.image.load("textures/case12_3.png"))
case12_4 = Case((1, 0, 0, 1, 1, 1, 1, 1), pg.image.load("textures/case12_4.png"))

case13_1 = Case((1, 0, 0, 0, 0, 0, 0, 0), pg.image.load("textures/case13_1.png"))
case13_2 = Case((0, 0, 1, 0, 0, 0, 0, 0), pg.image.load("textures/case13_2.png"))
case13_3 = Case((0, 0, 0, 0, 1, 0, 0, 0), pg.image.load("textures/case13_3.png"))
case13_4 = Case((0, 0, 0, 0, 0, 0, 1, 0), pg.image.load("textures/case13_4.png"))
case13_5 = Case((0, 1, 0, 0, 0, 0, 0, 0), pg.image.load("textures/case13_5.png"))
case13_6 = Case((0, 0, 0, 1, 0, 0, 0, 0), pg.image.load("textures/case13_6.png"))
case13_7 = Case((0, 0, 0, 0, 0, 1, 0, 0), pg.image.load("textures/case13_7.png"))
case13_8 = Case((0, 0, 0, 0, 0, 0, 0, 1), pg.image.load("textures/case13_8.png"))

case14_1 = Case((1, 0, 1, 0, 0, 0, 0, 0), pg.image.load("textures/case14_1.png"))
case14_2 = Case((0, 0, 1, 0, 1, 0, 0, 0), pg.image.load("textures/case14_2.png"))
case14_3 = Case((0, 0, 0, 0, 1, 0, 1, 0), pg.image.load("textures/case14_3.png"))
case14_4 = Case((1, 0, 0, 0, 0, 0, 1, 0), pg.image.load("textures/case14_4.png"))
case14_5 = Case((0, 0, 0, 1, 0, 1, 0, 0), pg.image.load("textures/case14_5.png"))
case14_6 = Case((0, 0, 0, 0, 0, 1, 0, 1), pg.image.load("textures/case14_6.png"))
case14_7 = Case((0, 1, 0, 0, 0, 0, 0, 1), pg.image.load("textures/case14_7.png"))
case14_8 = Case((0, 1, 0, 1, 0, 0, 0, 0), pg.image.load("textures/case14_8.png"))

liste_case = [case01_1, case01_2, case02_1, case02_2,
              case03_1, case03_2, case03_3, case03_4,
              case03_5, case03_6, case03_7, case03_8,
              case04_1, case04_2, case04_3, case04_4,
              case05_1, case05_2, case05_3, case05_4,
              case06_1, case06_2, case06_3, case06_4,
              case07_1, case07_2, case07_3, case07_4,
              case07_5, case07_6, case07_7, case07_8,
              case08_1, case08_2, case08_3, case08_4,
              case08_5, case08_6, case08_7, case08_8,
              case09_1, case09_2, case09_3, case09_4,
              case09_5, case09_6, case09_7, case09_8,
              case10_1, case10_2, case10_3, case10_4,
              case11_1, case11_2, case11_3, case11_4,
              case12_1, case12_2, case12_3, case12_4,
              case13_1, case13_2, case13_3, case13_4,
              case13_5, case13_6, case13_7, case13_8,
              case14_1, case14_2, case14_3, case14_4,
              case14_5, case14_6, case14_7, case14_8
              ]
