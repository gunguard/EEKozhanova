# 1 (5 баллов). Посчитайте среднее количество разборов (тэг ana) на слово (тэг w).


# Нужно два счётчика: для w и для ana. Поделить ana на w.
# <w>пожарных<ana lex="пожарный" gr="S,m,anim=abl,pl" /><ana lex="пожарный" gr="S,m,anim=acc,pl" /><ana lex="пожарный" gr="S,m,anim=gen,pl" /></w>
# NB слова и разборы повторяются => сделать вариант с учётом повторения + сделать вариант без учета повторения на основании тега

# 2 (8 баллов). Составьте частотный словарь всех частей речи в тексте. Например: {'APRO': 5, 'S': 277, ...}. Распечайте содержимое словаря в отдельный файл (на каждой строке "часть речи"<табуляция>"частотность").

# 3 (10 баллов). Найдите в тексте все существительные в творительном падеже (обратите внимание, что некоторые разборы омонимичные. Если хотя бы один разбор с указанием творительного падежа присутствует, слово берём). Запишите в отдельный файл найденные существительные и контекст их употребления в таком формате:
# 3 слова слева<табуляция>найденное существительное<табуляция>3 слова справа.
# За сохранение знаков препинания отдельный плюс.

# NB везде нужно ебаться с повторениями, примерный способ это сделать есть для задания 1.



import re
import csv
import os


def open_file():
    f = open('text.xml', 'r', encoding='utf-8')
    n = f.readlines()
    f.close
    return n


def freq_ana_1(n):
    mass = []
    mass2 = []
    for i in n:
        if re.search('<w>', i):
            m = re.search('<w>', i)
            mass.append(m)
        if re.findall('ana', i):
            l = re.findall('ana', i)
            for m in l:
                mass2.append(m)
    print(len(mass2))
    count = len(mass2) / len(mass)
    return count


def freq_ana_2(n):
    mass = []
    mass2 = []
    mass3 = []
    for i in n:
        if re.findall('<ana.+</w>', i):
            l = re.findall('<ana.+</w>', i)
            for m in l:
                mass2.append(m)
    for p in range(len(mass2)):
        if mass2.count(mass2[p]) == 1:
            mass3.append(mass2[p])
            #       else:
            #           for ma in range(len(mass3):
            #               for mas in range(len(mass2)):
            #                   if mass3[mas] == mass [p]:
    for g in range(len(mass2)):
        counter = 0
        for j in range(g + 1, len(mass2)):
            if mass2[g] == mass2[j]:
                counter += 1
                if counter >= 0:
                    mass3.append(mass2[g])
    for m in mass3:
        if re.findall('ana', m):
            l = re.findall('ana', m)
            for k in l:
                mass.append(k)
    print(len(mass2))
    print(len(mass3))
    print(len(mass))
    count = len(mass) / len(mass3)
    return count
    #   dict = []
    #   for i in n:
    #       g
    #       if re.search(r'<w>[абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ]+<', i):
    #           m = re.search(r'<w>[абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ]+<', i)
    #           l = m.group(0)[3:-1].lower()
    #           print(l)
    #           dict.append(l)
    #   for k in n:
    #       for key in dict:
    #           if key
    #           if re.findall('ana', k):
    #               s = re.findall('ana', k)
    #               for si in s:
    #                   mass2.append(s)
    #   print(dict)


def pre_freq_word_class(n):
    # gr="S,
    #    dict = {}
    mass = []
    for i in n:
        if re.findall('(gr="[A-Z]+(,|=))', i):
            l = re.findall('(gr="[A-Z]+(,|=))', i)
            for m in l:
                mass.append(m[0][4:-1])
    return mass


def freq_word_class(n):
    dict = {}
    for i in range(len(n)):
        if n[i] not in dict:
            dict[n[i]] = 1
        else:
            dict[n[i]] = dict[n[i]] + 1
    print(dict)
    return dict


def add_freq(n):
    with open('class_dict.csv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter='\t')
        m = n.keys()
        for i in m:
            output.writerow([i, n[i]])


def instr(n):
    dict = []
    for i in range(len(n)):
        if re.search('ins',n[i]):
            if re.search(r'<w>[а-яА-Я]+<', n[i]):
               m = re.search(r'<w>[а-яА-Я]+<', n[i])
               l = m.group(0)[3:-1]
               for k in range(i-3, i):
                   if re.search(r'<w>[а-яА-Я]+<', n[k]):
                       z = re.search(r'<w>[а-яА-Я]+<', n[k])
                       t = z.group(0)[3:-1]
                       dict.append(t)
               dict.append(l)
               for p in range(i+1, i+5):
                   if re.search(r'<w>[а-яА-Я]+<', n[p]):
                       g = re.search(r'<w>[а-яА-Я]+<', n[p])
                       j = g.group(0)[3:-1]
                       dict.append(j)
    print(dict)


def main():
    n = open_file()
    print(freq_ana_1(n))
    print(freq_ana_2(n))
    m = pre_freq_word_class(n)
    l = freq_word_class(m)
    add_freq(l)
    instr(n)


if __name__ == '__main__':
    main()
