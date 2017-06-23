# 1 (5 баллов). Посчитайте, сколько в каждом файле слов, запишите эту информацию в новый текстовый файл в формате "название файла<табуляция>количество слов", для каждого файла информация на новой строчке.

# 2 (8 баллов). Создайте csv-таблицу с полями "Название файла", "Автор", "Дата создания текста", содержащую информацию о всех статьях. Пример таблицы ниже.

# Название файла	Автор	Дата создания текста
# file.xhtml	Батюшков Константин	2017.05.30
# 3 (10 баллов). Найдите в текстах все биграммы вида "прилагательное в род. пад. + существительное в род. пад.". В новый текстовый файл запишите найденные биграммы; на каждой строке нужно записать биграмму и предложение, в котором она встретилась, разделив их табуляцией. Повторяющиеся биграммы убирать не надо.


import re
import os
import csv


def open_folder():
    names = []
    names2 = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if not f.endswith('.xhtml'):
                continue  # файлы с другими расширениями, не относящиеся к корпусу, нас не интересуют.
            names = os.path.join(os.getcwd(), root, f)
            names = os.path.normpath(names)
            names2.append(names)
    return names2


#    for root, dirs, files in os.walk('.'):
#        print(root)
#        print(dirs)
#        print(files)
#        for f in dirs:
#            for n in files:
#                print(n)

#    os.getcwd()
#    print(os.getcwd())
#    for root, dirs, files in os.walk('.'):
#        print(files)
#        print(dirs)
#        for f in files:
#            print(f.split('.')[1])
#            if f.split('.')[1] == 'xhtml':
#                names.append(os.path.join(os.getcwd(), dirs[0], f)
#    print(names)
#           if f.split('.')[1] == 'xhtml':
#                names.append(os.path.join(os.getcwd(),dirs[0],f)
#        for l in dirs:
#            for n in files:
#                lst.append(os.path.join(os.getcwd(),l,n))


def open_file(x):
    f = open(x, 'r', encoding='windows-1251')
    n = f.readlines()
    f.close
    return n


def freq_ana_1(n):
    mass = []
    for i in n:
        if re.search(r'<w>', i):
            m = re.search('<w>', i)
            mass.append(m)
    return mass


def file_freq(n, l):
    dict = {}
    p = str(l)
    print(p)
    k = re.search(r'news\\_.+\.xhtml', p)
    m = k.group(0)[5:]
    dict[m] = len(n)
    return dict


def add_freq(n):
    m = n.keys()
    with open('.\\1.csv', 'a', encoding='utf-8') as f:
        output = csv.writer(f, delimiter='\t')
        for i in m:
            output.writerow([i, n[i]])


# 2 (8 баллов). Создайте csv-таблицу с полями "Название файла", "Автор", "Дата создания текста", содержащую информацию о всех статьях. Пример таблицы ниже.
def pre_legend(l):
    # <title>Сергей Латышев.
    mass = []
    for i in l:
        if re.search(r'<meta content="(.+)" name="author">', i):
            m = re.search('<meta content="(.+)" name="author">', i)
            mass.append(m.group(1))
    return mass


def pre_legend2(l):
    mass = []
    for i in l:
        if re.search(r'<meta content="(.+)" name="created">', i):
            m = re.search('<meta content="(.+)" name="created">', i)
            mass.append(m.group(1))
    return mass


def pre_add_legend():
    with open('.\\2.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Название файла', 'Автор', 'Дата создания текста'])
        writer.writeheader()


def add_legend(p, t, q):
    m = p.keys()
    with open('.\\2.csv', 'a', encoding='utf-8') as f:
        output = csv.writer(f, delimiter='\t')
        for i in m:
            output.writerow([i, t[0], q[0]])


def main():
    n = open_folder()
    pre_add_legend()
    for i in n:
        l = open_file(i)
        m = freq_ana_1(l)
        p = file_freq(m, i)
        add_freq(p)
        t = pre_legend(l)
        q = pre_legend2(l)
        add_legend(p, t, q)


if __name__ == '__main__':
    main()
