words=[]
n=0
while n==0:
    print ('Введите число: ')
    s=input()
    if s=="":
        n=1
    else:
        words.append(s)
for i in range(len(words)-1, -1, -1):
    print(words[i])
