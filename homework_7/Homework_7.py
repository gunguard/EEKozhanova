# Во сколько раз слов длины 3 больше, чем слов длины 1 (если слов длины 1 нет вообще, программа должна об этом сообщить).
words = []
word = []
s = 0
num = 0
res = 0
f = open('text.txt', 'r', encoding='utf-8')
for word in f.read().split():
    word = word.strip(',.!?')
    words.append(word)
    if len(word) == 3:
        s += 1
    elif len(word) == 1:
        num += 1
f.close
if num == 0:
    print('Слов длины 1 в тексте нет.')
else:
    res = s / num
    print('Слов длины 3 в', res, 'раза больше, чем слов длины 1.')
