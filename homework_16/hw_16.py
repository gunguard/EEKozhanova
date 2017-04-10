# 3. Преобразовать все предложения в тексте, после каждого слова дописав его длину в символах через подчеркивание. Так, "Мама вымыла раму" превращается в



def PrepText():
    f = open('text.txt', 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.strip('n\.,!?:;\'\"“()[]=+-_#&@*{}|?/«»—'))
    f.close
    words2 = []
    for i in words:
        if len(i) > 0:
            words2.append(i)
    return words2


def dic(a):
    d1 = {n: len(n) for n in a}
    return d1


def form(txt, di):
    template = '{}_{}'
    for n in txt:
        print(template.format(n, di[n]))


def main():
    m = PrepText()
    form(m, dic(m))


if __name__ == "__main__":
    main()
