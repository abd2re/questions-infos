#question 1
def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#question 2
def sphinx_aime(p):
    if est_premier(p) and est_premier(p+2):
        return True
    return False

print(sphinx_aime(17))

#question 3
def code_hall(n_pref):
    i = n_pref
    while not sphinx_aime(i):
        i += 1
    return i

print(code_hall(15))

#question 4
import math
def est_puissance2(n):
    if math.log(n, 2) % 1 == 0:
        return True

print(est_puissance2(8))

#question 5
def osiris_aime(p):
    if est_puissance2(p+1) and p%5==3:
        return True
    return False

print(osiris_aime(63))

#question 6
def code_tresor(n_pref):
    i = n_pref
    while not osiris_aime(i):
        i += 1
    return i

print(code_tresor(20))


