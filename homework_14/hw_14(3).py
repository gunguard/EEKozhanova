# Поскольку карточки устроены стандартным образом, с таких страниц можно автоматически собирать информацию.
# Этим и должна заниматься Ваша программа из очередного дз. Она должна открывать заранее сохранённый html-файл со статьёй \
# из русской википедии на определённую тему с определённой карточкой (в зависимости от варианта) и доставать оттуда кое-какую информацию (тоже в зависимости от варианта).
# Извлеченную информацию она должна записать в текстовый файл.
# 3. статьи о вузах (напр., Высшая школа экономики) -- количество преподавателей

import re


def text():
    f = open('hse.html', 'r', encoding='utf-8')
    s = f.read()
    return s

def matches(m):
    s = re.findall('(Преподаватели).+?\n.+?\n.+?([0-9] [0-9]+)',m)
    st = ' '.join(s[0])
    return st


def main():
    txt = text()
    print(matches(txt))


main()