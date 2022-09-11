import numpy as np
slovar = dict()
print ('Введите длину префикса:')
pref = int(input())
print ('Введите строку:')
s = input()
lst = s.split()
for i in range(len(lst) - pref):
    key = lst[i]
    if not (key in slovar):
        znach = []
        for j in range(len(lst) - pref - i):
            if lst[i + j] == key:
                for k in range(pref):
                    znach.append(lst[i + j + pref])
        newznach = ' '.join(map(str, znach))
        other = {key: newznach}
        slovar.update(other)
print ('Введите длину генерируемого текста (слов):')
leng = int (input())
print ('Введите первое слово')
first = (input())
text = []
text.append(first)

for i in range(leng - 1):
    if (text[i] in slovar):
        newwordlist = slovar[text[i]].split()
        newword = np.random.choice(newwordlist)
        text.append(newword)
    else:
        #newword = np.random.choice(slovar.keys()) - чтобы вставлять случайное слово в случае отсустствия подходящих продолжений
        newword = lst[0] # чтобы возвращяться к первому слову текста в случае отсустствия подходящих продолжений
        text.append(newword)
    
print(' '.join(text))
