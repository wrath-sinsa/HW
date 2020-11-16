# 1 <= k <= 26
def encipher(p, k) :
    q = ""
    for i in range (len(p)) :
        a = ord(p[i])
        if a == 32 :
            a = 64
            a += k
            q += chr (a)
        elif 64 < a < 91 :
            a += k
            if a >= 91 :
                a -= 90
                a += 96 # a += 6
            q += chr (a)
        elif 96 < a < 123 :
            a += k
            if a >= 123 :
                a -= 122
                a += 31
                if a >= 33 :
                    a -= 32
                    a += 64  
            q += chr (a)  
    return q

def decipher (c, k) :
    d = ""
    for i in range (len(c)) :
        a = ord(c[i])
        if a == 32 :
            a = 123
            a -= k
            d += chr (a)
        elif 96 < a < 123 :
            a -= k
            if a <= 96 :
                a -= 97
                a += 91
            d += chr (a)
        elif 64 < a < 91 :
            a -= k
            if a <= 64 :
                a -= 65
                a += 33
                if a <= 31 :
                    a -= 32
                    a += 123
            d += chr (a)
    return d
        

K = int(input("K = "))
A = "Abc xyZ aBC XYz"
B = encipher (A, K)
decipher (B, K)


# 1 <= k <= 53