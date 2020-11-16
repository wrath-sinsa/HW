# 1번
"""
def twoSum(a, n) :
    b = []
    for i in range (0,int(n/2)+1,2) :
        b.append(a[i]+a[i+1])
    if n % 2 == 1 :
        b.append(a[n-1])
    return b

import random
N = int(input("N = "))
a = []
for i in range(N) :
    a.append(random.randint(1,5))
print (a)
b = twoSum(a,N)
print (b)
"""

#2번
"""
def printMatrix(A) : 
    a = len(A)
    b = 0
    c = 0
    d = 0
    for i in range (a) :
        for j in range (a) :
            print (A[i][j], end=" ")
        b += A[i].count(0)
        c += A[i].count(1)
        d += A[i].count(2)
        print("\n")
    print ("0은", b, "개", "1은", c, "개", "2는", d,"개 입니다.")


import random
N = int(input("N = "))
a = []
for i in range (N) :
    b = []
    a.append(b)
    for j in range (N) :
        a[i].append(random.randint(0,2))
print (a)
printMatrix(a)
"""

#3번
"""
def isPrime(a) : 
    b = 0
    if a >= 2 :
        for i in range (1, int(a/2)+1) :
            if a % i == 0 :
                b = i
        if b == 1 :
            return 2
        else : return 3

def printPrime(a) :
    b = 0
    c = 0
    for i in range (len(a)) :
        if isPrime(a[i]) == 2 :
            b += a[i]
        else : c += a[i]
    print ("소수의 합 :", b)
    print ("비소수의 합 :", c)


N = 0
a = []
while N != 999 :
    N = int(input("정수 입력(종료시 999) : "))
    if N <2 :
        print ("2 이상의 수만 입력하세요.")
    elif N == 999:
        print ("종료합니다.")
    else :
        if a.count(N) == 0 :
            a.append(N)
print(a)
printPrime(a)
"""
#4번
# def printRatio(n, minValue, maxValue):
#     a = []
#     for i in range (n) :
#         a.append(random.randint(minValue,maxValue))
#     for j in range (minValue, maxValue+1) :
#         b = a.count(j)
#         print (j,"의 빈도수", b)

# import random
# N = int(input("N = "))
# MIN = int (input("MIN = "))
# MAX = int (input("MAX = "))
# printRatio (N, MIN, MAX)

# count 안쓰기;
import random

def printRatio(n, minValue, maxValue) :
    a = []
    # c = 0 # 100개 맞나 확인용
    for i in range (n) :
        a.append(random.randint(minValue, maxValue))
    for j in range (minValue, maxValue+1) :
        b = 0
        for k in range (n) :
            if j == a[k] :
                b += 1
        # c += b
        print (j , "는", b, "개 입니다.")
        # print (c)

N = int(input("N = "))
MIN = int(input("MIN = "))
MAX = int(input("MAX = "))
printRatio (N, MIN, MAX)

