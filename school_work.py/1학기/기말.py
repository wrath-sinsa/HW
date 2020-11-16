# 1.
"""
def isPrime(a) :
    i = 1
    j = []
    j.append(a)
    while a/2 >= i :
        if a % i == 0 :
            j.append(i)
        i += 1
    if len(j) == 2 :
        return True
    else :
        return False

def sumPrime(a) :
    p_sum = 0 # 비소수
    n_sum = 0 # 소수
    for i in range (len(a)) : 
        if isPrime(a[i]) == True : # 소수일경우
            n_sum += a[i]
        else :
            p_sum += a[i]
    return (p_sum, n_sum)


N = int(input("정수 입력(종료시는 999) : "))
a = []
while N != 999 :
    if N < 2 : 
        print ("2 이상의 수만 입력하세요.")
        N = int(input("정수 입력(종료시는 999) : "))
    elif N != 999 :
        a.append(N)
        N = int(input("정수 입력(종료시는 999) : "))
    else : 
        print("종료")
a = list(set(a))
print ("생성된 리스트 : ", a)
b = sumPrime(a)
print ("소수의 합 : %d\n비소수의 합 : %d"%(b[1], b[0]))
"""
# 2.
"""
def sumThree(a, n) :
    lst = []
    for i in range (int(n/3)):
        j = 3 * i
        s = 0
        for k in range (3) :
            s += a[j]
            j += 1
        lst.append(s)
    return lst

from random import randint

N = int(input("N = "))
a = []
for i in range (N):
    a.append(randint(1,5))
print ("a = " , a)
m = N % 3
if m != 0 :
    while m != 3 :
        a.append(0)
        m += 1
n = len (a)
b = sumThree(a, n)
print ("b = ", b)
"""
# 3.
"""
def makeMatrix(m):
    a = []
    for i in range(m) :
        b = []
        for j in range (m) :
            if i == j :
                b.append (0)
            else :
                b.append(randint(0, 3))
        a.append (b)
    return (a)

def printMatrix(a) :
    n = len(a)
    for i in range (n) :
        for j in range (n) :
            print(a[i][j], end = " ")
        print ("")

def subMatrix(a) :
    A = 0
    B = 0
    for i in range (len(a)) :
        for j in range (len(a[i])) :
            if j > i :
                A += a[i][j]
            else :
                B += a[i][j]
    return (A, B)



from random import randint

M = int(input("M = "))
a = makeMatrix(M)
printMatrix (a)
b = subMatrix (a)
print ("결과 : %d - %d ="%(b[0],b[1]), b[0]- b[1])
"""
# 4.
def isAtoj(s) : 
    for i in range (len(s)) :
        t = ord(s[i])
        if t < 97 or t >106 :
            return False
    return True

def makeNumber(s) :
    A = 0
    for i in range (len(s)) :
        A *= 10
        a = ord(s[i])
        a -= 97
        A += a
    return A

S1 = input("S1 = ")
while isAtoj(S1) == False :
    print ("a 부터 j 사이의 영문 소문자만 입력 가능합니다.")
    S1 = input("S1 = ")
s1 = makeNumber(S1)
S2 = input("S2 = ")
while isAtoj(S2) == False :
    print ("a 부터 j 사이의 영문 소문자만 입력 가능합니다.")
    S2 = input("S2 = ")
s2 = makeNumber(S2)

print ("%d + %d = "%(s1,s2), s1 + s2)