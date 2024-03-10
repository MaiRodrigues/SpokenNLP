import os
import fileinput

dir = ''

for name in os.listdir(dir):
    if name.endswith('.txt'):
        path = os.path.join(dir, name)
        with fileinput.FileInput(path, inplace=True,  encoding='utf-8') as name:
            for linha in name:
                print(linha.replace('', ''), end='')
