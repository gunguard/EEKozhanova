# Подсчитать количество словоформ и записать в файл csv.



def PrepText():
    f = open('text.txt', 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"“()[]=+-_#&@*{}|?/«»—'))
    f.close
    words.sort()
    return words


def unique(n):
    match = {}
    for l in range(len(n)-1):
        for k in range(len(n)-1):
            if n[l] != n[k]:
                for i in match:
                    if n[l] == i:
                        break
                else:
                    match[n[l]] = 0
        match[n[l]] += 1
    print(len(match))
    print(match)
    return match


def lox(arr):
    with open('list1.txt', 'w', encoding='utf-8') as f:
        for a in sorted(arr):
            f.write(str(a))
            f.write('\t')
            f.write(str(arr[a]))
            f.write('\n')
    f.close


def main():
    may = PrepText()
    may1 = unique(may)
    lox(may1)

main()