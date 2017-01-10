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
    return random.choice(opening('support/noun.txt'))


def concord(nu, subj):
    random_verb = random.choice(opening(nu))
    if not subj.endswith(' ты') or subj.endswith(' я') or subj != 'ты' or subj != 'я':
        if subj.endswith('и') or subj.endswith('ы'):
            random_verb = random_verb + 'и'
        elif subj.endswith('а') or subj.endswith('я'):
            random_verb = random_verb + 'а'
        elif subj.endswith('е') or subj.endswith('о'):
            random_verb = random_verb + 'о'
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
    return subj + ' ' + adv + ' ' + random_verb + ' ' + object


def intranverb(subj, adv):
    random_verb = concord('support/intranverbs.txt', subj)
    return subj + ' ' + adv + ' ' + random_verb


def accusative():
    return random.choice(opening('support/object.txt'))


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


def link():
    return random.choice(opening('support/link.txt'))


def question():
    return random.choice(opening('support/question.txt'))


def adverbal_participle(obj, adv):
    random_part = random.choice(opening('support/part.txt'))
    return adv + ' ' + random_part + ' ' + obj


def type_1():
    sentence = intranverb(adjective(noun()), adverb()) + ',' + ' ' + adverbal_participle(accusative(),adverb()) + ',' + ' '+ link() + ' ' + intranverb(adjective(noun()), adverb()) + '.'
    sentence = sentence.capitalize()
    return sentence


def type_2():
    sentence = question() + ' ' + intranverb(adjective(noun()), adverb()) + '?'
    sentence = sentence.capitalize()
    return sentence


def type_3():
    sentence = intranverb(noun(), negadv()) + '.'
    sentence = sentence.capitalize()
    return sentence


def type_4():
    sentence = 'Если' + ' ' + intranverb(adjective(noun()), adverb()) + ',' + ' ' + tranverb(noun(), adverb(),accusative()) + '.'
    sentence = sentence.capitalize()
    return sentence


def type_5():
    sentence = imperative(noun())
    sentence = sentence.capitalize()
    return sentence


def text():
    a = type_1()
    b = type_2()
    c = type_3()
    d = type_4()
    e = type_5()
    txt = [a,b,c,d,e]
    random.shuffle(txt)
    print(' '.join(txt))
    return


text()
