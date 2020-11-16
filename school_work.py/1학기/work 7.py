def printMatrix(m) :
    for i in range (len(m)) :
        for j in range (len(m[i])) :
            print (m[i][j], end =" ")
        print ("\t")

def addMatrix(m, n) :
    for i in range (len(m)) : 
        for j in range (len(m[i])) :
            print (m[i][j] + n[i][j], end = " ")
        print ("\t")


A = [[1,2,3], [3,2,1], [4,5,6]]
B = [[4,5,6], [4,3,2], [2,1,3]]

printMatrix(A)

printMatrix(B)

addMatrix(A, B)