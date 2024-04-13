Dataset Card para [Noticias G1]


## Dados Gerais

<!-- Se você está apenas usando um dataset já existente, coloque aqui os dados
do dataset original. Se você está combinando ou alterando datasets, ou está
construindo um dataset novo, preencha apenas o nome do dataset. -->

- **Nome:** [Notícias G1]
- **Página WEB:** [Página WEB do dataset]
- **Repositório:** [Repositório para baixar o dataset]
- **Artigo:** [Link do artigo relacionado ao dataset]
- **Licença:** [Licença do dataset]

## Resumo

<!-- Elabore uma breve descrição do dataset, informando: 
* Se foram usados datasets já existentes (quais são esses datasets?).
* O uso principal pretendido (classificação de texto, reconhecimento de entidades, etc.).
* Os principais idiomas presentes.
* O domínio dos dados. -->

[Este dataset contém uma compilação de matérias extraídas dos sites do grupo globo. São mais de 10 mil matérias, publicadas entre 2014 e 2020, com as seguintes informações:


|Data: data em que a matéria foi extraída do site|
|------------------------------------------------|
|Url da notícia no web.archive: endereço em que a matéria foi salva no web.archive|
|Url da notícia: endereço em que a matéria foi publicada no site original|
|Título: título da matéria|
|Conteúdo: conteúdo da matéria|
|Assunto: assunto da matéria (esportes, economia, política ou famosos)|
]

## Utilização Pretendida

<!-- Indique quais as tarefas de NLP podem utilizar este dataset. Por exemplo, 
classificação de texto, reconhecimento de entidades, etc. 
Nesta seção, você pode detalhar e expandir o que foi apresentado no resumo. -->

<!-- Explique como o dataset pode ser carregado ou baixado, com códigos de 
exemplo e formatos de entrada. -->

## Idiomas

<!-- Indique os idiomas presentes no dataset. -->
[Português]

## Criação

<!-- Se o dataset foi construído por você, indique a fonte dos dados usados e
descreva o processo de coleta e processamento. Se foi usado um dataset já existente,
indique a URL do dataset original. Se o dataset existente foi modificado,
descreva a modificação realizada e as ferramentas usadas. -->

[Este conjunto de dados foi criado a partir de um script que pode ser facilmente modificado para ler o conteúdo de outros sites (web scraping).]

## Estrutura

|data                          |url_noticia                                           |url_noticia_curto                                   |titulo              |conteudo_noticia                              |assunto                                                                 |
|----                          |-----------                                           |-----------------                                   |------              |----------------                              |-------                                                                 |
|data de publicação da notícia |endereço da página com a notícia salva no web.archive |endereço da página com a notícia no portal original |título da notícia   |Texto principal da notícia                    |Assunto da notícia (esportes, economia, política, tecnologia ou famosos)|
|2013-12-31 a 2020-04-20       |10106 unique values                                   |10089 unique values                                 |10087 unique values |10081 unique values                           |esportes 60%, economia 15%,  Other (2516) 25% |
### Amostras

<!-- Dê um exemplo usando uma estrutura JSON de uma amostra típica do dataset. -->

<!-- Um exemplo de amostra do dataset:


```json
{
    "id": "13818513", 
    "summary": "Amanda baked cookies and will bring Jerry some tomorrow.", 
    "dialogue": "Amanda: I baked  cookies. Do you want some?\r\nJerry: Sure!"
}
```
-->

<!-- Se achar importante, dê informações adicionais sobre os dados e que não estejam
em outras seções, por exemplo, estatísticas sobre as amostras do dataset,
distribuição dos dados coletados, etc. -->

### Campos dos Dados

<!-- Indique e descreva os campos presentes no dataset. Informe o tipo do campo. 
Se for um campo de categoria, informe os valores possíveis. -->

- [nome do campo]: [Descrição do campo]
- [nome do campo]: [Descrição do campo]
- [nome do campo]: [Descrição do campo]

-->

