def inputPoly():
    A = int(input("지수 : "))
    B = int(input("계수 : "))
    lst = []
    a = set()
    while A >= 0 :
        lsta = []
        lsta.append(A)
        lsta.append(B)
        if A not in a :
            lst.append(lsta)
            a.add(A)
        else : print("같은 지수 값을 가지는 원소가 있습니다.")
        A = int(input("지수 : "))
        B = int(input("계수 : "))
    
    b = len(lst)
    if b == 0 : 
        print ("다시 입력 하십시오\n")
        return 0
    while b > 0 :
        for i in range (b-1) :
            if lst[i+1][0] > lst[i][0] :
                lst[i+1], lst[i] = lst[i], lst[i+1]
                print (lst)
        b -= 1 
    print ("종료\n다항식 리스트 : ", lst)
    return lst    


def printPoly(p):
    lng = len(p)
    for i in range (lng) :
        """
        if p[i][0] > 0 :   
            if p[i][0] == 1 :
                print ("%dx"%p[i][1], end = "")
            else :
                print ("%dx^%d"%(p[i][1],p[i][0]),\
                     end = "") 
            if i != lng - 1 : 
                print (" + ", end = "")
            else : print ("\n") 
        else : # 상수 일 경우
            print (p[i][1], end = "\n")                 
        """
        
        if p[i][0] > 1 and p[i][1] != 1 :
            print ("%dx^%d"%(p[i][1], p[i][0]), end = "")
        elif p[i][0] != 1 and p[i][1] == 1 : # 계수 1
            print ("x^%d"%p[i][0], end = "")
        elif p[i][0] == 1 and p[i][1] != 1 : # 지수 1
            print ("%dx"%p[i][1], end = "")
        elif p[i][0] == 1 and p[i][1] == 1: # 지수 1 계수 1
            print ("x", end = "")
        else : # 상수
            print (p[i][1])
        if i != lng - 1 :
            print (" + ", end = "")
    print ("\n")

                
def evalPoly(p, x):
    result = 0
    for i in range (len(p)) :
        A = 1
        for j in range (p[i][0]) : 
            A *= x
        A *= p[i][1]
        result += A
    return result


def addPoly(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b) :
        if a[i][0] > b[j][0] :
            c.append(a[i])
            i += 1
        elif a[i][0] < b[j][0] :
            c.append(b[j])
            j += 1
        else : 
            d = a[i]
            x = a[i][1] + b[j][1]
            d[1] = x
            c.append(d)
            """
            d = []
            d.append(a[i][0])
            print (a[i][1], a[j][1])
            x = a[i][1] + a[j][1]
            d.append(x) # [a[i][0],[x]]
            print (d)
            c.append(d)
            """
            i += 1
            j += 1
    while i < len(a) :
            c.append(a[i])
            i += 1
    while j < len(b) :
            c.append(b[j])
            j += 1
    print (c)
    return c


def multiplyPoly(a, b):
    lst = []
    for i in range (len(a)) :
        for j in range (len(b)) :
            c = [] 
            d = a[i][0] + b[j][0]
            e = a[i][1] * b[j][1]
            c.append(d)          
            c.append(e)
            lst.append(c)
    
    # 정렬
    lst2 = []
    lst2.append(lst[0])
    lst3 = []
    for i in range (1,len(lst) - 1) : # 최대, 최소 제외
        c = []
        d = lst[i][0]
        e = lst[i][1]
        for j in range (i+1, len(lst) - 1) :
            if lst[i][0] == lst[j][0] :
                e += lst[j][1]
                lst3.append(lst[j])
        if e != lst[i][1] :
            c.append(d)
            c.append(e)
            lst2.append(c)
        else : lst2.append(lst[i])
    if len(lst) != 1 :
        lst2.append(lst[len(lst) - 1 ])
    for i in range (len(lst3)) :
        lst2.remove(lst3[i])
    for i in range (1, len(lst2)) :
        for j in range (i + 1, len(lst2)) :
            if lst2[i] < lst2[j] :
                lst2[i], lst2[j] = lst2[j], lst2[i]
    return lst2

        ## 위는 안 줄어들게 해봤음.
    ## len(lst) 가 줄어듦에 따라 달라짐?? 왜달라지지?
"""
    m = 2
    for i in range (1, len(lst)-1) : # 정렬에 의해 최대, 최소 제외 가능
        j = m
        while j < len(lst) - 2 :
            print (i, j, lst[i][0], lst[j][0])
            if lst[i][0] == lst[j][0] :
                lst[i][1] = lst[i][1] + lst[j][1]
                lst.pop(j)
                print (lst, i, j, end = "\n\n")
            else : j += 1 
        m += 1
"""

"""    
    for i in range (1, len(lst)-1) : # 정렬에 의해 최대, 최소 제외함
        for j in range (i+1, len(lst)-1) :
            if lst[i][0] == lst[j][0] :
                print (lst, i, j, end = "\n\n")
                lst[i][1] = lst[i][1] + lst[j][1]
                lst.pop(j) 
            print (i,j)
    return lst
"""

m = 1
P = []
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) : '))
    if m == 1:
        print('다항식 입력 선택\n')
        P = inputPoly()
    elif m == 2:
        print('다항식 출력 선택\n')
        """
        A = [[5, 3], [2, 1], [1, 5], [0, 2]]
        printPoly(A)
        """
        printPoly(P)
    elif m == 3:
        print('다항식 계산 선택\n')
        """
        A = [[5, 3], [2, 1], [1, 5], [0, 2]]
        printPoly(A)
        X = int(input("X = "))
        result = evalPoly(A, X)
        print ("계산 결과 : ", result)
        """
        printPoly(P)
        X = int(input('X = '))
        result = evalPoly(P, X)
        print('계산 결과 : ', result)
    elif m == 4:
        print('다항식 덧셈 선택\n')
        """
        A = [[5, 3], [3, 5], [1, 4], [0, 2]]
        B = [[5, 7], [2, 4], [1, 7]]
        printPoly(A)
        printPoly(B)
        C = addPoly(A, B)
        printPoly(C)
        """
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = addPoly(A, B)
        printPoly(C)
    elif m == 5:
        print('다항식 곱셈 선택\n')
        
        A = [[5, 3], [3, 5], [1, 4], [0, 2]]
        B = [[5, 2], [2, 4], [1, 3]]
        printPoly(A)
        printPoly(B)
        C = multiplyPoly(A, B)
        printPoly(C)
        """
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = multiplyPoly(A, B)
        printPoly(C)
        """
    else:
        if m != 9:
            print('메뉴 선택 오류\n')