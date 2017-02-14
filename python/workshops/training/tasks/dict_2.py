# Задача по мотивам задачи на pythontutor. Нужно взять вот этот файл, сделать из него русско-латинский и латинско-русский словарь следующего вида:
# Ключами должны быть индивидуальные слова, а значениями их переводы. Если у нескольких слов одинаковый перевод, нужно разделить их и сделать отдельными ключами: {'ille': 'тот', 'illa': 'тот', 'illud': 'тот'}.
# Если у слова есть несколько переводов, то нужно склеить их все в одно значение: {'тот': 'ille, illa, illud'}
# в русско-латинском словаре ключи - руские слова, значения - их латинские переводы, в латинско-русском наоборот.


def text():
    f = open('lat_rus.txt', 'r', encoding='utf-8')
    s = f.readlines()
    words = []
    for n in s:
        words.append(n.strip('\n'))
    f.close
    return words


def latrus(t):
    dict = {}
    for i in t:
        pr = i.split(' — ')
        lat = pr[0].split(', ')
        for n in lat:
            dict[n] = pr[1]
    print(dict)


def ruslat(t):
    dict = {}
    for i in t:
        pr = i.split(' — ')
        rus = pr[1].split(', ')
        for n in rus:
            dict[n] = pr[0]
    print(dict)


def main():
    txt = text()
    latrus(txt)
    ruslat(txt)

main()