|data                         |url_noticia                                           |url_noticia_curto                                   |titulo            |conteudo_noticia          |assunto                                                                 |
|----                         |-----------                                           |-----------------                                   |------            |----------------          |-------                                                                 |
|data de publicação da notícia|endereço da página com a notícia salva no web.archive |endereço da página com a notícia no portal original |título da notícia |Texto principal da notícia|Assunto da notícia (esportes, economia, política, tecnologia ou famosos)|

### Divisão dos Dados

<!-- Descreva as divisões existentes no dataset. Por exemplo, conjuntos de
treinamento, validação e teste. Forneça os tamanhos das divisões. Se achar
pertinente, forneça também estatísticas úteis de cada divisão. -->


|Treino|
|------|
|Tamanho: 909| Número de palavras: 630435 |Número de sentenças: 23148| Número de notícias: 911|

|Número de notícias por categoria|

|:Categoria:      |:Quantidade:	|: Porcentagem de composição:|
|-----------------|-------------|----------------------------|
|brasil	          |71	          |7,8%|
|carros           |68	          |7,5%|
|economia	        |72           |7,9%|
|educacao         |65	          |7,2%|
|loterias         |71	          |7,9%|
|mundo	           |72	          |7,9%|
|musica	          |69	          |7,6%|
|natureza         |75	          |8,3%|
|planeta-bizarro  |74	          |8,1%|
|politica         |72           |7,9%|
|pop-arte         |65	          |7,1%|
|tecnologia	      |67	          |7,4%|
|turismo-e-viagem |68	          |7,5%|


|Distribuição de documentos aglutinados por tamanho (medido em notícias)|
|:n° notícias:	|:n° frequência:|
|---------------|---------------|
|1	            |69             |
|2	            |72             |
|3	            |63             |
|4	            |66             |
|5	            |49             |


|Teste|
|-----|
|Tamanho: 261| Número de palavras: 186426 |Número de sentenças: 6967| Número de notícias: 262|

|Número de notícias por categoria|
|:Categoria:	    |: Quantidade:	|: Porcentagem de composição:|
|-------------------|-------------|----------------------------|
|brasil	            | 18	        |6,9%                        |
|carros	            | 20	        |7,7%                        |
|economia           | 18	        |6,9%                        |
|educacao           | 23	        |8,8%                        |
|loterias           | 22	        |8,4%                        |
|mundo	             | 13         |5,0%                        |
|musica	            | 20	        |7,7%                        |
|natureza           | 19	        |7,3%                        |
|planeta-bizarro    | 19	        |7,3%                        |
|politica           | 20	        |7,7%                        |
|pop-arte	          | 25         |9,6%                        |
|tecnologia	        | 24	        |9,2%                        |
|turismo-e-viagem	  |20	         |7,7%                        |


Distribuição de documentos aglutinados por tamanho (medido em notícias)
|:n° notícias:	|:n° frequência:|
|---------------|---------------|
|1	            |19|
|2	            |21|
|3	            |14|
|4	            |16|
|5	            |19|


|Validação|
|Tamanho: 130|  Número de palavras: 91984 |Número de sentenças: 3295 |Número de notícias: 132|

|Número de notícias por categoria - conjunto de validação:|
|---------------------------------------------------------|
|:Categoria:	      |: Quantidade:	|: Porcentagem de composição:|
|brasil	           |11	           |8,5%|
|carros	           |12	           |9,2%|
|economia          |10	           |7,7%|
|educacao          |12	           |9,2%|
|loterias          |7	            |5,4%|
|mundo	            |15	           |11,5%|
|musica            |11	           |8,5%|
|natureza          |6	            |4,6%|
|planeta-bizarro   |7	            |5,4%
|politica          |8	            |6,2%|
|pop-arte          |10	           |7,7%|
|tecnologia	       |9	            |6,9%|
|turismo-e-viagem  |12	           |9,2%|


Distribuição de documentos aglutinados por tamanho (medido em notícias)
|:n° notícias:	| :n° frequência:|
|---------------|----------------|
|1	            |11              |
|2	            |8               |
|3	            |11              |
|4	            |8               |
|5	            |8               |
