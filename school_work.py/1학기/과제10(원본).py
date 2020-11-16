"""
def stringSearch(t, p) : #t:텍스트,p:패턴
    n = len(t)
    m = len(p)
    for i in range (n-m+1) : ## 패턴보다 길때 제거
        print (i)
        if t[i] == p[0] :
            j = 0
            print (j)
            while j < m :
                if t[i] == p[j] :
                    i += 1
                    j += 1
                    print (i,j)
                else : j += m # 패턴 틀릴경우 while 문탈출
                if j == m :
                    i -= j
                    print (i ,"패턴 발견")
                    
print (len(a), len(b))
c = a.find(b)
while 0<= c < len(a) :
    print (c, end= " ")
    c = a.find(b, c+1)
    if c == -1 : break
stringSearch(a, b)
"""     
"""
a = "A lover asked his beloved, Do you love yourself more\
     than you love lmel"
b = "love"
"""
"""
def stringSearch2 (t, p) :
    j = 1
    for i in range (1, len(p)) :
        if t[i] == p[j] :
            j += 1
    if j == len(p) :
        print ("패턴 발견")

for i in range (len(a)) :
    if a[i] == b[0] :
        d = ""
        print (i)
        for j in range (len(b)) :
            d += a[i]
            i += 1
        print (d)
        stringSearch2 (d, b)
"""        

def rotate(a, k) : #리스트 a 회전 k
    for i in range (k) :
        for j in range (len(a)-1, 0, -1) : 
            a[j], a[j-1] = a[j-1], a[j]
            print (a)



a = [1, 2, 3, 4, 5]
b = 3 
rotate(a, b)