# 3. Сколько найдено папок, название которых состоит только из кириллических символов.
# Кроме этого, программа должна выводить на экран названия всех файлов или папок, которые она нашла, без повторов (это задание на 9 и 10).

import os


def count():
    m = 0
    for f in os.listdir('.'):
        if os.path.isdir(f):
            # for i in range(1040, 1104):
            #       for s in f:
            #           if s != chr(i):
            #               break
            #           m += 1
            # print(f)
            # with open(os.path.join('.', f)) as text:
            #            print('file: ', f, '   text: ', text.read())
            # m += 1
            n = 0
            for s in f:
                if not 1040 <= ord(s) <= 1103:
                    n += 1
                    break
            if n == 0:
                m += 1
    print('Число папок: ', m)


def names():
    n = []
    for f in os.listdir('.'):
        if os.path.isfile(f):
            n.append(os.path.splitext(f)[0])
            # with open(os.path.join('.', f)) as text:
            #    print('file: ', f, '   text: ', text.read())
            #    print(text.read())
        else:
            n.append(f)
    return n


def unique(n):
    match = []
    for l in range(len(n)):
        for k in range(len(n)):
            if n[l] != n[k]:
                for i in match:
                    if n[l] == i:
                        break
                else:
                    match.append(n[l])
    print('Уникальные названия элементов: ', ', '.join(match))


def main():
    count()
    n = names()
    unique(n)


if __name__ == "__main__":
    main()
