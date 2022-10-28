from fonctions import generate
import pygame as pg
from succes import Succes
import os

x = 1920-250
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen = pg.display.set_mode((50*5, 50*5), pg.NOFRAME)
end = False
background = pg.image.load("textures/background.png")
background2 = pg.image.load("textures/background2.png")
valid = []

tab = generate()
enchant = Succes("Enchanter", pg.image.load("textures/enchanted_book.png"), "Enchant an item at an Enchantment Table")
tab.append(enchant)

while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pass
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                end = True
            if event.key == pg.K_u:
                tab = generate()
                tab.append(enchant)
        if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if event.button == 1:
                    print(tab[y//50][x//50])
                if event.button == 3:
                    if (x//50, y//50) in valid:
                        valid.remove((x//50, y//50))
                    else:
                        valid.append((x//50, y//50))

    for i in range(5):
        for j in range(5):
            if (i, j) in valid:
                screen.blit(background2, (50*i, 50*j))
            else:
                screen.blit(background, (50 * i, 50 * j))
            screen.blit(tab[j][i].img, (50*i+8, 50*j+8))

    pg.display.flip()