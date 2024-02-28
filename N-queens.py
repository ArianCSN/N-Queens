def func(arr , i , j):
    for x in range(8) :
        if arr[x][j] == "Q" :
            return 1

    for y in range(8) :
        if arr[i][y] == "Q" :
            return 1
    i2 = i
    j2 = j
    for x in range(8) :
        if arr[i2-1][j2-1] == "Q" :
                return 1
        else :
                i2 -= 1 
                j2 -= 1 
    i2 = i
    j2 = j
    for x in range(8) :
            if i2+1 == 8 :
                break
            if j2+1 == 8 :
                break
            if arr[i2+1][j2+1] == "Q" :
                return 1
            else :
                i2 += 1 
                j2 += 1 
    i2 = i
    j2 = j
    for x in range(8) :
            if i2+1 == 8 :
                break
            if arr[i2+1][j2-1] == "Q" :
                return 1
            else :
                i2 += 1 
                j2 -= 1 
    i2 = i
    j2 = j
    for x in range(8) :
            if j2+1 == 8 :
                break
            if arr[i2-1][j2+1] == "Q" :
                return 1
            else :
                i2 -= 1 
                j2 += 1 

    return 0

def check(arr , i):
    for x in range (8) :
        if arr[i][x] == "Q" :
            return 0
    return 1
    
arr = [
 [".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]
,[".", ".", ".", ".", ".", ".", ".", "."]]

flag = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
j=0
i=0 
ck=0
stop=0
while i<=8 :
    print(flag)
    print("i old =",i)
    if ck == 1 :
        arr[i][flag[i]] = "."
        print("i new = " ,i)
        j = flag[i]+1
        print("j new=" , j)
    while j<8 :
      print("actual j =" ,j)
      if func(arr , i , j) == 0 :
        arr[i][j] = "Q"
        flag[i] = j
        print("j old=",j)
        break 
      else :
           j+=1 
        
    if check(arr , i) :
        ck = 1 
        i-=1
        print("error")
    else :
        print("correct")
        j = 0 
        i+= 1
    
    if stop == 10 :
        break

    stop+=1


n = 8
for i in range(n):
    print()
    for j in range(n):
        print (arr[i][j] , end=' ')
print('\n')

