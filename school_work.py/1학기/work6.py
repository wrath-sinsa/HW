"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
C = c
while C % a != 0 or C % b != 0:
    C += c
print (C)
"""
"""
def function(x):
    if x % 2 == 1:return 1
    else: return 0

N = int(input("자연수 N 입력 : "))
for x in range(1,N+1):
    if function(x): print(x, end=" ")
"""

def power(x, y):
    res = 1
    for i in range(y):
        res *= x
    return res

a = int(input("a = "))
b = int(input("b = "))
result = power(a,b)
print (result)

# def max3(x, y, z):
#     if x>y :
#         x,y = y,x
#     if y>z :
#         y,z = z,y
#     return z

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# maxval = max3(a, b, c)
# print("최대값은 " , maxval , "입니다.")