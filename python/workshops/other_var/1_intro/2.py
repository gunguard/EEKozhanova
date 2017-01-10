# a умножить на b равно с
# c является решением линейного уравнения ax + b = 0
a = int(input())
b = int(input())
c = int(input())
if a * b == c:
    print('YES')
else:
    print('NO')
if a == 0:
    if b == 0:
        print('YES')
    else:
        print('NO')
else:
    if c == -b / a:
        print('YES')
    else:
        print('NO')
