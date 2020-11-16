def back(a):
    b = ""
    for i in range(0,len(a)) : 
        if a[i].isalpha() :
            b += a[i]
    b = b.lower()
    print(b)
    return b
            
def ishm(a):
    b = ""
    for i in range(1,len(a)+1) : 
        b += a[-i]
    print(a)
    print(b)
    if a == b :
        print ("회문입니다.")
    else :
        print ("회문이 아닙니다.")



# A = input("A = ")

A = "A man, a plan, a canal - Panama!"
B = "사전 사! 영한사전 사! 영영사전 사! 한영사전 사!"
C = "abcba"
ishm(back(A))
ishm(back(B))
ishm(C)