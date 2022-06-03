#question 1
somme_pairs = lambda liste: sum([i for i in liste if i%2==0])

print(somme_pairs([4, 7, 12, 0, 21, 5]))

#question 2
def nb_elem_pairs(liste):
    s = 0
    for i in liste:
        if i%2==0:
            s+=1
    return s

print(nb_elem_pairs([4, 7, 12, 0, 21, 5]))

#question 3
max_pair = lambda liste: max([i for i in liste if i%2==0])

print(max_pair([4, 7, 12, 0, 21, 5]))

#question 4
min_pair = lambda liste: min([i for i in liste if i%2==0])

#question 5
indice_de = lambda n,liste: liste.index(n)

print(indice_de(12, [4, 7, 12, 0, 21, 5]))

#question 6
def trouve_premier_pair(liste):
    for i in liste:
        if i%2==0:
            return i

print(trouve_premier_pair([1, 15, 4, 7, 12, 3]))

#question 7
def extrait_pairs(l1):
    empt = []
    for i in l1:
        if i%2==0:
            empt.append(i)
    return empt

print(extrait_pairs([4, 7, 12, 0, 3]))




