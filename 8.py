#question 1
def ann_suiv(x) :
    return int(x*1.09-200)

print(ann_suiv(8000))

#question 2
def nb_moustiques(nb_debut,annee_voulue):
    d = annee_voulue - 2017
    return int(nb_debut*1.09**d-200*d)

print(nb_moustiques(8000,2018))

#question 3
def annee_atteindra(seuil,nb_debut):
    c = 0
    while nb_debut <= seuil:
        nb_debut = ann_suiv(nb_debut)
        c += 1
    return c + 2016

print(annee_atteindra(8520,8000))


