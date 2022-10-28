from succes import Succes
import pygame as pg
logos = pg.image.load("textures/logo.png")


def clip(surface, x, y, x_size, y_size):
    handle_surface = surface.copy()
    clipRect = pg.Rect(x, y, x_size, y_size)
    handle_surface.set_clip(clipRect)
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy()

def lire(fichier):
    with open(fichier) as f:
        rows = []
        text = f.read()
        while len(text) != 0:
            a = text.find("</tr>")
            rows.append(text[:a+5])
            text = text[a+5:]

    liste = []
    for i in range(len(rows)):
        text = rows[i]
        a = text.find("</td>")
        l = text[:a+5]
        bp = l.find("background-position")
        bp2 = l.find('px">', bp)
        coord = l[bp+len("background-position:"):bp2]
        if len(coord) < 20:
            x = int(coord[1:coord.find("px")])
            y = int(coord[coord.find(" -")+2:])
            img = clip(logos, x, y, 32, 32)
        else:
            continue

        text = text[a+5:]
        a = text.find("</td>")
        l = text[:a + 5]
        s = l.find("<b>")
        e = l.find("<br>")
        nom = l[s+3:e]

        text = text[a + 5:]
        a = text.find("</td>")
        desc = text[4:a]
        for gerge in range(4):
            if "<a" in desc:
                s = desc.find("<a")
                e = desc.find(">")
                s2 = desc.find("</a>")
                desc = desc[:s] + desc[e+1:s2] + desc[s2+4:]
        liste.append(Succes(nom, img, desc))
    return liste