#question 1
def LireListeEntiers():
    arr = []
    n = 0
    while n >= 0:
        n = float(input("Entrez un entier positif: "))
        arr.append(n)
    return arr[:-1]

#print(LireListeEntiers())

#quesion 2
def callFunc(func):
    print(func())

#callFunc(LireListeEntiers)

#question 3
def LireListeReelsBornes(bmin=0,bmax=100):
    arr = []
    n = bmin
    while n >= bmin and n <= bmax:
        n = float(input("Entrez un entier positif: "))
        arr.append(n)
    return arr[:-1]

#print(LireListeReelsBornes(bmin=1,bmax=15))

#question 4
def MMSL(arr:list):
    maxarr,minarr = arr.copy(), arr.copy()
    for i in range(len(arr)-1):
        if maxarr[i] > maxarr[i+1]:
            maxarr[i+1] = maxarr[i]
        if minarr[i] < minarr[i+1]:
            minarr[i+1] = minarr[i]
    return f'max : {maxarr[-1]}, min : {minarr[-1]}'

#print(MMSL([1,2,3,4,5,6,7,8,9,10]))

#question 5
def callFunc(func):
    print(func)
    print(MMSL(func))

callFunc(LireListeReelsBornes(4,50))