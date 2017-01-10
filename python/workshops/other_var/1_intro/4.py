# a и b в сумме дают с
# a разделить на b дают с
a = int(input())
b = int(input())
c = int(input())
if a + b == c:
    print('YES')
else:
    print('NO')
if b==0:
    print('NO')
else:
    if a / b == c:
        print('YES')
    else:
        print('NO')