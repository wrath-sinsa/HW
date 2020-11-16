"""
b = []
a = int(input("정수 입력(종료시는 999) : "))
while a != 999:
    if b.count(a) != 1:
        b.append(a)
        #b.extend([a]) 
        # extend는 리스트[] 형식으로
    a = int(input("정수 입력(종료시는 999) : "))
print (b)
"""
"""
N = int(input("N = "))
m = int(input("m = "))
for m in range (0, N+1, m):
    if m != 0:
        print (m)
"""
"""
import time
N = int(input("자연수 N 입력 : "))
s = 0
start = time.time()
for i in range (1, N*N+1):
    s += i
end = time.time() - start
print ('합계 : ', s)
print ("실행시간 : ", end) 
"""

# a = int(input("2 이상의 자연수 입력 : "))
# while a <= 0 :
#     print (a , "는 2 이상의 자연수가 아닙니다.")
#     a = int(input("2 이상의 자연수 입력 : "))


# N = int(input ("N 입력 : "))
# a = list(range (N+1))
# a[1] = a[0]
# print (a)
# for i in range ()

def sosu(x):
    if x == 2:
        return x
    else :
        for i in range (1, int(x/2)+1):
            if x % i == 0:
                #print (i)
                y = i
        if y == 1 :
            #print (x , "는 소수")
            return x
        else :
            #print (x, "는 소수 아님")
            return 0
    
N = int(input ("N = "))
b = []
for a in range (2,N+1):
    b.append(sosu(a))
while b.count(0) != 0:
    b.remove(0)
print(b)
print(len(b))


# import time
# t = time.localtime()
# year = t [0]
# month = t [1]
# day = t [2]
# hour = t [3]
# print (year, month, day)
# print (time.localtime())

