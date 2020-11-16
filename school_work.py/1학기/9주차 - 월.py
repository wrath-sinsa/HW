## input 텍스트에서 읽기(r)모드로 열기
## read() 는 전부읽음

# fin = open("input.txt", "r")
# text = fin.read()
# print("텍스트 : ", text)
# fin.close

## readline()은 한줄만 읽음
# fin = open("input.txt", "r")
# line = fin.readline()
# print(line, end = "")
# fin.close


## readline()을 3줄까지만 읽게하기
## 어떻게 적용되는거지??

# fin = open("input.txt", "r")
# for i in range (3):
#     line = fin.readline()
#     print(line, end= "")
# fin.close

## 끝까지 읽기 이것도 모르겠음.

# fin = open("input.txt", "r")
# line = fin.readline()
# while line:
#     print(line, end="")
#     line = fin.readline()
# fin.close

## output.txt 를 만들어서 (직접 안만들어도 만들어짐)
## 섭씨온도 >> 화씨온도 변환 후 출력
## 동시에 하면 왜 안될까?
"""
fout = open("output.txt", "w")
for c in range (0, 51, 4) : 
    f = c*9/5 + 32
    out = "섭씨 온도 : %d, 화씨온도 : %.1f\n" % (c, f)
    fout.write(out)
fout.close
"""

fin = open("output.txt", "r")
line = fin.readline()
while line:
    A = line.split(" ")
    print (A)
    print(line, end = "")
    line = fin.readline()
fin.close


##단어 별로 끊어서 리스트에 삽입
"""
def makeList(x) :
    a = x.split()
    print(a)
    return a


fin = open("input.txt", "r")
line = fin.readline()
while line:
    makeList(line)
    line = fin.readline()
fin.close
"""
## 탐색
## for 문에서 i를 썼다고 할때, i를 빼든 더하든 다시 값으로 돌아감
## 예를 들어 for i range (10)에 i += 2 , print (i)를 하면
## 0 > 2를 출력 1 > 3출력 ... 이런식.
## 그래서 while 써 봄
"""
def findx(a, x) : #a는 주어진 텍스트 x는 찾을거
    i = 0
    j = 0   
    while i < len(a) :
        # print (i, j)
        if a[i] == x[j] :
            j = 0
            while a[i] == x[j]:
                if j < len(x)-1 :
                    i += 1
                    j += 1
                    # print (j)
                else : 
                    i -= j
                    print (i , "번 째에서 발견")
                    # return 0
                    i += j+1
            if 0 < j < 5 :
                i -= j
                j = 0
        i += 1
    print ("패턴 발견하지 못함")

A = "A lover asked his beloved, Do you love yourself more than you love me"
B = "love"
findx(A, B)                    
"""



        
            
