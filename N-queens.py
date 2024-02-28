import random
import os
import pygame
import time 

from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
 
pygame.init()
win = pygame.display.set_mode((800,800))
win.fill((255,255,255))
current_dir = os.path.dirname(os.path.abspath(__file__))
wqueen_path = os.path.join(current_dir, "queen-white.png")
bqueen_path = os.path.join(current_dir, "queen-black.png")
wqueen = pygame.transform.scale(pygame.image.load(wqueen_path), (100,100))
bqueen = pygame.transform.scale(pygame.image.load(bqueen_path), (100,100))
clock = pygame.time.Clock()
board = [['  ' for i in range(8)] for i in range(8)]

def check_is_digit(input):
    if input.strip().isdigit():
        return 1
    else:
        return 0

list = [0, 1, 2, 3, 4, 5, 6, 7]

board[0][random.choice(list)] = 'Q'


def attack(i, j):
    for k in range(0,8):
        if board[i][k]=="Q" or board[k][j]=="Q":
            return True
    for k in range(0,8):
        for l in range(0,8):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=="Q":
                    return True
    return False
def N_queens(n):
    if n==1:
        return True
    for i in range(1,8):
        for j in range(0,8):
            if (not(attack(i,j))) and (board[i][j]!="Q"):
                board[i][j] = 'Q'
                if N_queens(n-1)==True:
                    return True
                board[i][j] = "  "
    return False

N_queens(8)
i=0 
while i<8 :
    if i%2 == 0 :
        j=1
    else :
        j=0
    while j<8 :
        pygame.draw.rect(win,(0,0,0),[i*100,j*100,100,100])
        j+=2
    i+=1
        
for i in range(8):
    for j in range(8):
        if board[i][j] == "Q":
            if (i+j)%2 == 0 :
                win.blit(wqueen,(i*100,j*100))
            else :
                win.blit(bqueen,(i*100,j*100))
pygame.display.update()    


run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False