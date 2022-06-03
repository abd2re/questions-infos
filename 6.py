#question 1
def lundi(text):
    return text + " " + text

print(lundi('bonjour'))

#question 2
def mardi(text):
    if len(text) % 2 == 0:
        return ((text + '-') * 6)[:-1]
    return ((text + ',') * 3)[:-1]

print(mardi('bonjour'))

#question 3
def mercredi(text):
    if len(text) % 2 == 1:
        return 'impair'
    return text

#question 4
print(mercredi('bonjour'))

def jeudi(text):
    return text * (len(text)%3)

print(jeudi('merci'))

#question 5
def vendredi(text):
    return text

print(vendredi('bonjour'))

#question 6
l = [lundi, mardi, mercredi, jeudi, vendredi]

def transform(text,num_jour):
    return l[num_jour-1](text)

print(transform('bonjour',5))