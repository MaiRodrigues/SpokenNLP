# TRADUCAO DO DATASET
from googletrans import Translator
import os
import shutil

# Carrega o tradutor
translator = Translator()

input_location = 'diretorio'  # Pasta com dataset original
output_location = 'diretorio'  # Pasta com as traduções

for root, dir, files in os.walk(input_location):
    for file in files:
        if file.endswith('.txt'):
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_location, file)  # Usa o nome original do arquivo

            # Faz a leitura dos arquivos
            with open(input_file_path, 'r', encoding='utf-8') as f:
                file_contents = f.read()

            # Traduz os arquivos
            translation = translator.translate(file_contents, dest='pt')
            translated_text = translation.text

            # Salva os novos arquivos traduzidos em outra pasta
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(translated_text)

# INCLUI O ' ' NOVAMENTE NA MARCAÇÃO DOS RÓTULOS 

for filename in os.listdir(output_location):
    if filename.endswith(".txt"):
        filepath = os.path.join(output_location, filename)
        temp_filepath = os.path.join(output_location, "temp_" + filename)
        with open(filepath, 'r', encoding='utf-8') as infile, open(temp_filepath, 'w', encoding='utf-8') as outfile:
            for line in infile:
                outfile.write(line.replace(';', ' ;'))
        shutil.move(temp_filepath, filepath)
