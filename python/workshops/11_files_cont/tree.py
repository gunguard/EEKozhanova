#Написать программу, которая рисует дерево текущей папки в таком виде:
#--folder1
# --folder4
#       file4
#       file5
# --folder5
#--folder2
# file2
# file3
#--folder3

import os

for root, dirs, files in os.walk('C:/User/gunguard/Desktop/FaCL, 1 year/PaCI and some shit/EEKozhanova/python/workshops/11_files_cont/nu'):
    print(root)
    for d in dirs:
        print(d)
        for f in files:
            print(d, f)