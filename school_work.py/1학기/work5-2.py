"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
A , B , C = a, b, c
while A!=B:
    if A>B:
        B += b
    else :
        A += a
S = A
while S!=C:
    if S>C:
        C += c
    else :
        S += A 
print (a, b, c, "의 최소공배수는", S, "입니다")
"""
"""
a = int(input("a = "))  
n = 1
s = 0
while a > n :
    if a % n == 0 :
        s += n
    n += 1
if s == a :
    print (a , "는 완전수 입니다.")
else :
    print (a , "는 완전수가 아닙니다.")
"""
"""
N = int(input("N = "))
if N < 2 :
    while N < 2 :
        print ("N는 2보다 큰 자연수여야 합니다")
        N = int (input("N = "))    
a = 2
b = 1
while N >= a :
    s = 0
    while int(a/2) >= b :
        if a % b == 0 :
            s += b
        b += 1    
    if s == a:
        print (a) 
    a += 1
    b = 1
"""