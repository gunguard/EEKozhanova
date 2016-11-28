word = input('Введите слово: ')
word = word*2
for i in range(len(word)// 2):
    print( word[i:len(word) // 2+i])
