"""
def isDivisor(m,n):
    if m % n == 0:
        return True
    else :
        return False
        
a = int(input('a = '))
for i in range (1,a+1):
    if isDivisor(a, i):
        print(i, end=" ")
"""
"""
?def gcd(m,n):
    while m != 0 and n != 0:
        m , n = n , m % n
    return m

a = int(input("a = "))
b = int(input("b = "))
print("a와 b의 최대공약수는", gcd(a,b), "입니다.")
"""
"""
def lcm(m,n):
    M, N = m, n
    while M != N:
        if M > N:
            N += n
        else : M += m
    return M

a = int(input("a = "))
b = int(input("b = "))
print (lcm(a,b))
"""
"""
def isPerfect(m):
    n = 1
    o = 0
    while int(m/2) >= n:
        if m % n == 0:
            o += n
        n += 1
    if o == m :
        return m

a = int(input('a = '))
for i in range (1,a+1):
    if isPerfect(i):
        print (i,end =" ")
"""
