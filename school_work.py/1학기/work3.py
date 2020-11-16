"""
i=1
for i in range(1, 6) :
    print (i)
"""
"""
for i in range(1,11) :
    if i < 10 : 
        print(i, end=",")
    else: print(i, end="")
"""
"""
n = int(input("n = "))
s = 0
for n in range (1,n+1):
    s += n
print (s)
"""
"""
N = int(input("N = "))
while N > 0 :
    N -= 1
    if N%2 == 1 :
        print (N)
"""
N = int(input("N = "))
i = int(input("i = "))
if i == 1 :
    while N > 0 :
        if N % 2 == 1:
            print(N)
        N -= 1
if i == 2 :
    while N > 0 :
        if N % 2 == 0:
            print(N)
         N -= 1
else : print ("입력 오류")