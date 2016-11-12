# Программа должна спрашивать у пользователя слова до тех пор, пока он не введёт пустое слово.
# После этого программа должна вывести на экран все введённые слова, удалив в первом слове первый символ, во втором слове первые два символа, в третьем -- первые три символа и т.д. (каждое слово на отдельной строчке).
words = []
validation = False
while validation == False:
    print('Введите слово : ')
    s = input()
    if s == "":
        validation = True
    else:
        words.append(s)
for i in range(len(words)):
    if i + 1 < (len(words[i])):
        word = words[i]
        word = word[(i + 1):]
        words[i] = word
    else:
        words[i] = ""
for i in range(len(words)):
    print(words[i])