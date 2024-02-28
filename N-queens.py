import random
import os
import pygame
from pygame.locals import QUIT
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

clock = pygame.time.Clock()
ROOT = tk.Tk()
ROOT.withdraw()

# Configuration
# CLOCK : speed of queens placement on the board during the program execution.
CLOCK = 0
# USER_INPUT: If set to 1, the program will prompt the user to input the position of the first queen.
USER_INPUT = 1
# RED: If set to 1, after each queen placement and movement, the program highlights the old position in red.
RED = 0
# N: Number of Queens and size of the chessboard (N x N).
N = 10
# Create the chessboard and load images for black and white queens.
# Queen with a black background: queen-black.png
# Queen with a white background: queen-white.png
# !!Make sure to load the images from the appropriate folder!!
pygame.init()
FullBoard = pygame.display.set_mode((N*50,N*50))
FullBoard.fill((255,255,255))

current_dir = os.path.dirname(os.path.abspath(__file__))
wqueen_path = os.path.join(current_dir, "queen-white.png")
bqueen_path = os.path.join(current_dir, "queen-black.png")
wqueen = pygame.transform.scale(pygame.image.load(wqueen_path), (50, 50))
bqueen = pygame.transform.scale(pygame.image.load(bqueen_path), (50, 50))


# If the user enters a number between 1 and 8, it will be used as the initial queen position.
# Otherwise, the program will randomly select a position between 0 and 7 from the list.
number = 0 
board = [[' ' for i in range(N)] for i in range(N)]
list = [0, 1, 2, 3, 4, 5, 6, 7]
if (USER_INPUT) :
    number = simpledialog.askinteger(title="Queen Number?",
                                  prompt="Enter the row number for the first queen (1 - 8): ")
    number -=1
    if 0<= number <=7 :
      board[0][number] = 'Q'
    else :
        messagebox.showerror("Error",
         "Invalid input! The program will randomly select a position between 1 and 8.")
        number = random.choice(list)
        board[0][number] = 'Q' 
else :
    number = random.choice(list)
    board[0][number] = 'Q'

# Placing white and black squares on the board
i=0 
while i<N :
    if i%2 == 0 :
        j=1
    else :
        j=0
    while j<N :
        pygame.draw.rect(FullBoard,(0,0,0),[i*50,j*50,50,50])
        j+=2
    i+=1

# placing the first queen
if (0+number)%2 == 0 :
    FullBoard.blit(wqueen,(0*50,number*50))
else :
    FullBoard.blit(bqueen,(0*50,number*50))
pygame.display.update()


# N queen Logic
def attack(i, j):
    for k in range(0,N):
        if board[i][k]=="Q" or board[k][j]=="Q":
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=="Q":
                    return True
    return False
def N_queens(n):
    if n==1:
        return True
    for i in range(1,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!="Q"):
                board[i][j] = 'Q'
                if (i+j)%2 == 0 :
                    FullBoard.blit(wqueen,(i*50,j*50))
                else :
                    FullBoard.blit(bqueen,(i*50,j*50))
                    clock.tick(CLOCK)
                    pygame.display.update() 
                if N_queens(n-1)==True:
                    return True
                board[i][j] = " "
                if (RED) :
                    pygame.draw.rect(FullBoard,(255,0,0),(i*50,j*50,50,50))
                    clock.tick(CLOCK)
                    pygame.display.update()
                if (i+j)%2 == 0 :
                    pygame.draw.rect(FullBoard,(255,255,255),[i*50,j*50,50,50])
                else :
                    pygame.draw.rect(FullBoard,(0,0,0),[i*50,j*50,50,50])
                    clock.tick(CLOCK)
                    pygame.display.update() 

    return False

N_queens(N)

# displaying the final positions of the queens
for i in range(N):
    for j in range(N):
        if board[i][j] == "Q":
            if (i+j)%2 == 0 :
                FullBoard.blit(wqueen,(i*50,j*50))
            else :
                FullBoard.blit(bqueen,(i*50,j*50))
pygame.display.update() 

# Pygame display loop continues until the user closes the window
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False