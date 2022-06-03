#question 1
liste_decroissante = lambda n: [i for i in range(n,-1,-1)]
print(liste_decroissante(5))

#question 2
multiples = lambda m,longueur: [i for i in range(longueur) if i % m == 0]
print(multiples(3,20))

#question 3
pairs = lambda longueur: list(reversed(liste_decroissante(longueur)))[::2]
print(pairs(20))
