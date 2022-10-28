import random
import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1,1))
list_3 = ["Slingshot","Sharpshooter's Oath","Raven Bow","Emerald Orb","Thrilling Tales Of Dragon Slayers","Magic Guide",
          "Black Tassel","Debate Club","Bloodtainted Greatsword","Ferrous Shadow","Skyrider Sword","Harbinger Of Dawn",
          "Cool Steel"]
list_4 = [["Xinyan","Sucrose","Diona","Chongyun","Noelle","Bennett","Fischl","Ningguang","Xingqiu","Beidou","Xiangling",
          "Amber","Razor","Kaeya","Barbara","Lisa"],["Rust","Sacrificial Bow","The Stringless","Favonius Warbow",
          "Eye Of Perception","Sacrificial Fragments","The Widsith","Favonius Codex","Favonius Lance","Dragon's Bane",
          "Rainslasher","Sacrificial Greatsword","The Bell","Favonius Greatsword","Lions Roar","Sacrificial Sword",
          "The Flute","Favonius Sword"]]
list_5 = [["Qiqi", "Mona", "Keqing", "Diluc", "Jean"],["Amos Bow","Skyward Harp","Lost Prayer To The Sacred Winds",
          "Skyward Atlas","Primordial Jade Winged-Spear","Skyward Spine","Wolf's Gravestone",
          "Skyward Pride","Skyward Blade","Aquila Favonia"]]


def pull(pity_5, pity_4):
    rate5 = 0.6
    rate4 = 5.1
    if pity_4 == 8 or pity_4 == 9:
        rate4 = 50
    if pity_4 == 10:
        rate4 = 100
        rate5 = 0
    if pity_5 == 90:
        rate5 = 100
    if pity_5 > 75:
        rate5 = 40
    r = random.random()*100
    if r < rate5:
        if random.random() > 0.5:
            a = '\033[33m' + random.choice(list_5[0]) + '\033[0m'
            return a, 5
        else:
            a = '\033[33m' + random.choice(list_5[1]) + '\033[0m'
            return a, 5
    elif r < rate5+rate4:
        if random.random() > 0.5:
            a = '\033[95m' + random.choice(list_4[0]) + '\033[0m'
            return a, 4
        else:
            a = '\033[95m' + random.choice(list_4[1]) + '\033[0m'
            return a, 4
    else:
        a = '\033[37m' + random.choice(list_3) + '\033[0m'
        return a, 3


print("a pour x1, z pour x10, e pour inventaire, r pour reset")
inventaire = [[], [], []]
nbr = 0
pity_5 = 0
pity_4 = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                nbr += 1
                pity_5 += 1
                pity_4 += 1
                p, r = pull(pity_5, pity_4)
                print(('\033[33m'+str(pity_5)+'\033[0m'), ('\033[95m'+str(pity_4)+'\033[0m'), p)
                if r == 5:
                    pity_5 = 0
                    inventaire[0].append(p)
                if r == 4:
                    pity_4 = 0
                    inventaire[1].append(p)
                if r == 3:
                    inventaire[2].append(p)
                print("___________________")

            if event.key == pygame.K_z:
                for i in range(10):
                    nbr += 1
                    pity_5 += 1
                    pity_4 += 1
                    p, r = pull(pity_5, pity_4)
                    print(('\033[33m'+str(pity_5)+'\033[0m'), ('\033[95m'+str(pity_4)+'\033[0m'), p)
                    if r == 5:
                        pity_5 = 0
                        inventaire[0].append(p)
                    if r == 4:
                        pity_4 = 0
                        inventaire[1].append(p)
                    if r == 3:
                        inventaire[2].append(p)
                print("___________________")

            if event.key == pygame.K_e:
                print("pity =", nbr)
                print("5*")
                for i in inventaire[0]:
                    print(i)
                print("4*")
                for i in inventaire[1]:
                    print(i)
                print("3* : x",len(inventaire[2]))

            if event.key == pygame.K_r:
                inventaire = [[],[],[]]
                nbr = 0
                pity_5 = 0
                pity_4 = 0
