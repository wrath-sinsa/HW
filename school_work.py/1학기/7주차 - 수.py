# print(ord(" "))
# print(chr(32))

# c = ord("A") -1
# print(c)
# s = ""
# for i in range (26) :
#     c += 1
#     print (c)
#     s += chr(c)
#     print(s)

"""
def makeNum(x) :
    b = 0
    for i in range (len(x)) :
        a = ord(x[i]) - 48
        b *= 10
        b += a
    return b

a = input("a = ")
b = input("b = ")
print ( makeNum(a) + makeNum(b) )
"""


"""
def incipher(c, k) :
    d = ""
    for i in range (len(c)) :
        a = ord(c[i])
        if a == 32:
            a -= 32
            a += 123
        a -= k
        if a == 96:
            a -= 96
            a += 32
        elif a < 96 :
            a += 26
            a += 1
        d += chr(a)
    print(d)
    return d

def decipher(c, k) :
    d = ""
    for i in range(len(c)) :
        a = ord(c[i])
        if a == 32 :
            a -= 32 
            a += 96
        a += k
        if a == 123 :
            a -= 123
            a += 32
        if a > 123 :
            a -= 26
            a -= 1
        d += chr (a)
    print (d)
    return d

k = int(input("k = "))

decipher("attack safe zone", k)
incipher(decipher("attack safe zone", k), k)

decipher("abc xyz", 3)
incipher(decipher("abc xyz", 3), 3)
"""

# import datetime

# print(datetime.date.today())
# d = datetime.date.today()
# print(d.year)

# from datetime import date
# datetime이라는 모듈에서 date만 갖고 옴

# print(date.today())
# print(datetime.now())

# import random
# print(random.randint(0,1000))
# print(random.randrange(0,7))
# A = [1,2,3,5,6,7,3]
# print (A)
# random.shuffle(A)
# print(A)
# B = ["짜장", "짬뽕", "탕수육"]
# print(random.choice(B))

import random

def castDice(N) :
    b = []
    c = 0
    for i in range (N) :
        b.append(0)
    for j in range (N) :
        c = random.randint(1,6)
        b[j] = c
    for k in range (1,7) :
        d = b.count(k)
        print ((d/N)*100,"%")
castDice(10000)
