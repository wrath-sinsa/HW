a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d = int(input("d : "))

if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if c>d:
    c,d=d,c
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a,b,c,d)