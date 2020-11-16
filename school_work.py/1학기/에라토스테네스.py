import time

def erathos(N):
    start = time.time()
    a = list(range(N+1))
    a[1]=a[0]
    i = 2
    while N/2 >= i :
        j = 2 
        while N >= i * j :
            a[i*j] = a[0]
            j += 1
        i += 1
    while a.count(0) != 0 :
        a.remove(0)
    end = time.time() - start
    print ("실행시간" , end)
    print (len(a), "개의 소수 발견")

N = int(input("N : "))
erathos(N)
