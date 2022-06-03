#question 1
def commence_par(lettre,mot):
    if list(mot)[0] == lettre:
        return True
    return False

print(commence_par('h','hello'))

#question 2
voyelles = ['a','e','i','o','u']
def contient_voyelle(mot):
    for i in voyelles:
        if i in mot:
            return True
    return False

print(contient_voyelle('hello'))

#question 3
def derniere_consonne(mot):
    for i in range(len(list(mot))-1,-1,-1):
        if list(mot)[i] not in voyelles:
            return [i,list(mot)[i]]

print(derniere_consonne('arrivee'))

#question 4
def double_consonne(mot):
    for i in range(len(list(mot))-1):
        if list(mot)[i] == list(mot)[i+1] and list(mot)[i] not in voyelles:
            return True,list(mot)[i]
    return False,None

print(double_consonne('reussite'))

#question 5
envers = lambda li: [li[i] for i in range(len(li)-1,-1,-1)]

print(envers(['a', 'b', 'c', 'd']))

#question 6
def mot_autorise(mot):
    if list(mot) == envers(list(mot)):
        return True
    return False

print(mot_autorise('ici'))

#question 7
def mot_autorise(mot,liste):
    if mot not in liste:
        return True
    return False
print(mot_autorise('fric', ['sous', 'fric', 'thune', 'ble']))