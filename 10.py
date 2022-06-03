# plus grand diviseur premier

#question 1 :
def est_premier(x):
    for a in range(2,x):
        if x % a == 0:
            return False
    return True

def plus_grand_diviseur_premier(n) :
    for i in range(n,0,-1):
        if n % i  == 0 and est_premier(i):
            return i


print(plus_grand_diviseur_premier(24))

#question 2 :
def pgcd(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i

print(pgcd(12,16))

#question 3 :
def ppcm(a,b):
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            return i

print(ppcm(81,90))

#question 4 :
def irreductible(numerateur, denominateur):
    if denominateur % 2 == 0 or denominateur % 5 == 0 or numerateur % denominateur == 0:
        return True
    return False

print(irreductible(12,7))

