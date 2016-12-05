#Программа должна печатать предложения, которые начинаются с гласных букв.
words = []
letter = []
word = ''
vowels = 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        for w in words:
            if w[0] in vowels:
                print(w)
#words=[]
#letter=[]
#vowels='АаЕеЁёИиОоУуЫыЭэЮюЯя'
#with open('file1.txt','r',encoding='utf-8') as f:
#    for line in f:
#        words=line.split()
#        word=words[0]
#        letter=word.split()
#        if letter[0] in vowels:
#           print(line)