# 1. 한줄 지나가면 2배 길어짐

def Double(N) : 
    n = 1
    a = 1
    while N >= a :
        for i in range (n) :
            if N >= a :
                print (a, end =" ")
                a += 1
        n *= 2
        print ("\n")

N = int(input("N = "))
Double(N)


# 2. evalTerm(a, x, e) a * x ^ e

def evalTerm (a, x, e) :
    s = 1
    for i in range (e) :
        s *= x
    s *= a
    return s

A = evalTerm(4, 2, 3)
print (A)