import random as rd


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b
        if (r, g, b) == (0, 0, 0):
            self.randomize_color()

    def randomize_color(self):
        self.r = rd.randrange(100, 255)
        self.g = rd.randrange(100, 255)
        self.b = rd.randrange(100, 255)

    def __call__(self, *args, **kwargs):
        return self.r, self.g, self.b

    def close_color(self):
        r = self.r + rd.randrange(-50, 50)
        g = self.g + rd.randrange(-50, 50)
        b = self.b + rd.randrange(-50, 50)
        r = 255 if r > 255 else r
        r = 0 if r < 0 else r
        g = 255 if g > 255 else g
        g = 0 if g < 0 else g
        b = 255 if b > 255 else b
        b = 0 if b < 0 else b
        return Color(r, g, b)

    def __str__(self):
        return str(self.r) + "," + str(self.g) + "," + str(self.b)
