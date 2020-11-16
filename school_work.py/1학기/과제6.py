# 1. perfect(n) 완전수1, 과잉수2, 부족수3 판별
"""
def perfect(n) :
    s = 0
    for i in range (1, int(n/2)+1) : # n/2 까지
        if n % i == 0 : 
            s += i
    if s > n : return 2 # 과잉수
    elif s < n : return 3 # 부족수
    else : return 1 # 완전수 s == n

while True :
    N = int(input("자연수 입력 : "))
    a = perfect(N)
    if a == 2 : print("과잉수")
    elif a == 3 : print("부족수")
    else : print("완전수")
"""

# 2. 3x3 행렬 생산, 행렬 덧셈
"""
def printMatrix(m) :
    for i in range (len(m)) :
        for j in range (len(m[i])) : 
            print (m[i][j], end = " ")
        print ("\n")


def addMatrix(m, n) : 
    for i in range (len(m)) : 
        for j in range (len(m[i])) :
            print (m[i][j] + n[i][j], end = " ")
        print ("\n")

A = [[1,2,3], [3,2,1], [4,5,6]]
B = [[4,5,6], [4,3,2], [2,1,3]]

printMatrix(A)
printMatrix(B)
addMatrix(A, B)
"""