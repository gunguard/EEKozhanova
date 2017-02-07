import re


def PrepText():
    f=open('brik.txt','r',encoding='utf-8')
    s=f.readlines()
    s1=re.sub('(([А-Яа-я0-9]| )+ [А-Яа-я0-9]+)(\.\?!)', '\\1@@@', s)
#    s1=re.sub('[А-Яа-я0-9]+ [А-Яа-я0-9]|(!|"|\'|\)?+')
    print(s1)

PrepText()
