word = input('Введите слово: ')
for i in range(len(word)):
    print(word)
    anotherword = word[1:len(word)] + word[0]
    word = anotherword
    anotherword = ''