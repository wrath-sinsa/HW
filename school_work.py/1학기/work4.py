"""
a = int(input('a = '))
for i in range (1, int(a/2)+1):
    if a % i == 0:
        print(i, end=" ")
print(a)
"""
"""
a = int(input("a = "))
b = int(input("b = "))

if (a>0 and b>0) or (a<0 and b<0):
    print ("양수")
else : print ("음수")
"""
"""
a = int(input("a = "))
b = int(input("b = "))    
c = 1
d = 0
if (a<b):
    a,b = b,a
while (b>=c):
    if (a % c == 0 and b % c == 0):
        d = c
    c += 1
print (d)
"""
a = int(input("a = "))
b = int(input("b = "))
d = 0
if (b>a):
    a,b = b,a
c = a % b
while (c != 0 and b != 0):
    b = b % c
    c = c % b
if b == 0 :
    b,c = c,b
print (b)
    
