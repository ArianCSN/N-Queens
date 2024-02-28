import random

board = [
 [".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]]


def check(i, j):
    for k in range(0,8):
        if board[i][k]=="Q" or board[k][j]=="Q":
            return False
    for k in range(0,8):
        for l in range(0,8):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=="Q":
                    return False
    return True

def N_queens(n):
    if n==0:
        return True
    for i in range(0,8):
        for j in range(0,8):
            if (check(i,j)) and (board[i][j]!="Q"):
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
