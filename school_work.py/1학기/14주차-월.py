
h = int(input("높이 h = "))
blnk = " "
lst = []
pre = [1]
lst.append(pre)
for i in range (h) :
    tem = [1]
    for i in range (len(pre)-1) :
        tem.append(pre[i] + pre[i+1])
    tem.append(1)
    lst.append(tem)
    pre = tem
for i in range (len(lst)) :
    print (blnk * ( h * 2 ), end = "")
    for j in range (len(lst[i])) :
        print (lst[i][j],end = "   ")
    print ("\t")
    h -= 1    

"""
h = int(input("높이 h = "))
res = []
pre = [1]
res.append(pre)
for i in range (h) :
    # 
    cur = [1]
    for j in range (len(pre)-1) :
        cur.append(pre[j] + pre[j+1])
    cur.append(1)
    # 
    res.append(cur)
    pre = cur
for i in range (len(res)) :
    for j in range (len(res[i])) :
        print (res[i][j],end = " ")
    print ("\t")
"""