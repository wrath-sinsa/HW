# 1번
"""
def twoSumSorted(a, n) :
    # i = 0 
    # while i < len(a) : 
    #     j = i + 1
    #     while j < len(a) :
    #         if a[i] + a[j] == n :
    #             print ("%d 번째와 %d 번째 원소"%(i+1, j+1))
    #         j += 1
    #     i += 1
    lst = []
    for i in range (len(a)) :
        for j in range (i+1, len(a)) :
            if a[i] + a[j] == n :
                lst1 = [i, j]
                lst.append(lst1)
    return lst 

from random import randint

N = int(input("리스트의 원소 개수 입력 : "))
a = []
for i in range(N) :
    a.append(randint(1,2*N))
a.sort()
print ("정렬된 리스트 :", a)
b = list (set(a))
print ("중복이 제거된 리스트 : ", b)
M = int(input("목표값 입력 : "))
print ("두 수의 합이 %d인 원소 쌍"%M)
A = twoSumSorted(b, M)
if len(A) != 0 :
    for i in range (len(A)) :
        print ("%d번째와 %d번째 원소"%(A[i][0]+1, A[i][1]+1))
else : print ("없음")
"""

# 2번
def multiplyMatrix(A, B) :
    a = []
    for i in range (len(A)) :
        b = []
        for m in range (len(B[0])) :
            s = 0
            for j in range (len(B)) :
                c = A[i][j] * B[j][m]
                s += c
            b.append(s)
        a.append(b)
    return a

def printMatrix(m) :
    for i in range (len(m)):
        for j in range (len(m[i])):
            print (m[i][j], end = " ")
        print ("\t")

def mkMatrix(a, b) :
    lst = []
    for i in range (a):
        ad = []
        for j in range (b):
            ad.append(randint(-3, 3))
        lst.append(ad)
    return lst

from random import randint
L = int(input("L = "))
M = int(input("M = "))
N = int(input("N = "))

A = mkMatrix (L, M)
B = mkMatrix (M, N)
print (A, B)
print ("행렬 A")
printMatrix(A)
print ("행렬 B")
printMatrix(B)
print ("행렬 C")
C = multiplyMatrix(A, B)
printMatrix (C)
