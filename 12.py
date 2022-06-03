#question 1
def moyenne(n1,n2,bonus=0):
    m = (n1+n2)/2+bonus
    if m > 20:
        return 20
    return m
print(moyenne(10,15,4))

#question 2
def points_manche(pcent,npoints,multi=1):
    return round(npoints * pcent/100,0) * multi

print(points_manche(20,3,3))

#question 3
def division_arrondi(num,denom,arrondir=False,decimales=0):
    if denom == 0:
        return "Erreur"
    if arrondir:
        return round(num/denom,decimales)
    return num/denom

print(division_arrondi(15,8,True,2))

