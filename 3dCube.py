import numpy as np
import pygame

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def getRotM(a, b, c):

    Pa = np.zeros((3, 3))
    Pa[0][0] = np.cos(a)
    Pa[0][1] = -np.sin(a)
    Pa[1][0] = np.sin(a)
    Pa[1][1] = np.cos(a)
    Pa[2][2] = 1

    Pb = np.zeros((3, 3))
    Pb[0][0] = np.cos(b)
    Pb[1][1] = 1
    Pb[2][0] = np.sin(b)
    Pb[0][2] = -np.sin(b)
    Pb[2][2] = np.cos(b)

    Pc = np.zeros((3, 3))
    Pc[0][0] = 1
    Pc[1][1] = np.cos(c)
    Pc[1][2] = -np.sin(c)
    Pc[2][1] = np.sin(c) 
    Pc[2][2] = np.cos(c)

    P = Pa@Pb@Pc

    return P

def rot(cube, amx, amy):

    if amx == 0 and amy == 0:
        return cube

    rad = np.sqrt(pow(amx, 2) + pow(amy, 2))
    rx = np.abs(amx/rad)
    ry = np.abs(amy/rad)

    if amx > 0:
        a = rx/10
    elif amx < 0:
        a = -rx/10
    else:
        a = 0

    if amy > 0:
        b = ry/10
    elif amy < 0:
        b = -ry/10
    else:
        b = 0

    c = ry/rx/10
    P = getRotM(a, b, c)
    
    for i in range(8):
        z = cube[i].z

        pt = np.array([amx, amy, z])

        newpt = P@pt

        newpt[0] = newpt[0] + width/2
        newpt[1] = newpt[1] + height/2

        cube[i].x = newpt[0]
        cube[i].y = newpt[1]
        cube[i].z = newpt[2]

    return cube

height = 1000
width = 1000
length = width/2
buffer = min(width/5, height/5) 

pygame.init()
scr = pygame.display.set_mode((height, width))
pygame.display.set_caption("Cube")

p1 = Point(buffer, 2 * buffer, 0)
p2 = Point(width/2, 3 * buffer, (width - 2 * buffer)/2)
p3 = Point(width - buffer, 2 * buffer, 0)
p4 = Point(width/2, buffer, -(width - 2 * buffer)/2)
p5 = Point(buffer, height - 2 * buffer, 0)
p6 = Point(width/2, height - buffer, (width - 2 * buffer)/2)
p7 = Point(width - buffer, height - 2 * buffer, 0)
p8 = Point(width/2, height - 3 * buffer, -(width - 2 * buffer)/2)

cube = [p1, p2, p3, p4, p5, p6, p7, p8]

running = True
drawn = False

while running:

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            amx = mx - width/2
            amy = my - height/2
            cube = rot(cube, amx, amy)
            drawn = False

    if not drawn:
        pygame.draw.line(scr, (200, 200, 200), (cube[0].x, cube[0].y), (cube[1].x, cube[1].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[1].x, cube[1].y), (cube[2].x, cube[2].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[2].x, cube[2].y), (cube[3].x, cube[3].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[3].x, cube[3].y), (cube[0].x, cube[0].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[4].x, cube[4].y), (cube[5].x, cube[5].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[5].x, cube[5].y), (cube[6].x, cube[6].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[6].x, cube[6].y), (cube[7].x, cube[7].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[7].x, cube[7].y), (cube[4].x, cube[4].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[0].x, cube[0].y), (cube[4].x, cube[4].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[1].x, cube[1].y), (cube[5].x, cube[5].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[2].x, cube[2].y), (cube[6].x, cube[6].y), 1)
        pygame.draw.line(scr, (200, 200, 200), (cube[3].x, cube[3].y), (cube[7].x, cube[7].y), 1)
        drawn = True
        
        pygame.display.update()

pygame.quit()

    