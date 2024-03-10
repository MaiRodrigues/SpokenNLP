import os

dir = ''

texto = ''

for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            contents = file.read()
            indice = contents.find(texto)
            if indice != -1:
                print({name})
