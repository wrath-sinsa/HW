"""
def sum_average(a, b, c):
    sum_int = a + b + c
    average_int = sum_int / 3
    return (sum_int, average_int)

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
result = sum_average(a, b, c)
print('합 = %d, 평균 = %.2f'%(result[0], result[1]))
"""

"""
def maxMin(l) :
    min = l[0]
    for i in range (1, len(l)) :
        if min > l[i] :
            min = l[i]
    max = l[0]
    for j in range (len(l)-1) :
        if max < l[j] :
            max = l[j]
    return (min, max)



from random import randint

N = int(input("N = "))
a = []
for i in range (10) :
    a.append(randint(1,N))
print (a)
b = maxMin(a)
print ("최소 : %d , 최대 : %d" %(b[0],b[1]))
"""
"""
def len_a(a) :
    max_len = 1
    max_list = []
    for i in range (1, len(a)+1):
        if i in a :
            count_list = []
            count_list.append(i)
            count = 1
            left = i - 1
            right = i + 1
            while left in a :
                a.remove(left)
                count_list.append(left)
                left -= 1
                count += 1
            while right in a :
                a.remove(right)
                count_list.append(right)
                right += 1
                count += 1
            if count > max_len :
                max_len = count
                max_list = count_list
    print (max_len, max_list)
    return (max_len, max_list)



from random import randint

N = int(input("난수의 개수 입력 : "))
a = []
for i in range (N) :
    a.append(randint(1, N))
print (a)
b = set (a)
print (b)
c = len_a(b)
print ("최장 연속 순차의 길이 : %d \t \
    최장 연속 순차 : %li"%(c[0], c[1]))
"""
def Sequence(A) :
    Seq = set(A)
    print (Seq)
    max_len = 1
    max_list = []
    for i in range (len(A)) :
        m = A[i]
        left = m - 1
        right = m + 1
        count = 1
        count_list = [m]
        while left in Seq :
            Seq.remove(left)
            count_list.append(left)
            count += 1
            left -= 1 
        while right in Seq :
            Seq.remove(right)
            count_list.append(right)
            count += 1
            right += 1
        if count > max_len :
            max_len = count
            max_list = count_list
            max_list.sort()
    return (max_len, max_list)


from random import randint

N = int(input("난수의 개수 입력 : "))
a = []
for i in range (N) :
    a.append(randint(1,N))
print (a)
b = Sequence(a)
print (b)
