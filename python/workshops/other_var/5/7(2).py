# Во сколько раз слов длины 3 больше, чем слов длины 1 (если слов длины 1 нет вообще, программа должна об этом сообщить).
words = []
s = 0
num = 0
res=0
f = open('text.txt', 'r', encoding='utf-8')
for word in f.read().split():
    word=word.strip(',.!?')
    words.append(word)
for i in range(len(words)):
    words.strip('.,?!')
    if len(words[i]) == 3:
        s += 1
    elif len(words[i]) == 1:
        num += 1
if num == 0:
    print('fuck you')
else:
    res=s/num
    print(res)

# Во сколько раз слов длины 3 больше, чем слов длины 1 (если слов длины 1 нет вообще, программа должна об этом сообщить).
words = []
s = 0
num = 0
res=0
f = open('text.txt', 'r', encoding='utf-8')
for word in f.read().split():
    word=word.strip(',.!?')
    words.append(word)
for i in range(len(words)):
    words.strip('.,?!')
    if len(words[i]) == 3:
        s += 1
    elif len(words[i]) == 1:
        num += 1
if num == 0:
    print('fuck you')
else:
    res=s/num
    print(res)
