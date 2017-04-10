# Программа считывает текст и создает словарь, где ключ - словоформа, а значение - позиция в тексте.


def PrepText():
    f = open('text.txt', 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"“()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words


def gh(m):
    a = {n: m[n] for n in range(len(m))}
    print(a)


def put(arr):
    with open('list2.txt', 'w', encoding='utf-8') as f:
        for a in arr:
            print(a)
            f.write('{0}\t{1}\n'.format(a, str(arr(a))))



def main():
    may = PrepText()
    may1 = gh(may)
    put(may1)

main()