def abc(N) :
    a = 1
    b = 1
    while N >= a :
        for j in range (b) :
            if N >= a :
                print (a, end=" ")
                a += 1
        b *= 2
        print ("\n")

def evalTerm(a, x, e) : 
    A = 1
    for i in range (e) :
        A *= x
        print (A)
    A *= a
    print (A)

evalTerm(4, 2, 3)