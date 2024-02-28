import random

def check_is_digit(input):
    if input.strip().isdigit():
        return 1
    else:
        return 0

board = [
 [".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]]

list = [0, 1, 2, 3, 4, 5, 6, 7]

number = input("Enter the row number for the first queen (1 - 8): ")
if check_is_digit(number)  :
    number = int(number)
    number -=1
    if 0<= number <=7 :
        board[0][number] = 'Q' 
    else :
        print("Invalid input! The program will randomly select a position between 1 and 8.")
        board[0][random.choice(list)] = 'Q' 
else :
    print("Invalid input! The program will randomly select a position between 1 and 8.")
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
                board[i][j] = "."
    return False

N_queens(8)

for i in range(8):
    print()
    for j in range(8):
        print (board[i][j] , end=" ")
