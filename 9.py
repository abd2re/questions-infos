# banque

# question 1 :
def capital(nb_annee, capital_debut) :
    return capital_debut*1.05**nb_annee - 11 * nb_annee

print(capital(10,8000))

#question 2 :
def gagner_argent(nb_annee, capital_debut):
    if capital(nb_annee, capital_debut) >= capital_debut :
        return True
    else :
        return False

print(gagner_argent(10,8000))

