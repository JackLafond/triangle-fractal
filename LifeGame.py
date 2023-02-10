# game of life

import numpy as np
import pygame 
import time

scrSize = 800
gridSize = 600
bound = (scrSize - gridSize)/2
intv = gridSize / 20

startLen = gridSize/4
startHeight = bound/2
startX = scrSize/2 - startLen/2
startY = scrSize - bound + startHeight/2
startRect = pygame.Rect(startX, startY, startLen, startHeight)

resetX = bound
resetY = startY
resetLen = gridSize/4
resetHeight = startHeight
resetRect = pygame.Rect(resetX, resetY, resetLen, resetHeight)

stopLen = gridSize/4
stopHeight = startHeight
stopX = scrSize - bound - stopLen
stopY = startY
stopRect = pygame.Rect(stopX, stopY, stopLen, stopHeight)

pygame.init()
scr = pygame.display.set_mode((scrSize, scrSize))
pygame.display.set_caption("Game of Life")

mat = np.zeros((20, 20))

def printGrid(aMat, scr):
    for i in range(20):
        ix = i * intv
        for j in range(20):
            jx = j * intv
            aRect = pygame.Rect(100 + ix, 100 + jx, intv, intv)
            if aMat[i][j] == 0:
                pygame.draw.rect(scr, (200, 200, 200), aRect, 1)
            else:
                pygame.draw.rect(scr, (200, 200, 200), aRect)
    pygame.draw.rect(scr, (0, 200, 0), startRect)
    pygame.draw.rect(scr, (200, 0, 0), stopRect)
    pygame.draw.rect(scr, (0, 0, 200), resetRect)
    
def matUpdateStart(aMat, x, y):
    r = (int)((x - bound) / intv)
    c = (int)((y - bound) / intv)
    aMat[r][c] = 1
    return aMat

def iterateMat(aMat):
    newMat = np.zeros((20,20))
    for i in range(20):
        for j in range(20):
            nbr = 0
            if i == 0:
                if j == 0:
                    nbr = aMat[i+1][j] + aMat[i+1][j+1] + aMat[i][j+1]
                elif j == 19:
                    nbr = aMat[i+1][j] + aMat[i+1][j-1] + aMat[i][j-1]
                else:
                    nbr = aMat[i][j-1] + aMat[i+1][j-1] + aMat[i+1][j] + aMat[i+1][j+1] + aMat[i][j+1]
            elif i == 19:
                if j == 0:
                    nbr = aMat[i-1][j] + aMat[i-1][j+1] + aMat[i][j+1]
                elif j == 19:
                    nbr = aMat[i-1][j] + aMat[i-1][j-1] + aMat[i][j-1]
                else:
                    nbr = aMat[i][j-1] + aMat[i-1][j-1] + aMat[i-1][j] + aMat[i-1][j+1] + aMat[i][j+1]
            else:
                if j == 0:
                    nbr = aMat[i-1][j] + aMat[i-1][j+1] + aMat[i][j+1] + aMat[i+1][j+1] + aMat[i+1][j]
                elif j == 19:
                    nbr = aMat[i-1][j] + aMat[i-1][j-1] + aMat[i][j-1] + aMat[i+1][j-1] + aMat[i+1][j]
                else:
                    nbr = aMat[i-1][j-1] + aMat[i-1][j] + aMat[i-1][j+1] + aMat[i][j-1] + aMat[i][j+1] + aMat[i+1][j-1] + aMat[i+1][j] + aMat[i+1][j+1]

            if aMat[i][j] == 0:
                if nbr == 3:
                    newMat[i][j] = 1
                else:
                    newMat[i][j] = 0
            else:
                if nbr < 2 or nbr > 3:
                    newMat[i][j] = 0
                else:
                    newMat[i][j] = 1
    return newMat


running = True
drawn = False
start = False
end = False
reset = False
stop = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= bound and my >= bound and mx <= bound + gridSize and my <= bound + gridSize and not start:
                mat = matUpdateStart(mat, mx, my)
                drawn = False
            elif mx >= startX and my >= startY and mx <= startX + startLen and my <= startY + startHeight:
                start = True
                stop = False
            elif mx >= stopX and my >= stopY and mx <= stopX + stopLen and my <= stopY + stopHeight:
                start = False
                stop = True
            elif mx >= resetX and my >= resetY and mx <= resetX + resetLen and my <= resetY + resetHeight:
                reset = True

    if reset:
        start = False
        stop = False
        drawn = False
        mat = np.zeros((20, 20))
        reset = False

    if start:
        mat = iterateMat(mat)
        drawn = False

    if not drawn and not stop:
        scr.fill((0, 0, 0))
        printGrid(mat, scr)
        pygame.display.update()
        drawn = True
        time.sleep(.75)

pygame.quit()
