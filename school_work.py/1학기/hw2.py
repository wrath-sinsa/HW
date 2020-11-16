N = int(input("N = "))
a = 2
while N >= a :
    b = 1
    c = 0
    if a == 2 :
        print (a)
        a += 1
    while int(a/2)+1 >= b : 
        if a % b == 0:
            c = b
        b += 1
    if c == 1:
        print (a)
    a += 1    