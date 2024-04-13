# Dataset Card para [Noticias publicadas no Brasil]

## Dados Gerais

<!-- Se você está apenas usando um dataset já existente, coloque aqui os dados
do dataset original. Se você está combinando ou alterando datasets, ou está
construindo um dataset novo, preencha apenas o nome do dataset. -->

- **Nome:** [Notícias publicadas no Brasil]
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

[Este conjunto de dados contém uma compilação de matérias extraídas dos sites do grupo globo. São mais de 10 mil textos, publicados entre 2014 e 2020, com as seguintes informações:

|Dados: dados em que a matéria foi extraída do site|
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

[classicacção de texto]
[modelagem de tópicos]

## Idiomas

<!-- Indique os idiomas presentes no dataset. -->

[Português]

## Criação

<!-- Se o dataset foi construído por você, indique a fonte dos dados usados e
descreva o processo de coleta e processamento. Se foi usado um dataset já existente,
indique a URL do dataset original. Se o dataset existente foi modificado,
descreva a modificação realizada e as ferramentas usadas. -->

[(https://www.kaggle.com/datasets/diogocaliman/notcias-publicadas-no-brasil)]

[O dataset criado por Diogo Caliman inicialmente continha 10.109 notícias categorizadas em esportes, economia, política, tecnologia e celebridades. Após a limpeza dos valores incorretos e a remoção de 75% das notícias de esportes para balancear o dataset, restaram 1.500 notícias de esportes e 5.564 notícias de outras categorias.

O dataset foi então dividido em um conjunto de treinamento com 3.895 notícias e um conjunto de teste com 1.669 notícias. No conjunto de treinamento, as categorias foram distribuídas da seguinte forma:

Economia: 1.092 notícias
Esportes: 1.017 notícias
Política: 979 notícias
Tecnologia: 422 notícias
Famosos: 385 notícias
No conjunto de teste, as categorias ficaram assim:

Esportes: 474 notícias
Economia: 466 notícias
Política: 384 notícias
Tecnologia: 190 notícias
Famosos: 155 notícias
Essa divisão foi feita considerando a distribuição de documentos por categoria em cada conjunto, com diferentes quantidades de documentos por notícia. O objetivo era criar conjuntos balanceados para treinamento e teste do modelo.

O conjunto de treinamento foi composto por 3.895 notícias divididas em documentos com diferentes quantidades de notícias por documento:

895 documentos com 5 notícias cada
1000 documentos com 4 notícias cada
1500 documentos com 3 notícias cada
500 documentos com 2 notícias cada
Já o conjunto de teste foi composto por 1.669 notícias divididas da seguinte forma:

385 documentos com 5 notícias cada
416 documentos com 4 notícias cada
651 documentos com 3 notícias cada
218 documentos com 2 notícias cada
]

## Estrutura

|dataset|Historico_de_materias| 
|-------|---------------------|
|idioma|Portuguese|
|# docs|10109|
|# docs utilizados| 5564|
|# sections| 
|# sentences|
|# headings|
|# classes|

### Amostras

<!-- Dê um exemplo usando uma estrutura JSON de uma amostra típica do dataset. 

Um exemplo de amostra do dataset:

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

[Este conjunto de dados foi criado a partir de um script que pode ser facilmente modificado para ler o conteúdo de outros sites (web scraping).]

### Campos dos Dados

<!-- Indique e descreva os campos presentes no dataset. Informe o tipo do campo. 
Se for um campo de categoria, informe os valores possíveis. -->


- |:dados de publicação da notícia:| :endereço da página com a notícia salva no web.archive:|:endereço da página com a notícia no portal original:|:título da notícia:      |:Texto principal da notícia:|:Assunto da notícia (esportes, economia, política, tecnologia ou famosos):|  
  |--------------------------------|--------------------------------------------------------|---------------------------------------------------|---------------------------|-------------------------  -|--------------------------------------------------------------------------|
  |31/12/2013 a 2020-04-20         |10106 endereços únicos                                  |10089 valores únicos                               | 10087 valores únicos      |10081 valores únicos        |  Esportes 60%,  Economia 15%,  Outro (2516)  25%                         |

### Divisão dos Dados

<!-- Descreva as divisões existentes no dataset. Por exemplo, conjuntos de
treinamento, validação e teste. Forneça os tamanhos das divisões. Se achar
pertinente, forneça também estatísticas úteis de cada divisão. -->


#### Treino
Tamanho: 2643
Número de palavras: 3047504
Número de sentenças: 64881
Número de documentos gerados: 1062


Número de notícias por categoria


|:Categoria: |: Quantidade: | : Porcentagem de composição: |
|--------|------------|------------------------------------|
|economicas  | 1535         | 58,1%                               |
|sociais  | 396         | 15,0%                               |                                        
|ibge| 307         | 11,6%                               |                                        
|geociencias| 183         | 6,9%                               |                                        
|seriesespeciais| 66         | 2,5%                               |                                        
|sociais;economicas   | 13         | 0,5%                               |                                        
|revistaretratos  | 47         | 1,8%                               |                                        
|ibge;censo2020| 80         | 3,0%                               |                                        
|seriesespeciais;censo2020| 7  | 0,3%                               |                                        
|sociais;geociencias| 2         | 0,07%                               |                                        
|ibge;geociencias| 3         | 0,1%                               |                                        
|censo2020| 1       | 0,04%                               |                                        
|sociais;ibge| 2 | 0,08%                                |
|revistasretratos;ibge| 1 | 0,04%                                |
|sociais;censo2020| 0 | 0,0%                                |

Distribuição de documentos aglutinados por tamanho (medido em notícias)

|:n° notícias:| :n° frequência:|
|--------|---------------|
|1       | 258             |
|2       | 282             |
|3       | 267             |
|4       | 255             |


#### Teste
Tamanho: 755
Número de palavras: 889779
Número de sentenças: 17918
Número de documentos gerados: 299

Número de notícias por categoria


|:Categoria: |: Quantidade: | : Porcentagem de composição: |
|--------|------------|------------------------------------|
|economicas  | 446         | 59,1%                               |
|sociais  | 109         | 14,44%                               |                                        
|ibge| 80         | 10,6%                               |                                        
|geociencias| 58         | 7,7%                               |                                        
|seriesespeciais| 14         | 1,9%                               |                                        
|sociais;economicas   | 5         | 0,7%                               |                                        
|revistaretratos  | 16         | 2,1%                               |                                        
|ibge;censo2020| 20         | 2,6%                               |                                        
|seriesespeciais;censo2020| 2  | 0,3%                               |                                        
|sociais;geociencias| 0         | 0,0%                               |                                        
|ibge;geociencias| 0         | 0,0%                               |                                        
|censo2020| 3       | 0,4%                               |                                        
|sociais;ibge| 1 | 0,1%                                |
|sociais;censo2020| 1 | 0,1%                                |
|revistasretratos;ibge| 0 | 0%                                |


Distribuição de documentos aglutinados por tamanho (medido em notícias)

|:n° notícias:| :n° frequência:|
|--------|---------------|
|1       | 65             |
|2       | 79             |
|3       | 87             |
|4       | 68             |

#### Validação
Tamanho: 378
Número de palavras: 435643
Número de sentenças: 9021
Número de notícias: 156


Número de notícias por categoria - conjunto de validação:


|:Categoria: |: Quantidade: | : Porcentagem de composição: |
|--------|------------|------------------------------------|
|economicas  | 227         | 60,0%                               |
|sociais  | 51         | 13,5%                               |                                        
|ibge| 48         | 12,7%                               |                                        
|geociencias| 24         | 6,4%                               |                                        
|seriesespeciais| 11         | 2,9%                               |                                        
|sociais;economicas   | 2         | 0,5%                               |                                        
|revistaretratos  | 5         | 1,3%                               |                                        
|ibge;censo2020| 9         | 3,4%                               |                                        
|seriesespeciais;censo2020| 0  | 0,0%                               |                                        
|sociais;geociencias| 0         | 0,0%                               |                                        
|ibge;geociencias| 0         | 0,0%                               |                                        
|censo2020| 1       | 0,3%                               |                                        
|sociais;ibge| 0 | 0,1%                                |
|sociais;censo2020| 0 | 0,1%                                |
|revistasretratos;ibge| 0 | 0%                                |

Distribuição de documentos aglutinados por tamanho (medido em notícias)

|:n° notícias:| :n° frequência:|
|--------|---------------|
|1       | 44             |
|2       | 42             |
|3       | 30             |
|4       | 40             |



