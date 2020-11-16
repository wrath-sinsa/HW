# 1번
"""
def everySearch(t, p) :
    a = len(t)
    b = len(p)
    for i in range (a-b+1) :
        if t[i] == p[0] :
            strg = ""
            for j in range (b) :
                strg += t[i]
                i += 1
            i -= b 
            if stringSearch(strg, p) == 1:
                print("패턴을 발견한 위치 : %d"%i)
    print ("문자열 탐색 완료")

def stringSearch(t, p) :
    a = len(t)
    for i in range (a) :
        if t[i] != p[i] :
            return False
    return True



a = "A lover asked his beloved, Do you love yourself more than you love me?"
b = "love"

everySearch(a, b)
"""

# 2번
def rotate(a, k) : #리스트 a 회전 k
    for i in range (k) :
        for j in range (len(a)-1, 0, -1) : 
            a[j], a[j-1] = a[j-1], a[j]
            print (a)
    return a


a = int(input("원소의 개수 : "))
b = int(input("회전수 : "))
A = list(range(1,a+1))
print("원래 리스트 :", A)
B = rotate(A, b)
print ("회전리스트 :", B)