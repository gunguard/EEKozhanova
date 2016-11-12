# Программа должна спрашивать у пользователя слова до тех пор, пока он не введёт пустое слово.
# После этого программа должна вывести на экран все введённые слова, удалив в первом слове первый символ, во втором слове первые два символа, в третьем -- первые три символа и т.д. (каждое слово на отдельной строчке).
words = []
validation = False
numberofword = 0
while validation == False:
    print('Введите слово : ')
    s = input()
    numberofword = numberofword + 1
    if s == "":
        validation = True
    else:
        if numberofword < (len(s)):
            s = s[(numberofword):]
        else:
            s = ""
        words.append(s)
for i in range(len(words)):
    print(words[i])