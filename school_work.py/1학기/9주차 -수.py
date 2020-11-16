# 1번

"""
N = 0
a = []
while N != 999 :
    N = int(input("N (999종료)= "))
    if N == 999 :
        break
    else :
        a.append(N)
print (a)
"""

# 2번

"""
import random
a = []
N = int(input("N = "))
for i in range (N) :
    a.append(random.randint(1,N))
print (a)
"""

# 3번

## 3.1
"""
import random
a = []
i = 0
N = int(input("N = "))
while i < N :
    b = random.randint(1,N)
    if a.count(b) == 0 :
        a.append(b)
    else : i -= 1
    i += 1
print (a)
"""
## 3.2
"""
import random
a = []
i = 0
N = int(input("N = "))
while i < N :
    b = random.randint(1,N)
    while a.count(b) != 0 :
        b = random.randint(1,N)
    a.append(b)
    i += 1
print (a)
"""
## 3.3 셔플 사용하기!!!
"""
import random

N = int(input("N = "))
a = list(range (1,N+1)) 
random.shuffle(a)
print (a)
"""
# 4번
"""
def Even(N) :
    if N % 2 == 0 :
        return 1 # 짝수
    else : return 0 # 홀수

def Perfect(N) :
    i = 0
    for j in range (1, int(N/2)+1) :
        if N % j == 0 :
            i += j
    if i > N : return 2 # 과잉수 
    elif i < N : return 3 # 부족수
    else : return 4 # 완전수

def Prime(N) :
    i = []
    i.append(N)
    for j in range (1, int(N/2)+1) :
        if N % j == 0 :
            i.append(j)
    if len(i) == 2 :
        return 1 # 소수
    else : return 0 # 비소수

A = int(input("A = "))
B = int(input("B = "))

for i in range (A,B+1) :
    print (i)
    if Even(i): print ("짝수")
    else : print ("홀수")
    if Perfect(i) == 2 : print ("과잉수")
    elif Perfect(i) == 3 :print ("부족수")
    else : print ("완전수")
    if Prime(i) : print ("소수")
    else : print ("비소수")
"""
# 5번
"""
def makeL(M, N):
    a = []
    for i in range (M) :
        b = []
        for j in range (N) :
            b.append(random.randint(1,m))
        a.append(b)
    return a

import random
m = int(input("m = "))
n = int(input("n = "))
print (makeL(m, n))
"""

# 6번
"""
def abc(n):
    a = []
    b = 0
    for i in range (n):
        a.append(random.randint(1,n))
    for j in range (n):
        b += a[j]
    return b

import random
N = int(input("N = "))
a = abc(N)
print ("합 : %d 평균 : %.1f "%(a,a/N))
"""
# 7번
"""
def abc(s):
    a = []
    for i in range (26) :
        a.append(0)
    print (a)
    for j in range (len(s)) :
        b = ord(s[j])
        b -= 97
        a[b] += 1
    print (a)

S = "abbddemmnnzzxtzy"
abc(S)
"""

# 8번
n = 0
while n != 9 :
    print ("1. 데이터 입력", end = "\n")
    print ("2. 데이터 탐색", end = "\n")
    print ("3. 데이터 출력", end = "\n")
    print ("9. 종료", end = "\n")
    n = int(input("메뉴 선택 : "))
    if n == 1 : print ("데이터 %s 선택", end = "\n")
    elif n == 2 : print ("데이터 %s 선택", end = "\n")
    elif n == 3 : print ("데이터 %s 선택", end = "\n")
    elif n == 9 : print ("종료합니다")
    else : print ("메뉴에서 골라주십시오.")