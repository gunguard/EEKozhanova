# Для работы программы понадобится файл с разметкой из исландского корпуса. Размеченные тексты выстроены таким образом, что на одной строке располагается одна словоформа в следующем виде: <w lemma="til" type="ae">Til</w>.
# Морфологическая разметка даётся как последовательность символов внутри type="", где каждый символ кодирует определённый грамматический показатель. Что значат эти показатели, написано в отдельном pdf-файле .

# 1. (5 баллов) Открыть файл с корпусом, подсчитать в нём число строк; открыть другой файл для записи, записать туда число строк, найденных в файле с корпусом.

# 2. (8 баллов) Создать словарь, в котором ключами являются строки с морфологическим разбором слов (то есть значения атрибута type для строк, в которых имеется "<w lemma="), а значениями - количество их вхождений в файле. Распечатать ключи из словаря в открытый для записи файл (значения распечатывать не нужно).

# 3. (10 баллов) С помощью регулярных выражений найти и подсчитать все вхождения прилагательных во множественном числе \
# (то есть таких разборов, в которых type=" начинается с "l" и содержит "f" на третьей позиции, например: type="lhfosf").
# Результат подсчётов напечатать в другой открытый для записи файл таким образом, чтобы каждая пара "разбор - число вхождений" \
# располагалась на одной строке. Преобразуйте содержимое корпуса в формат csv. Возьмите строки внутри тэга <body> и очистите их от тэгов при помощи re.sub.
# Запишите результат в новый файл следующим образом: на одной строке должны находиться лемма, разбор, словоформа, разделенные запятыми.
# Пунктацию и служебную информацию можно удалить.
import re
import csv


def text():
    f = open('f.xml', 'r', encoding='utf-8')
    s = f.readlines()
    return s


def count(corp):
    with open('count.txt', 'w', encoding='utf-8') as f:
        n = str(len(corp))
        f.write(n)


def dic(corp):
    dict = {}
    # <w lemma="hafa" type="sng">hafa</w>
    for i in corp:
        r = re.search('<w lemma=.+ type="(.+)".+', i)
        if r:
            n = r.group(1)
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
    return dict


def dic_to_file(dic, m):
    with open(m, 'w', encoding='utf-8') as f:
        for i in sorted(dic):
            ni = i
            nis = str(dic[i])
            f.write(ni + ' - ' + nis + '\n')


def adjective(corp):
    dict = {}
    for i in corp:
        # в которых type=" начинается с "l" и содержит "f" на третьей позиции, например: type="lhfosf")
        # <w lemma="strangur" type="lvfovm">strangari</w>
        r = re.search('<w lemma=.+ type="(l[a-z]f.+)".+', i)
        if r:
            n = r.group(1)
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
    return dict


def csvtr(corp):
    dict = []
    dict1 = []
    for i in corp:
#<w lemma="frá" type="aa">frá</w>
#лемма, разбор, словоформа, разделенные запятыми.
        r = re.search('<w lemma=.+',i)
        if r:
            s = re.sub('<w lemma="(.+?)" type="(.+)">(.+)<.+', '\\1, \\2, \\3', i)
            s = s.strip('            \n')
            dict.append(s)
    for i in dict:
        dict1.append(i.split(', '))
    return dict1


def csvtran(dic):
    with open('fin_dict.csv','w', encoding='utf-8') as f:
        output = csv.writer(f)
        for i in range(len(dic)):
            output.writerow([dic[i][0],dic[i][1], dic[i][2]])


def main():
    corp = text()
    count(corp)
    dic_to_file(dic(corp), 'dict_8.txt')
    dic_to_file(adjective(corp), 'dict_10.txt')
    csvtran(csvtr(corp))


main()
