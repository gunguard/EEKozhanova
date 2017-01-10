# Текст должен состоять из 5 предложений разных типов (утвердительные, вопросительные, отрицательные, условные, побудительные) на русском языке.
# Типы предложений должны выводиться в случайном порядке.
import random


# Утвердительное предложение вида: Я яростно прыгал, бесконечно дергая водяные волосы, пока она отчаянно страдала.
                                    # noun + adv + intran + ',' + adv + advpart + pronadj + plurnoun + ',' + link + noun +\
                                    # intran + '.'
                                    # Нужны отдельные списки союзов в принципе и союзов условных предложений + в прил\
                                    # агательные пихнуть местоименные штуки

# Вопросительное предложение вида: Почему бесконечный Миша много бил поле?
#Что + "это"; кто + "этот/эта"; какой/какая/какое
# Нужно отдельное прописывание для местоимений, мужского и женского родов

# Отрицательное предложение вида: Я не бегал.
                                    # noun +
# никогда, нигде, нимало, никак, ничуть, нисколько, нисколечко + не
# Условное предложение вида: Если мама поцеловала лягушку, ты кинул меня.


# Побудительное предложение вида: Пой, свинота!
                                # Давай прыгать, мечтатель!
                                # Пусть умрет смерть!
def type_2():
    sentence = question() + ' ' + tranverbconcord(adjective(givingnoun()), adv(), accusative(givingnoun(),givingtype())) + '?'
    sentence=sentence.capitalize()
    return sentence


def type_3():
    sentence = givingnoun() + ' ' + negadv() + ' ' +
    sentence=sentence.capitalize()
    return sentence


def opening(name):
    f = open(name, 'r', encoding='utf-8')
    s = f.read().split()
    words = []
    for n in s:
        words.append(n.lower().strip('n\.,!?:;\'\"()[]=+-_#&@*{}|?/«»—'))
    f.close
    return words


def noun():
    if random.random>0.5:
        return [random.choice(opening('support/animnoun.txt')),0]
    else:
        return [random.choice(opening('support/inanimnoun.txt')),1]


def givingnoun():
    r=noun()
    return r[0]


def givingtype():
    r=noun()
    return r[1]


def adjective(word):
    random_adjective=random.choice(opening('support/adjective.txt'))
    if len(word)>=3:
        if word.endswith('и') or word.endswith('ы'):
            random_adjective = random_adjective.replace('ый', 'ые')
            random_adjective = random_adjective.replace('ий', 'ие')
        elif word.endswith('а') or word.endswith('я'):
            random_adjective = random_adjective[0:len(random_adjective)-2] + 'ая'
        elif word.endswith('о') or word.endswith('е'):
            random_adjective = random_adjective[0:len(random_adjective)-2] + 'ое'
    return random_adjective + ' ' + word
#СРЕЗЫ, ИСПОЛЬЗУЙ СРЕЗЫ!!!!!!!!


def adverb():
    return random.choice(opening('support/adverb.txt'))


def negadv():
    random_adverb=random.choice(opening('support/negadverb.txt'))
    if random_adverb != 'не':
        random_adverb = random_adverb + ' ' + 'не'
    return random_adverb


def imperative(word):
    random_imperative = random.choice(opening('support/imperative.txt'))
    if word.endswith('ы') or word.endswith('и'):
        random_imperative = random_imperative + 'те'
    return random_imperative + ',' + ' ' + word + '!'


def adverbal_participle(obj,adv):
    return adv + ' ' + random.choice(opening('support/part.txt')) + ' ' + obj


def concord(nu,subj):
    random_verb = random.choice(opening(nu))
    if not subj.endswith('ты') or subj.endswith('я') :
        if subj.endswith('и') or subj.endswith('ы'):
            return random_verb + 'и'
        elif subj.endswith('а') or subj.endswith('я'):
            return random_verb + 'а'
        elif subj.endswith('е') or subj.endswith('о'):
            return random_verb + 'а'
    else:
        return random_verb


def intranverbconcord(subj, adv, nu):
    random_verb = random.choice(opening('support/intranverbs.txt'))
    if len(subj)>=3:
        concord('support/intranverbs.txt',)
    else:
        result = subj + ' ' + adv + ' ' + random_verb
        #Нужно учесть "Вы"
    return result


def tranverbconcord(subj, adv, object, nu):
    random_verb = random.choice(opening('support/tranverbs.txt'))
    if not subj.endswith(' ты') or subj.endswith(' я'):
        if subj.endswith('и') or subj.endswith('ы'):
            random_verb = random_verb + 'и'
        elif subj.endswith('а') or subj.endswith('я'):
            random_verb = random_verb + 'а'
        elif subj.endswith('о') or subj.endswith('е'):
            random_verb = random_verb + 'о'
    return subj + ' ' + adv + ' ' + random_verb + ' ' + object


def accusative(obj,number):
    if not obj == 'я' or obj == 'ты' or obj == 'он' or obj == 'она' or obj == 'вы' or obj == 'оно' or obj == 'мы':
        if obj.endswith('я'):
            acc = obj[0:len(obj) - 1] + 'ю'
        elif obj.endswith('а'):
            acc = obj[0:len(obj) - 1] + 'у'
        elif obj.endswith('е') or obj.endswith('о') or obj.endswith('и') or obj.endswith('ы'):
            acc = obj
    elif obj == 'я':
        acc = 'меня'
    elif obj == 'мы':
        acc = 'нас'
    elif obj == 'ты':
        acc = obj
    elif obj == 'вы':
        acc = 'вас'
    elif obj == 'он' or obj == 'оно':
        acc = 'его'
    elif obj == 'она':
        acc = 'её'
    return acc


def condadv():
    return random.choice(opening('support/condlink.txt'))


def link():
    return random.choice(opening('support/link.txt'))


def question():
    return random.choice(opening('support/question.txt'))


def type_1():
    sentence = givingnoun() + ' ' + intranverbconcord(adjective(givingnoun()), adv()) + ',' + ' ' + adverbal_participle(givingnoun(),adverb())\
    + ',' + link() + ' ' + intranverbconcord(adjective(givingnoun()), adv()) + '.'
    sentence=sentence.capitalize()
    return sentence




def text_creation():




def text():
    random.shuffle(txt)
    return print (' '.join(txt))