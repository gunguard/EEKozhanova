def PrepText(m):
    f=open(m,'r',encoding='utf-8')
    s=f.read().split()
    words=[]
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words


def countsyl(arr,n):
    voc = 'аеиуоюяыэ'
    for word in arr:
        num = 0
        for letter in word:
            if letter in voc:
                num+=1
        if num == n:
            print(word)
    return


def firstlet(arr,l):
    for word in arr:
        if word.startswith(l):
            print(word)
    return


def main():
    choice()


def choice():
    print('Если хотите распечатать слова с заданным количеством шагов, введите 1. Если хотите распечатать слова, начинающиеся с заданной буквы, введите 2.')
    n=int(input())
    if n==1:
        m=input()
        n=int(input())
        countsyl(PrepText(m),n)
    elif n==2:
        m=input()
        l=input()
        firstlet(PrepText(m),l)
        

main()
