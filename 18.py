#question 1
def NextElem(elm,liste):
    liste.append(liste[0])
    if elm in liste:
        return liste[liste.index(elm)+1]

print(NextElem('c',['a','b','c']))

#question 2
import string
ordre = [' '] + list(string.ascii_lowercase) + [".",'?','!',',',';',':',"'",'(',')','[',']','{','}']
def encode(texte,liste):
    a = ''
    for i in texte:
        a = a + str(liste.index(i)) + ' '
    return a

print(encode("hello world",ordre))



