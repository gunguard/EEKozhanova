#Написать свою имплементацию функции shutil.rmtree() - то есть функцию, которая удаляет выбранную папку со всеми папками и файлами внутри неё.

import os
import shutil

for root, dirs, files in os.walk('C:/Users/gunguard/Desktop/FaCL, 1 year/PaCI and some shit/EEKozhanova/python/workshops/11_files_cont/benis', topdown=False):
    for f in files:
        os.remove(os.path.join(root,f))
    for d in dirs:
        os.rmdir(os.path.join(root,d))
    os.rmdir(root)