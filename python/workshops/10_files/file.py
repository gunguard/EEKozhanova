# Пользователь вводит предложение на английском языке, и программа создает вложенные друг в друга папки, так чтобы путь к самой глубокой из них составлял введенное предложение.
# Например, если пользователь ввел предложение "It is a wonderful day", программа должна создать вложенные папки, и путь к последней из них должен быть "it/is/a/wonderful/day"

import os


def inp():
    inpt = input('Введите предложение: ')
    words = inpt.split(' ')
    return words


def cret(a):
    path = '.'
    for i in a:
        path = path + os.sep + i
    os.makedirs(path)


def main():
    cret(inp())


main()
