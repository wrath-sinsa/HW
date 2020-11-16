"""
def Bubblesort(a) :
    n = len(a)
    for i in range (n-1, -1, -1) :
        for j in range (i) :
            if a[j] > a[j+1] :
                a[j+1],a[j] = a[j],a[j+1]
    return a

A = [5,4,3,2,1]
Bubblesort(A)

import random, time
N = 3000
a = []
b = []
a.append(-1)
for i in range (1, N+1) :
    a.append(i)
for j in range (N, 0, -1) :
    b.append(j)
start_time = time.time()
c = Bubblesort(a)
finish = time.time() - start_time
print(finish)
start_time2 = time.time()
d = Bubblesort(b)
finish2 = time.time() - start_time2
print(finish2)
"""
# N * M 행렬 만들기
import random

def inputmatrix(N, M) :
    a = []
    for i in range (N) :
        a.append([random.randint(0,3)])
        for j in range (M-1) :
            a[i].append(random.randint(0,3))
    print (a)
    return a

# A를 행렬으로 출력
def printmatrix(A):
    N = len(A)
    M = len(A[0])
    for i in range (N) :
        for j in range (M) :
            print (A[i][j], end=" ")
        print ("\n")
        

N = 2
M = 3


printmatrix(inputmatrix(N,M))