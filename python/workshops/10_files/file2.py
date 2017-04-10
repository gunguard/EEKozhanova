# Пользователь вводит число, например, 3.
# Нужно создать количество папок в соответствии с введенным числом.
# В нашем случае это три папки, которые должны называться "1", "2", "3". В первой папке нужно создать один текстовый файл, во второй два файла, в третьей - три файла и т.д.

import os


def inp():
    inpt = input('Введите предложение: ')
    return inpt

def cret(a):
    n = a
    n=int(n)
    for i in range(n):
        path = '.'
        path = path + os.sep + i
        os.mkdir(path)
        for m in range(i):
            path = path + os.sep + m + os.sep + '.txt'
            f=open(path,'w')
            f.close()
        path = '.'

def main():
    cret(inp())


main()