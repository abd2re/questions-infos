#question 1
def tarif_carte(reduction=None):
    if reduction == 'Jeune':
        return 50
    if reduction == 'Senior':
        return 60
    if reduction == None:
        return 0
    else:
        print('Carte inconnue')
        return False

#question 2
trajets = [
    ('Grenoble', 'Paris', 100),
    ('Grenoble', 'Lyon', 20),
    ('Lyon', 'Paris', 80)
]

def plein_tarif(depart,arrive):
    for i,j,prix in trajets:
        if list(zip(depart,arrive)) == list(zip(i,j)) or list(zip(depart,arrive)) == list(zip(j,i)):
            return prix
    print('Trajet inconnu')
    return False

#print(plein_tarif('Paris','Lyon'))

#question 3
def tarif_billet(depart,arrive,modifiable=True,carte=None,periode=None):
    trajet = plein_tarif(depart,arrive)
    carte_valide = tarif_carte(carte)
    if carte==None:
        if modifiable==False:
            return trajet * 0.9
    if periode=='bleue':
        return trajet * 0.5
    if periode=='blanche':
        if carte=='Jeune':
            return trajet * 0.7
        if carte=='Senior':
            return trajet * 0.75
    return trajet

#print(tarif_billet('Paris','Grenoble',modifiable=False,carte=None,periode=None))

#question 4
def prix_client():
    prix_total = 0
    achat_de_carte = input("Voulez-vous acheter une cartede réduction ? (oui/non) : ")
    if achat_de_carte == 'oui':
        carte = input("Quelle carte ? (Jeune/Senior) : ")
        prix_total += tarif_carte(carte)
    if achat_de_carte == 'non':
        carte = None
    achat_de_billet = input('Voulez-vous acheter un billet ? (oui/non) : ')
    if achat_de_billet == 'oui':
        depart = input('depart: ')
        destination = input('destination: ')
        if tarif_carte(carte) > 0:
            print("Vous avez une carte de reduction")
            periode = input('Quelle periode ? (bleue/blanche) : ')
            prix_total += tarif_billet(depart,destination,carte=carte,periode=periode)
        if tarif_carte(carte) == 0:
            precision = input("Autres precisions a fournir ? (oui/non) : ")
            if precision == 'non':
                prix_total = tarif_billet(depart,destination,carte=carte,periode=None)
            if precision == 'oui':
                carte = input("Carte de reduction (Jeune, Senior, ou aucune)? : ")
                if carte == 'Jeune' or carte == 'Senior':
                    periode = input('Quelle periode ? (bleue/blanche) : ')
                    prix_total = tarif_billet(depart,destination,carte=carte,periode=periode)
                if carte == 'aucune':
                    modifiable = input("Billet modifiable ? (oui/non) : ")
                    if modifiable == 'oui':
                        prix_total = tarif_billet(depart,destination,modifiable=True,carte=None,periode=None)
                    if modifiable == 'non':
                        prix_total = tarif_billet(depart,destination,modifiable=False,carte=None,periode=None)
        return prix_total
    if achat_de_billet == 'non':
        return prix_total
    else:
        prix_client()


print(prix_client())




