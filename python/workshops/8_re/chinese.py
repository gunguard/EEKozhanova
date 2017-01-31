import re

def PrepText():
    f=open('text.txt','r',encoding='utf-8')
    s=f.readlines()
    words=[]
    for n in s:
        words.append(n)
    f.close
    return words


def findname(m):
    res = []
    reg = '«([А-Я][а-я]+)(-[0-9]*)?»'
    for i in m:
        res.append(re.findall(reg,i))
    return res


def main():
    print(findname(PrepText()))
    return


main()
