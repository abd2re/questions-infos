#question 1
decale = lambda l,d: [i+d for i in l]
print(decale([1,2,3,4,5],2))

#question 2
def intercale_zeros(l):
    arr = []
    for i in l:
        arr.append(i)
        arr.append(0)
    return arr

print(intercale_zeros([1,2,3,4,5]))

#question 3
def supprime(l,elem):
    arr = []
    for i in l:
        if i!= elem:
            arr.append(i)
    return arr

print(supprime([4, 7, 12, 4, 4, 0, 4, 5], 4))

#question 4
def insere_milieu(l,elem):
    if len(l)%2==0:
        l.insert(len(l)//2,elem)
    if len(l)%2==1:
        l.insert(len(l)//2+1,elem)
        l.insert(len(l)//2-1,elem)
    return l

print(insere_milieu([9, 3, 5, 6, 2], 1))

#question 5
def decoupe(l,seuil):
    lsup = l.copy()
    linf = l.copy()
    for i in range(len(l)):
        if l[i]<=seuil:
            lsup.remove(l[i])
        else:
            linf.remove(l[i])
    return linf,lsup

print(decoupe([14, 27, 12, 0, 40, 34, 20, 11], 20))

