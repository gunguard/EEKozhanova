#Программа должна печатать предложения, которые начинаются с гласных букв.
words = []
letter = []
word = ''
vowels = 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if len(line.split('. ')) > 1:
            words = line.split('. ')
        for w in words:
            print(w+"это элемент")
            #if len(w) >= 2:
            #if w[2] in vowels:
             #   print(w)
