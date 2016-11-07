word=input('Введите слово: ')
if word.endswith('a') or word.endswith('я'):
    print ('Possible forms: Nom. Sg.')
elif word.endswith('ы') or word.endswith('и'):
    print ('Possible forms: Gen. Sg./Nom. Pl./Acc. Pl.')
elif word.endswith('у') or word.endswith('ю'):
    print ('Possible forms: Acc. Sg.')
elif word.endswith('e'):
    print ('Possible forms: Dat. Sg./Prep. Sg.')
elif word.endswith('ой') or word.endswith('ей'):
    print ('Possible forms: Instr. Sg.')
elif word.endswith('ь'):
    print ('Possible forms: Gen. Pl.')
elif word.endswith('aм') or word.endswith('ям'):
    print ('Possible forms: Dat. Pl.')
elif word.endswith('aми') or word.endswith('ями'):
    print ('Possible forms: Instr. Pl.')
elif word.endswith('aх') or word.endswith('ях'):
    print ('Possible forms: Prep. Pl.')
else:
    print ('Possible forms: Gen. Pl.')
