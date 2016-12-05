# Программа должна печатать предложения, которые начинаются с гласных букв.
words = []
letter = []
word = ''
vowels = 'АЕЁИОУЫЭЮЯ'
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        for item in words:
            if item[0] in vowels:
                print (line)
