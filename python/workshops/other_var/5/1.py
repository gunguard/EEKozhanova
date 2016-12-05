# Чему равно среднее число слов в строке.
words = []
j = 0
f = open('text.txt', 'r', encoding='utf-8')
for line in f.read():
    j += 1
    word = line.split()
    words.append(word)
f.close
print(j)
print(len(words))
j = j / len(words)
print(j)
print(len(words))
