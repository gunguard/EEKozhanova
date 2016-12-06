# Программа должна открыть частотный словарь в кодировке UTF-8 и корректно вывести на экран только строчки с союзами.

line = []
f = open('text.txt', 'r', encoding='utf-8')
for i in f:
    line = i.split(' | ')
    if line[1].startswith('союз'):
        print(line)
f.close()

# Программа должна распечатать через запятую все существительные женского рода единственного числа, а также вывести на экран сумму их ipm.
line = []
line2 = []
line3=[]
f = open('text.txt', 'r', encoding='utf-8')
for i in f:
    line = i.split(' | ')
    line2 = line[1].split()
    if line2[0] == 'союз' or line2[0] == 'прл' or line2[0] == 'мест' or line2[0] == 'гл' or line2[0] == 'нар' or line2[
        0] == 'част' or line2[0] == 'межд' or line2[0] == 'предик' or line2[0]=='предл' or line2[0]=='ввод' or line2[0]=='числ' or line2[0]=='мод' or line2[0]=='дееп':
        continue
    if line2[2]=='мн' or line2[1]=='ед' or line2[1]=='мн':
        continue
    if line2[3] == 'муж' or line2[3] == 'ср' or line2[3] == 'общ':
        continue
    line3.append(line[0])
    line3.append(line[2])
print(line3)