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

def mklst(n) :
    lst1 = []
    for i in range (n) :
        lst1.append(randint(1,10*n))
    print (lst1)
    lst2 = []
    lst3 = []
    if n % 2 == 0 :
        a = int(n/2)
    else : a = int(n/2) +1
    print (a)
    for i in range (a) :
        lst2.append(lst1[i])
    for i in range (a) :
        lst1.pop(0)
    for j in range (len(lst1)) :
        lst3.append(lst1[j])
    lst2.sort()
    lst3.sort()
    return (lst2, lst3)
"""
from random import randint
a = mklst(10)
print (a)
b = merge (a[0], a[1])
print (b)
"""
def mkrun(n) :
    lst = []
    for i in range (n) :
        lst.append (randint(1,100))
    print (lst)
    ntr = []
    while len(lst) != 0 : 
        j = 0 # 리스트 담기
        a = []
        a.append(lst[j])
        if j < len(lst) - 1 :
            while lst[j] < lst[j+1] :
                a.append(lst[j+1])
                if j != len(lst) - 1 :
                    j += 1
        print (a)
        ntr.append(a)
        for i in range (j+1) : 
            lst.pop(0)
        print(lst)
    print (ntr)
    m = len(ntr)
    for i in range (m) :
        print ("run%d : %li"%(i+1, ntr[1]))
    
"""
from random import randint 
mkrun(20)
"""
def lwhgh(nums, key) :
    low = 0
    high = len(nums) - 1
    while low <= high :
        print ("low : ", low, "high : " ,high)
        mid = int((low+high) / 2)
        print ("mid : " , mid)
        if nums[mid] < key :
            low += 2
            print ("%d < %d"%(nums[mid], key))
        elif nums[mid] > key :
            high -= 2
            print ("%d > %d"%(nums[mid], key))
        else : return mid
    return -1

def lwhgh(nums, key) :
    low = 0
    high = len(nums) - 1
    mid = int((low+high) / 2)
    print ("low : ", low, "high : " ,high)
    if nums[mid] < key :
        print ("mid : " , mid)
        print ("%d 번째 원소 %d < 탐색키 %d"%(mid+1, nums[mid], key))
        while nums[mid] < key and mid < len(nums) -1 :
            low += 2
            mid = int((low+high) / 2) 
            print ("low : ", low, "high : " ,high)
            print ("mid : " , mid)
            if nums[mid] > key :
                print ("%d 번째 원소 %d > 탐색키 %d"%(mid+1, nums[mid], key))
            else :
                print ("%d 번째 원소 %d < 탐색키 %d"%(mid+1, nums[mid], key))
    elif nums[mid] > key :
        print ("mid : " , mid)
        print ("%d 번째 원소 %d > 탐색키 %d"%(mid+1, nums[mid], key))
        while nums[mid] > key and mid > 0 : 
            high -= 2
            mid = int((low+high) / 2)
            print ("low : ", low, "high : " ,high)
            print ("mid : " , mid)
            if nums[mid] < key :
                print ("%d 번째 원소 %d < 탐색키 %d"%(mid+1, nums[mid], key))
            else : 
                print ("%d 번째 원소 %d > 탐색키 %d"%(mid+1, nums[mid], key))
    else : return mid
    return -1

from random import randint
N = int(input("데이터의 개수 입력 : "))
a = []
for i in range (N) : 
    a.append(randint(1,4*N))
a.sort()
print(a)
M = int(input("탐색 키 입력 : "))
b = lwhgh (a, M)
if b == -1 :
    print ("탐색 키와 동일한 원소가 없습니다")
else : print ("리스트의 %d 번째 위치에서 탐색 \
    키와 동일한 원소 발견" %b)