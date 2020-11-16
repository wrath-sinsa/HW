
a = int(input("a = "))
b = int(input("b = "))
while (a != 0 and b != 0):
    a , b = b , a % b
print (a)

"""
a = int(input("a = "))
b = int(input("b = "))
c = 1
d = 0
if a > b:
    a, b = b, a
while a >= c :
    if a % c == 0 and b % c == 0:
        d = c
    c += 1
e = int(a / d)
f = int(b / d)
print (d * e * f)
"""
"""
while True:
    a = int(input("a ="))
    b = int(input("b ="))
    A , B = a , b
    while A!= B:
        if A> B:
            B += b
        else :
            A += a
    print (A)
"""