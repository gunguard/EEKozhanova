words=[]
with open('file1.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        a=line.split()
        for item in a:
            words.append(item)
fw=open('file2.txt','w',encoding='utf-8')
for word in words:
    fw.write(word)
fw.close()
