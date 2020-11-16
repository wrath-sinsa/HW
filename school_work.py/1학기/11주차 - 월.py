"""
def twoSum(num, t): # list[num], t는 구하고 싶은 상수
    n = len(num)
    for i in range (n) :
        j = i + 1
        while j < n :
            if t == num[i] + num [j] :
                print (i+1,"번째 원소와", j+1,"번째 원소")
            j += 1
         
from random import randint

a = []
N = int(input("N = "))
M = int(input("M = "))
for i in range (N) :
    a.append(randint(1,2*N))
print (a)
twoSum(a, M)
"""
# set()형 배우기
"""
# def ABC() :


from random import randint
a = []
N = int(input("N = "))
for i in range (N) :
    a.append(randint(1,2*N))
print (a)
b = set(a)
print (b)
"""
#집합에 없는 원소 구하기
def Isin(A, N) :
    b = []
    for i in range(1, N) :
        if i not in A :
            b.append(i)
    for j in range(len(b)) :
        print (b[j],end=" ")

from random import randint
a = []
N = int(input("N = "))
for i in range (N) :
    a.append(randint(1,N))
print (a)
b = set(a)
print(b)
Isin(b, N)
