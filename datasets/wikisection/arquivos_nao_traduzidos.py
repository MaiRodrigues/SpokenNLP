import re
import os

input_folder = r'direotorio'

# palavras em ingles mais comuns
english_words = {
    "the", "is", "to", "of", "and", "in", "that", "have",
    "it", "not", "on", "with", "he", "you", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there",
    "their", "what", "so", "out", "if", "about", "who", "get",
    "which", "go",
}

matching_files = []
total_files = 0

# faz a leitura dos arquivos
for file_name in os.listdir(input_folder):
    if file_name.endswith('.txt'):
        total_files += 1
        input_file_path = os.path.join(input_folder, file_name)

        with open(input_file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()

        matched_words = [word for word in english_words if re.search(r'\b{}\b'.format(re.escape(word)), file_contents)] # loop pra procurar pelas palavras da lista  no diretorio

        if len(matched_words) > 10: # filtra apenas os arquivos onde a quantidade de palaras encontradas e maior que 10
            print(f"Palavras encontradas em {file_name}: {', '.join(matched_words)}")
            matching_files.append(file_name)
            os.remove(input_file_path) # Remove o arquivo correspondente

print("Numero total de arquivos:", total_files)
print("Numero total de arquivos em inglês:", len(matching_files))
