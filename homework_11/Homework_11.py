# Cколько в тексте существительных с суффиксом -hood, какое существительное имеет минимальную частотность, а также выводит слова, от которых эти существительные образованы (например, если нашлось childhood, то нужно напечатать child, и так для всех слов с этим суффиксом).


def PrepText():
    f = open('text.txt', 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words


def hoodlist(arr):
    words = []
    for word in arr:
        if word.endswith('hood'):
            words.append(word)
    return words


def frequency(arr):
    n = 1
    frequency = []
    l = arr
    for i in range(len(l)):
        for j in range(len(l)):
            if type(l[i]) == str and type(l[j]) == str and l[i] == l[j] and i != j:
                n += 1
                l[j] = 0
        if type(l[i]) == str:
            frequency.append(n)
        l[i] = 0
        n = 1
    return frequency


def wordlist(arr):
    n = 1
    exactword = []
    l = arr
    for i in range(len(l)):
        if type(l[i]) == str:
            exactword.append(l[i])
        for j in range(len(l)):
            if type(l[i]) == str and type(l[j]) == str and l[i] == l[j] and i != j:
                n += 1
                l[j] = 0
        l[i] = 0
    return exactword


def minfrequency(arrword, arrnum):
    return arrword[(arrnum.index(min(arrnum)))]


def roots(arr):
    new = []
    for word in arr:
        word = word[0:len(word) - 4]
        new.append(word)
    return new


def main():
    print(len(hoodlist(PrepText())))
    print(minfrequency(wordlist(hoodlist(PrepText())), frequency(hoodlist(PrepText()))))
    print(roots(wordlist(hoodlist(PrepText()))))
    return


main()
