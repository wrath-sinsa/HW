"""
N = int(input("N = "))
print ("1:홀수 , 2:짝수")
i = int(input("i = "))
a = 1
if i == 1 :
    while N>=a :
        if a % 2 == 1 :
            print (a)
        a += 1
elif i == 2 :
    while N>=a :
        if a % 2 == 0 :
            print (a)
        a += 1
else : print ("입력 오류")
"""
"""
N = int(input("N = "))
print ("1:홀수, 2:짝수")
i = int(input("i = "))
if i == 1 :
    for a in range (1,N+1) :
        if a % 2 == 1 :
            print (a)
elif i == 2 :
    for a in range (1,N+1):
        if a % 2 == 0 :
            print (a)
else : print ("입력 오류")
"""
"""
N = int(input("자연수 입력 : "))
a = 1
if N>0 :
    while (N>=a) :
        if N % a == 0 : 
            print (a)
        a += 1
else : print(N,"은 자연수가 아닙니다.")
"""
"""
N = int(input("자연수 입력 : "))
while N <= 0 :
    print (N,"은 자연수가 아닙니다")
    N = int(input("자연수 입력 : "))
a = 1
while (N>=a):
    if N % a == 0 :
        print (a)
    a += 1
"""
    
