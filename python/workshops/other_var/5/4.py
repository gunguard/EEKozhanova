# Какой процент от общего количества слов не оканчивается знаком препинания (можно взять только запятую и точку)
words = []
s = 0
f = open('text.txt', 'r', encoding='utf-8')
for word in f.read().split():
    if word.endswith('.') or word.endswith(','):
        s += 1
    words.append(word)
f.close
s = len(words) - s
res = s / len(words) * 100
print(res)