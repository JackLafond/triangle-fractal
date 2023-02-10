import numpy as np
import pygame
import random

width = 1000
height = 1000
iter = 100000
frac = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pygame.init()
scr = pygame.display.set_mode((height, width))
pygame.display.set_caption("Triangle Fractal")
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not frac:
        p1 = Point(.5 * width, 100)
        p2 = Point(p1.x + ((height - 200) / np.sqrt(3)), height - 100)
        p3 = Point(p1.x - ((height - 200) / np.sqrt(3)), height - 100)

        plist = [p1, p2, p3]

        pygame.draw.circle(scr, (165, 165, 165), (p1.x, p1.y), 1)
        pygame.draw.circle(scr, (165, 165, 165), (p2.x, p2.y), 1)
        pygame.draw.circle(scr, (165, 165, 165), (p3.x, p3.y), 1)

        dotX = p1.x
        dotY = p1.y
        for i in range(iter):
            rand = random.randint(0, 2)
            rX = plist[rand].x
            rY = plist[rand].y
            dotX = dotX + int(.5 * (rX - dotX))
            dotY = dotY + int(.5 * (rY - dotY))
            pygame.draw.circle(scr, (200, 200, 200), (dotX, dotY), 1)
            pygame.display.update() 
        frac = True

    pygame.display.update()
    
pygame.quit()