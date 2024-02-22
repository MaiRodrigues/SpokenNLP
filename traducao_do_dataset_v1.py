!pip install googletrans==3.1.0a0

from googletrans import Translator
from google.colab import drive
import os

#conecta com drive
drive.mount('/content/drive')

#carrega o tradutor
translator = Translator()

input_location = 'diretorio' # pasta com dataset original
output_location = 'diretorio' # pasta com as traduções
translator = Translator()


for root, dir, files in os.walk(input_location):
    for file in files:
        if file.endswith('.txt'):
            new_file = "{}_translated.txt".format(file.split('.')[0])
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_location, new_file)

            # faz a leitura dos arquivos
            with open(input_file_path, 'r') as f:
                file_contents = f.read()

            # traduz os arquivos
            translation = translator.translate(file_contents, dest='pt')
            translated_text = translation.text

            # salva os novos arquivos traduzidos em outra pasta
            with open(output_file_path, 'w') as f:
                f.write(translated_text)
