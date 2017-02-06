def PrepText():
    f=open('text.txt','r',encoding='utf-8')
    s=f.read().split()
    words=[]
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"“()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words
a=PrepText()
print(a)


def PrepText():
    f=open('text.txt','r',encoding='utf-8')
    s=f.readlines()
    words=[]
    for n in s:
        words.append(n)
    f.close
    return words


random_adjective = 'маня'
random_adjective = random_adjective.replace('ня', 'ый')
print(random_adjective)
#РАБОТАЕТ

s = 'spameggs'
s = s[0:len(s)-2]
print(s)
#РАБОТАЕТ, НО БОЛЕЕ НЕУДОБНО, ПОТОМУ ЧТО ОКОНЧАНИЕ ВАРИАТИВНО

import random

def hui():
    words = [1,2,3,4,5,6]
    return random.choice(words), 1

r=hui()
n=r[1]
print(r[0],r[1])

def givingnoun():
    r=hui()
    return r[0]


def givingtype():
    r=hui()
    return r[1]


def mamka():
    r=givingtype()
    n=givingnoun()
    return givingnoun()
print(givingnoun())
print(mamka())

l='мамкатвоя'
if l.endswith('оя'):
    print(l)
