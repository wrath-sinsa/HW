# 1. 에라토스테네스의 체 프로그램 실행시간
def erathos(N) :
    a = list(range(N+1))
    a [1] = 0
    i = 2
    while i <= N/2 :
        j = 2
        while N > i * j :
            a [i*j] = 0
            j += 1
        i += 1
    while a.count(0) != 0 :
        a.remove(0)
    print (len(a), "개의 소수 발견")

from time import time


N = int(input("2 이상의 자연수 입력 : "))
start = time()
erathos (N)
finish = time() - start
print ("실행시간", finish)

def erathos2(N) :
    a = list(range(N+1))
    a [1] = 0
    i = 2
    while N/2 >= i :
        j = 2
        if a[i] != 0 :
            j = 2
            while N > i * j :
                a [i*j] = 0
                j += 1
        i += 1
    while a.count(0) != 0 :
        a.remove(0)
    print(len(a), "개의 소수 발견")

from time import time
N = int(input("2이상의 자연수 입력 : "))
start = time()
erathos2 (N)
finish = time() - start
print ("실행시간", finish)