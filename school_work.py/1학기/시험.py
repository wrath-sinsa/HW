# 1번 모르겠음 ㅅㅂ
"""
def makeString(c) :
    for i in range (4) :
        A = c[i] + 48
        B = chr (A) 
    lst.append(B)
    return lst

A = int(input("A = "))
B = int(input("B = "))
C = A + B
print ("A + B = %d"%(C))
D = makeString(C)
print (D)
"""

# 2번
"""
def exchangeMatrix(a) :
    c1 = 0
    c2 = 0
    for i in range (len(a)) :
        for j in range (len(a)) :
            if i > j :
                if a[i][j] == a[j][i] :
                    c1 += 1
                else :
                    a[i][j], a[j][i] = a[j][i], a[i][j]
                    c2 += 1
    return (c1, c2, a)
            

def makeMatrix(n) :
    lst = []
    for i in range (n) :
        lst1 = []
        for j in range (n) :
            if i == j :
                lst1.append(0)
            else :
                lst1.append(randint(0,1))
        lst.append(lst1)
    return lst

def printMatrix(a) :
    for i in range (len(a)) :
        for j in range (len(a)) :
            print (a[i][j], end = " ")
        print ("")

from random import randint

N = int(input("N = "))
A = makeMatrix(N)
printMatrix (A)
B = exchangeMatrix(A)
print ("대칭인 원소의 개수 : %d"%B[0])
print ("대칭인 원소의 개수 : %d"%B[1])
printMatrix(B[2])
"""
# 3번
"""
def emailSearch(t, p) :
    t[p:]    





def stringSearch(t, p, i):
    j = 0
    N = len(t) 
    M = len(p) 
    while i < N and j < M:
        if t[i] != p[j]:   
            i = i - j 
            j = -1
        i += 1
        j += 1
    if j == M : 
        return i - M
    else : 
        return i

fin = open("email.txt", "r")
line = fin.readline()
while line:
    A = stringSearch(line, "mailto:", '\"')
    emailSearch(line, "mailto:")
    print(line, end="")
    line = fin.readline()
fin.close
"""
# 4번
def makeNumbers(S) :
    lst = []
    a = ""
    for i in range (len(S)) :
        if isNumber(S[i]) == 1 :
            a += S[i]
        elif isNumber(S[i]) != 1 :
            s = makeNum(a)
            lst.append(s)
            lst.append(S[i])
            a = ""
        if i == len(S) - 1 :
            s = makeNum(a)
            lst.append(s)
    return lst

def makeNum (x) :
    s = 0
    for j in range (len(x)) :
        k = ord(x[j]) - 48
        s *= 10
        s += k
    return s

def isExpression(s): 
    for i in range(len(s)): 
        if not (isNumber(s[i]) or s[i] == '+' or s[i] == '-'): 
            return False
    return True

def isNumber(s): 
    if ord(s) >= 48 and ord(s) <= 57: 
        return True
    else: 
        return False

def evalList(a): 
    while len(a) > 1:
        if a[1] == '+': 
            res = a[0] + a[2] 
        elif a[1] == '-': 
            res = a[0] - a[2] 
        a.pop(0) 
        a.pop(0) 
        a.pop(0) 
        a.insert(0, res) 
    return a[0] 

S = input("S = ")
while isExpression(S) != 1 :
    print ("숫자와 +, - 기호만 입력 가능합니다.")
    S = input("S = ")

A = makeNumbers(S)
print("수식리스트 :", A)
B = evalList(A)
print ("계산 결과 :", B)