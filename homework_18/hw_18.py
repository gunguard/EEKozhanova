# Программа должна обходить всё дерево папок, начинающееся с той папки, где она находится, и сообщать следующую информацию (далее - по вариантам):
# 3. файлы с каким расширением чаще всего встречаются в этих папках (если таких много, можно печатать только одно);


import os
import random


def extension():
    lst = []
    # os.chdir('C:/Users/gunguard/Desktop/FaCL, 1 year/PaCI and some shit/EEKozhanova/homework_18')
    for root, dirs, files in os.walk('.'):
        # os.getcwd()
        # По какой-то причине указание точки как текущей директории работает не очень, поэтому использую эту функцию.
        for n in files:
            lst.append(os.path.splitext(n)[1])
    return lst


def count(n):
    dict = {}
    for i in range(len(n)):
        if n[i] not in dict:
            dict[n[i]] = 1
        else:
            dict[n[i]] += 1
    return dict


def freq(n,r):
    m = n[random.choice(r)]
    for i in sorted(n):
        if m < n[i]:
            m = int(n[i])
    print(m)


def main():
    n = extension()
    m = count(n)
    freq(m,n)


if __name__ == '__main__':
    main()