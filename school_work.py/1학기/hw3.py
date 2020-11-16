N = int(input("N 입력 : "))
a = list (range (N+1))
a[1]=a[0]
b = [2,3,5,7,11,13]
for i in range (0,len(b)):
    # c = int (N / b[i])
    # for j in range (2,c+1):
    #     a[b[i]*j]=a[0]
    j = 2
    while N >= b[i]*j:
        a[b[i]*j]=a[0]
        j += 1
while a.count(0) != 0 :
    a.remove(0)
print (a)
print (len(a))