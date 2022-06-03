def depasse(A):
    a = 1
    while True:
        f = 1
        for i in range(1,a+1):
            f = f * i
        if f >= A:
            return a
        else:
            a += 1



print(depasse(120))