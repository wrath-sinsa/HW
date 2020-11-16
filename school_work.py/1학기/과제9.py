def encipher (p, k) : #p는 암호 k는 변화수
    a = ""
    for i in range (len(p)) :
        b = ord(p[i])
        if b == 32 : # 빈공간 일경우
            b = 64
            b += k
        elif 64 < b < 91 :
            b += k
            if b >= 91 :
                b -= 90
                b += 96
        elif 96 < b < 123 :
            b += k
            if b >= 123 :
                b -= 122
                b += 31
                if b >= 33 :
                    b -= 32
                    b += 64
        a += chr(b)
    return a

def decipher (q, k) :
    a = ""
    for i in range (len(q)) :
        b = ord(q[i])
        if b == 32 :
            b = 123
            b -= k
        elif 96 < b < 123 :
            b -= k
            if b <= 96 :
                b -= 97
                b += 91
        elif 64 < b < 91 :
            b -= k
            if b <= 64 :
                b -= 65
                b += 33
                if b <= 31 :
                    b -= 32
                    b += 123
        a += chr(b)
    return a


K = int(input("K = "))
A = "Abc xyZ aBC XYz"
print ("평문 :", A)
B = encipher (A, K)
print ("암호문 :", B)
C = decipher (B, K)
print ("복호화된 평문 :", C)