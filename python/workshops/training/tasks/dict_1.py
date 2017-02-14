# Программа должна прочитать текст, создать частотный список слов в этом тексте, используя слова в качестве ключей словаря, а частотность в качестве значений.
# После этого нужно распечатать самое частотное слово в тексте.
# Найти среднее значение частотности слов в тексте.


def text():
    f=open('text.txt','r',encoding='utf-8')
    s=f.read().split()
    words=[]
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"“()[]=+-_#&@*{}|?/«»—'))
    f.close
    print(len(words))
    return words


def unique(n):
    match = {}
    for l in range(len(n)-1):
        for k in range(len(n)-1):
            if n[l] != n[k]:
                for i in match:
                    if n[l] == i:
                        break
                else:
                    match[n[l]] = 0
        match[n[l]] += 1
    print(len(match))
    print(match)
    return match


def max(m):
    for i in sorted(m):
        for n in sorted(m):
            if m[i]>=m[n]:
                s = i
            else:
                s = n
        break
    print(s)
    return s

# не очень красивый код, но работает вроде
max(unique(text()))