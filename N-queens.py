import random
import os
import pygame
from pygame.locals import QUIT
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()
number = simpledialog.askinteger(title="Queen Number?",
                                  prompt="Enter the row number for the first queen (1 - 8): ")

pygame.init()
FullBoard = pygame.display.set_mode((800,800))
FullBoard.fill((255,255,255))
current_dir = os.path.dirname(os.path.abspath(__file__))
wqueen_path = os.path.join(current_dir, "queen-white.png")
bqueen_path = os.path.join(current_dir, "queen-black.png")
wqueen = pygame.transform.scale(pygame.image.load(wqueen_path), (100,100))
bqueen = pygame.transform.scale(pygame.image.load(bqueen_path), (100,100))

board = [[' ' for i in range(8)] for i in range(8)]
list = [0, 1, 2, 3, 4, 5, 6, 7]
number -=1
if 0<= number <=7 :
    board[0][number] = 'Q'
else :
    messagebox.showerror("Error",
     "Invalid input! The program will randomly select a position between 1 and 8.")
    board[0][random.choice(list)] = 'Q' 

#Engine 
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
                board[i][j] = " "
    return False

N_queens(8)


i=0 
while i<8 :
    if i%2 == 0 :
        j=1
    else :
        j=0
    while j<8 :
        pygame.draw.rect(FullBoard,(0,0,0),[i*100,j*100,100,100])
        j+=2
    i+=1
        
for i in range(8):
    for j in range(8):
        if board[i][j] == "Q":
            if (i+j)%2 == 0 :
                FullBoard.blit(wqueen,(i*100,j*100))
            else :
                FullBoard.blit(bqueen,(i*100,j*100))
pygame.display.update() 


run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False