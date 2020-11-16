# 1번 a의 약수 구하기

# a = int(input("a = "))
# i = 1
# while a/2 >= i :
#     if a % i == 0 :
#         print (i)
#     i += 1
# print (a)

# 2번 a와 b의 최대공약수 구하기

# a = int(input("a = "))
# b = int(input("b = "))
# i = 1
# if a > b : a,b = b,a
# while a/2 >= i :
#     if a % i== 0 and b % i == 0 :
#         c = i
#     i += 1
# if a % b == 0 : 
#     c = a
# print (c)

# 3번 유클리드 호제법으로 a와 b의 최대공약수 구하기

# a = int(input("a = "))
# b = int(input("b = "))
# if a < b : a,b = b,a
# while a != 0 and b != 0 :
#     a = a % b
#     print (a)
#     if a != 0 :
#         b = b % a
#         print(b)
# if a == 0 : a,b =b ,a
# print (a)

# 4번 자연수 a와 b의 최소공배수 구하기

# a = int(input("a = "))
# b = int(input("b = "))
# A,B = a,b
# while A != B:
#     if A>B : B += b
#     else : A += a
# print (A)

# 5번 a, b, c의 최소공배수 구하기

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a < b : a,b = b,a
# if a < c : a,c = c,a
# A = a
# while A % b != 0 or A % c != 0 :
#     A += a
# print (A)

# 6번 자연수 N을 입력 받아, 출력하기

# N = int(input("N : "))
# a = 1
# b = 1

# while N >= b : 
#     for i in range (a) :
#         if N >= b :
#             print (b, end =" ")
#             b = b+1
#     print ("\t")
#     a = a + 1


# 7번 자연수 a의 완전수, 과잉수, 부족수를 판별하는 함수
# def isPerfect(a) :
#     i = 1
#     j = 0
#     while a/2 >= i :
#         if a % i == 0 :
#             j += i
#         i += 1
#     if j == a :
#         return 1
#     elif j > a :
#         return 2
#     else :
#         return 3

# while True:
#     N = int(input("N : "))
#     if isPerfect(N) == 1 :
#         print ("완전수")
#     elif isPerfect(N) == 2 :
#         print ("과잉수")
#     else : print ("부족수")

# N = int(input("N = "))
# print (isPerfect(N))

# 8번 자연수 a의 소수여부를 판별하는 함수

# def isPrime(a) :
#     i = 1
#     j = []
#     j.append(a)
#     while a/2 >= i :
#         if a % i == 0 :
#             j.append(i)
#         i += 1
#     if len(j) == 2 :
#         return "소수"
#     else :
#         return "소수 아님"

# N = int(input("N = "))
# print (isPrime(N))

# 9번 에라토스테네스의 체 2부터 N사이의 소수 출력 함수

# def erathos(n) :
#     a = list(range(n+1))
#     a[1] = a[0]
# 
#     for i in range (0,len(b)) :
#         j = 2  
#         while n >= b[i] * j :
#             a[b[i]*j]=a[0]
#             j += 1
#     while a.count(0) != 0 :
#         a.remove(0)
#     print (a)

# N = int(input("N = "))
# erathos(N)
    
# 10번 자연수 a의 계승을 계산 함수

# def fact(a):
#     A = a
#     while a >= 2 :
#         a -= 1
#         A *= a
#     print (A)

# N = int(input("N = "))
# fact(N)    

# 11번 n개의 파보나치 수 출력 함수

# def fib(n) :
#     n1 = 1
#     n2 = 1
#     print (n1)
#     print (n2)
#     a = n - 2
#     while a > 0 :
#         n1 = n1 + n2
#         a -= 1
#         print (n1)
#         if a > 0 :
#             n2 = n1 + n2
#             print (n2)
#             a -= 1

# N = int(input("N = "))
# fib(N)

# 12번 a, x, e를 입력 받아 항(term)의 값을 계산하는 함수

# def evalTerm(a, x, e) : 
#     A = 1
#     for i in range (e) :
#         A *= x
#         print (A)
#     A *= a
#     print (A)

# evalTerm(4,2,3) 

# 14번 N개 정수로 이루어진 리스트 a를 버블 정렬 기법을
# 이용하여 정렬하는 함수

# def bubbleSort(lis) : 
#     a = len(lis)
#     for b in range (a) :
#         for i in range (a-1) :
#             if lis[i] > lis[i+1] :
#                 lis[i+1], lis[i] = lis[i], lis[i+1]
#         a -= 1
#     print (lis)
    
# A = [5,2,5,6,7,1,2]
# bubbleSort(A)       




        
