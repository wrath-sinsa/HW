"""
def lngseq(num) :
    s = set()
    n = len(num) 
    max_len = 0
    max_list = []
    for i in range (n) :
        m = num[i]
        cnt_list = [m]
        left = m - 1
        right = m + 1
        cnt = 1
        while left in num :
            s.discard(left)
            cnt_list.append(left)
            left -= 1
            cnt += 1
        while right in num :
            s.discard(right)
            cnt_list.append(right)
            right += 1
            cnt += 1
        cnt_list.sort()
        if cnt > max_len :
            max_len = cnt
            max_list = cnt_list
    return (max_len, max_list)

from random import randint

N = int(input("난수의 개수 입력 : "))
a = []
for i in range (N) :
    a.append(randint(1,N)) 
print (a)
b = lngseq(a)
print (b)
"""
"""
def srtlst(num) :
    i = len(num)
    max_len = 1
    while i != 0 :
        m = num[i-1]
        left = m - 1
        cnt = 1
        num.remove(m)
        while num.count(left) != 0 :
            num.remove(left)
            cnt += 1
            left -= 1
        if cnt > max_len :
            max_len = cnt
        i = len(num)
    return max_len

def strlst2(num) :
    max_len = 1
    n = len(num)
    for i in range (num[0], num[n - 1]) :
        cnt = 1
        while num.count(i) == 1 :
            cnt += 1
            i += 1
        if cnt > max_len :
            max_len = cnt
        return max_len


from random import randint

N = int(input("난수의 개수 입력 : "))
a = []
for i in range (N) :
    x = randint(1,N)
    if a.count(x) == 0 :
        a.append(x)
a.sort()
print (a)
b = srtlst(a)
print (b)
"""
def merge(r1, r2) :
    m = len(r1)
    n = len(r2)    
    i = 0
    j = 0
    res = []
    while i < m and j < n :
        if r1[i] < r2[j] :
            res.append(r1[i])
            i += 1
        elif r1[i] > r2[j] :
            res.append(r2[j])
            j += 1
        else :
            res.append(r2[i])
            res.append(r2[j])
            i += 1
            j += 1
    print (i, j)
    if i == m :
        while j < n :
            res.append(r2[j])
            j += 1
    elif j == n :
        while i < m :
            res.append(r1[i])
            i += 1
    return res


from random import randint

a = int(input("첫 번째 리스트의 원소 개수 입력 : "))
b = int(input("두 번째 리스트의 원소 개수 입력 : "))
A = []
B = []
for i in range (a) :
    A.append(randint(1,100))
for j in range (b) :
    B.append(randint(1,100))
A.sort()
B.sort()
print (A, B)
C = merge(A, B)
print(C)