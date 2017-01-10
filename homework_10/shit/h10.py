# Текст должен состоять из 5 предложений разных типов (утвердительные, вопросительные, отрицательные, условные, побудительные) на русском языке.
# Типы предложений должны выводиться в случайном порядке.
import random


def opening(name):
    f = open(name, 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words


def noun():
    n = random.random()
    if n > 0.5:
        return [random.choice(opening('support/animnoun.txt')), 0]
    else:
        return [random.choice(opening('support/inanimnoun.txt')), 1]


def givingnoun():
    r = noun()
    return r[0]


def givingtype():
    r = noun()
    return r[1]


def concord(nu, subj):
    random_verb = random.choice(opening(nu))
    if not subj.endswith(' ты') or subj.endswith(' я') or subj != 'ты' or subj != 'я':
        if subj.endswith('и') or subj.endswith('ы'):
            random_verb = random_verb + 'и'
        elif subj.endswith('а') or subj.endswith('я'):
            random_verb = random_verb + 'а'
        elif subj.endswith('е') or subj.endswith('о'):
            random_verb = random_verb + 'а'
    return random_verb


def adjective(word):
    random_adjective = random.choice(opening('support/adjective.txt'))
    if len(word) >= 3:
        if word.endswith('и') or word.endswith('ы'):
            random_adjective = random_adjective.replace('ый', 'ые')
            random_adjective = random_adjective.replace('ий', 'ие')
        elif word.endswith('а') or word.endswith('я'):
            random_adjective = random_adjective[0:len(random_adjective) - 2] + 'ая'
        elif word.endswith('о') or word.endswith('е'):
            random_adjective = random_adjective[0:len(random_adjective) - 2] + 'ое'
    return random_adjective + ' ' + word


def tranverb(subj, adv, object):
    random_verb = concord('support/tranverbs.txt', subj)
    print(type(subj))
    print(type(adv))
    print(type(object))
    return subj + ' ' + adv + ' ' + random_verb + ' ' + object


def intranverb(subj, adv):
    random_verb = concord('support/intranverbs.txt', subj)
    return subj + ' ' + adv + ' ' + random_verb


def accusative(obj, num):
    acc = ''
    if not obj == 'я' or obj == 'ты' or obj == 'он' or obj == 'она' or obj == 'вы' or obj == 'оно' or obj == 'мы':
        if obj.endswith('я'):
            acc = obj[0:len(obj) - 1] + 'ю'
            return acc
        elif obj.endswith('а'):
            acc = obj[0:len(obj) - 1] + 'у'
            return acc
        elif obj.endswith('е') or obj.endswith('о') or obj.endswith('ё'):
            acc = obj
            return acc
    elif obj == 'я':
        acc = 'меня'
        return acc
    elif obj == 'мы':
        acc = 'нас'
        return acc
    elif obj == 'ты':
        acc = obj
        return acc
    elif obj == 'вы':
        acc = 'вас'
        return acc
    elif obj == 'он' or obj == 'оно':
        acc = 'его'
        return acc
    elif obj == 'она':
        acc = 'её'
        return acc
    elif num == 0:
        if obj.endswith('ы') or obj.endswith('ки'):
            acc = obj[0:len(obj) - 1] + 'ов'
        elif obj.endswith('и'):
            acc = obj[0:len(obj) - 1] + 'ев'
        elif obj.endswith('й'):
            acc = obj[0:len(obj) - 1] + 'я'
        else:
            acc = obj[0:len(obj) - 1] + 'а'
        return acc
    elif num == 1:
        acc = obj
        return acc


def imperative(word):
    random_imperative = random.choice(opening('support/imperative.txt'))
    if word.endswith('ы') or word.endswith('и'):
        random_imperative = random_imperative + 'те'
    return random_imperative + ',' + ' ' + word + '!'


def adverb():
    return random.choice(opening('support/adverb.txt'))


def negadv():
    random_adverb = random.choice(opening('support/negadverb.txt'))
    if random_adverb != 'не':
        random_adverb = random_adverb + ' ' + 'не'
    return random_adverb


def condadv():
    return random.choice(opening('support/condlink.txt'))


def link():
    return random.choice(opening('support/link.txt'))


def question():
    return random.choice(opening('support/question.txt'))


def adverbal_participle(obj, adv):
    random_part = random.choice(opening('support/part.txt'))
    return adv + ' ' + random_part + ' ' + obj


def type_1():
    sentence = intranverb(adjective(givingnoun()), adverb()) + ',' + ' ' + adverbal_participle(
        accusative(givingnoun(), givingtype()),
        adverb()) \
               + ',' + link() + ' ' + intranverb(adjective(givingnoun()), adverb()) + '.'
    sentence = sentence.capitalize()
    return sentence


def type_2():
    sentence = question() + ' ' + tranverb(adjective(givingnoun()), adverb(),
                                           accusative(givingnoun(), givingtype())) + '?'
    sentence = sentence.capitalize()
    return sentence


def type_3():
    sentence = intranverb(givingnoun(), negadv()) + '.'
    sentence = sentence.capitalize()
    return sentence


def type_4():
    sentence = condadv() + ' ' + intranverb(adjective(givingnoun()), adverb()) + ',' + link() + ' ' + tranverb(
        givingnoun(), '',
        accusative(
            givingnoun(),
            givingtype())) + '.'
    sentence = sentence.capitiliza()
    return sentence


def type_5():
    sentence = imperative(givingnoun())
    sentence = sentence.capitalize()
    return sentence

print(type_5())


def text():
    a = type_1()
    b = type_2()
    c = type_3()
    d = type_4()
    e = type_5()
    txt = [a,b,c,d,e]
    random.shuffle(txt)
    print(txt)
    return


text()
