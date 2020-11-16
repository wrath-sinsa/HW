def route(N) : #루트 N까지의 소수 구하기 (d : 소수 )
    a = int(N ** 0.5) # a는 루트 N
    b = 2
    d = []
    while a >= b :
        i = 1
        c = [b]
        while b/2 >= i :
            #print (c)
            if b % i == 0 :
                c.append(i)
                #print (c)
            i += 1
        if len(c) == 2 :
            d.append(b)
        b += 1
    print (d)
    return d

def sosu(N) : # N까지의 소수 구하기
    a = list(range(N+1))
    a[1]=a[0]
    b = route(N)
    for i in range (0,len(b)) : 
        j = 2
        while N >= b[i] * j :
            a[b[i]*j] = a[0]
            j += 1
    while a.count(0) != 0 :
        a.remove(0)
    print (a)
    print (len(a))
    return a

N = int(input("N = "))
sosu(N)