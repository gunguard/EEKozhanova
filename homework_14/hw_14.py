# Поскольку карточки устроены стандартным образом, с таких страниц можно автоматически собирать информацию.
# Этим и должна заниматься Ваша программа из очередного дз. Она должна открывать заранее сохранённый html-файл со статьёй \
# из русской википедии на определённую тему с определённой карточкой (в зависимости от варианта) и доставать оттуда кое-какую информацию (тоже в зависимости от варианта).
# Извлеченную информацию она должна записать в текстовый файл.
# 4. статьи об учёных (напр., Эйнштейн, Альберт) -- научная сфера;

import re


def PrepText(m):
    f = open(m, 'r', encoding='utf-8')
    s = f.readlines()
    words = []
    for n in s:
        words.append(n)
    f.close
    return words


def matches(m):
    fres = []
    for i in m:
        if re.search('<span class="no-wikidata" data-wikidata-property-id="P101">', i):
            res = i.split('\"')
            for n in range(len(res)-1):
                if res[n] == ' title=':
                    fres.append(res[n+1])
    for l in range(len(fres)-1):
        if fres[l].endswith(')'):
            f = fres[l].split(' ')
            fres[l] = f[0]
    string = ', '.join(fres)
    return string


def main():
    text = PrepText('einstein.html')
    text1 = PrepText('tesla.html')
    print(matches(text))
    print(matches(text1))


main()