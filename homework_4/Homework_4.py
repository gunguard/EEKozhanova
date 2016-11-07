print('Введите слово: ')
S=str(input())
d=str('')
x=0
n=len(S)
for i in range(n):
    if S[n - i - 1] in '0123456789' or S[n - i - 1] in 'abcdefghijklmnopqrstuvwxyz' or S[n - i - 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('Неверный ввод.')
        x=1
        break
    if S[n-i-1] not in 'зяЗЯ':
        d=d+S[n - i - 1]
if x==0:
    print(d)