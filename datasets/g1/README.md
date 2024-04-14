# Dataset Card para [Noticias publicadas no Brasil]

## Dados Gerais

<!-- Se você está apenas usando um dataset já existente, coloque aqui os dados
do dataset original. Se você está combinando ou alterando datasets, ou está
construindo um dataset novo, preencha apenas o nome do dataset. -->

- **Nome:** *Dataset* de notícias extraído do RSS do G1

## Resumo

<!-- Elabore uma breve descrição do dataset, informando: 
* Se foram usados datasets já existentes (quais são esses datasets?).
* O uso principal pretendido (classificação de texto, reconhecimento de entidades, etc.).
* Os principais idiomas presentes.
* O domínio dos dados. -->

Este conjunto de dados contém notícias extraídas do repositório de notícias do G1 (Portal de notícias *online* da Globo) no formato *RSS* (*Rich Site Summary*), atualizado pela última vez em 08/11/2012 (disponível em: https://g1.globo.com/tecnologia/noticia/2012/11/siga-o-g1-por-rss.html). Os arquivos foram submetidos a pré-processamentos para aderirem ao formato do modelo a ser utilizado no projeto.



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


Extraiu-se os arquivos *RSS* através de requisição à API disponibilizadao pelo fornecedor (`GET https://g1.globo.com/rss/g1/{categoria}`) com as notícias da data referida. Para extrair os textos das notícias das respostas em formato *XML*, elas foram requisições a um pré-processamento e cada notícia foi armazenada na linha de um *dataframe* **Pandas**. Para aleatorizar as notícias nele armazenadas e evitar o surgimento de grandes blocos contíguos de notícias de mesma categoria, ele foi aleatorizado utilizando-se o método **.sample**, passando como argumentos **frac=1**.

Para prepará-lo para as etapas de treinamento, realizou-se as seguintes etapas:
- Tokenização dos textos das notícias a nível de sentença e posterior concatenação delas com o caractere de quebra de linha (**\n**);
- Divisão do conjunto em outros três: **treino** (contendo 70% das amostras), **teste** (com 20%) e **validação** (com 10%).
- Aglutinação das notícias para criação de textos maiores em arquivos (cada arquivo contém de uma a cinco notícias, quantia atribuída aleatoriamente), respeitando o formato de entrada do **Segformer**;

## Estrutura

A tabela abaixo mostra alguns dados gerais do *dataset* construído:

|dataset|Notícias G1| 
|-------|---------------------|
|idioma|português|
|Número de documentos total |1300|
|Número de documentos utilizados| 1300 |

Na próxima seção, são mostradas algumas amostras do *dataset*.

### Amostras

Segue uma amostra do conjunto de dados no primeiro estágio (como registro de um *dataframe* **Pandas**). Nele, cada linha do *dataframe* corresponde a uma notícia. **Obs.:** A amostra abaixo é exibida no formato **JSON** apenas para efeitos de visualização.

```json
{
 "title": "Cientista e engenheiro de dados estão em alta e têm salário que pode passar de R$ 20 mil; veja como entrar",
 "description": "   Com desafio de encontrar mão de obra qualificada, profissões seguem em alta em 2024 porque empresas valorizam cada vez mais o uso de dados na tomada de decisões.\nO g1 ...",
 "category": "tecnologia"
}
```

Um exemplo de arquivo com notícias de diferentes tópicos aglutinadas segue abaixo:

```text
========== ; loterias; loterias
   Sorteio acontece no dia 30 de março, às 20h.
Apostas podem ser feitas a partir deste sábado (16).
Dupla Sena, Loteria
Stephanie Fonseca/G1
A Dupla Sena de Páscoa irá pagar um prêmio de R$ 35 milhões.
O concurso especial será realizado no dia 30 de março, às 20h (horário de Brasília).
As apostas podem ser feitas a partir deste sábado (16) — e vão até as 19h do dia do sorteio.
(Veja mais abaixo como apostar) 
Como a Dupla Sena de Páscoa não acumula, se ninguém acertar as seis dezenas, o prêmio será dividido entre os acertares da quina do primeiro sorteio, e assim por diante.
Essa é a oitava edição do concurso especial da Dupla Sena.
O maior prêmio da modalidade foi pago em 2023, quando duas apostas dividiram R$ 34,9 milhões.
Como apostar
As apostas podem ser feitas em lotéricas, no portal Loterias Caixa e também no aplicativo Loterias Caixa.
O bilhete da Dupla Sena dá o dobro de chances de ganhar: são dois sorteios por concurso e ganha acertando 3, 4, 5 ou 6 números no primeiro ou segundo sorteio.
O apostador deve escolher de 6 a 15 números dentre os 50 disponíveis para jogar.
O apostador também tem a opção de solicitar a Surpresinha, que é quando o sistema escolhe os números.
A aposta simples custa R$ 2,50.
Veja como foi a edição de 2023:
Dupla Sena de Páscoa: Bolão de Goiânia ganha R$ 17 milhões

```

### Campos dos Dados

<!-- Indique e descreva os campos presentes no dataset. Informe o tipo do campo. 
Se for um campo de categoria, informe os valores possíveis. -->

A resposta às requisições feitas à rota `GET https://g1.globo.com/rss/g1/{categoria}` são retornadas em formato *XML*, e contêm, em sua hierarquia, uma lista de elementos chamada **items** dentro de **channel** -> **image**. Cada um desses elementos possui a seguinte forma:


- **title:** título da notícia 
- **link:** URL da  página da notícia
- **description:** corpo da notícia  
- **category:** categoria da notícia (sempre é G1) 
- **pubDate:** data de publicação 

Para a elaboração do primeiro estágio (criação do *dataframe* Pandas), projeta-se um subconjunto desses atributos: **title**, **description** e **category**. Como, para todas as notícias, o valor do último atributo é sempre **G1**, ele é sobrescrito com o parâmetro **{categoria}** da *URL* da requisição. Além disso, o texto presente em **description** é processado para a remoção de alguns demarcadores padrões retornados pela rota. Seguem os seus campos e suas respectivas descrições:


- **title:** título da notícia
- **description:** corpo da notícia (com remoção de demarcadores) |
- **category:** categoria da notícia (extraída da URL da requisição) |

O campo categoria representa o tema da notícia, e a relação entre os seus valores e as seções de notícias do portal é dada pela seguinte tabela:

|Valor do campo|Seção         | 
|--------------|---------------------|
| brasil | Brasil |
| carros | Carros |
| economia | Economia |
| educacao | Educacao |
| loterias | Loterias |
| mundo | Mundo |
| musica | Musica |
| natureza | Natureza |
| planeta-bizarro | Planeta Bizarro |
| politica | Política |
| pop-arte | Pop & Arte |
| tecnologia | Tecnologia & Games |
| turismo-e-viagem | Turismo & Viagem |

Os arquivos gerados para entrada ao modelo **Segformer** possuem o seguinte formato:

```text
========== ; category_1; category_1
description_1
========== ; category_2; category_2
description_2
.....
```
, no qual **category_n** representa a categoria (campo **category** anteriormente mencionado) da notícia  **n** do arquivo e **description_n** (campo **description** anteriormente mencionado) o texto do mesmo (com 1 <= **n** <= 5). O modelo escolhido utiliza apenas a primeira ocorrência de **category_n** no arquivo (entre os delimitadors "========== ;" e ";"), sendo a segunda necessária apenas porque a entrada do modelo a atribui como obrigatória (não a utilizando no processamento interno). 


### Divisão dos Dados

<!-- Descreva as divisões existentes no dataset. Por exemplo, conjuntos de
treinamento, validação e teste. Forneça os tamanhos das divisões. Se achar
pertinente, forneça também estatísticas úteis de cada divisão. -->

Nas próximas subseções, seguem informações e estatísticas acerca dos subconjuntos gerados a partir da divisão do *dataset*.

#### Treino
- Tamanho (medido em notícias): 909
- Número de palavras: 630435
- Número de sentenças: 23148
- Número de documentos gerados: 319


Número de notícias por categoria


|Categoria | Quantidade |  Porcentagem de composição |
|--------|------------|------------------------------------|
|brasil  | 71         | 7,8%                               |
|carros  | 68         | 7,5%                               |                                        
|economia| 72         | 7,9%                               |                                        
|educacao| 65         | 7,2%                               |                                        
|loterias| 71         | 7,9%                               |                                        
|mundo   | 72         | 7,9%                               |                                        
|musica  | 69         | 7,6%                               |                                        
|natureza| 75         | 8,3%                               |                                        
|planeta-bizarro| 74  | 8,1%                               |                                        
|politica| 72         | 7,9%                               |                                        
|pop-arte| 65         | 7,1%                               |                                        
|tecnologia| 67       | 7,4%                               |                                        
|turismo-e-viagem| 68 | 7,5%                               |

Distribuição de documentos aglutinados por tamanho (medido em notícias)

|Número de notícias| Frequência |
|--------|---------------|
|1       | 69             |
|2       | 72             |
|3       | 63             |
|4       | 66             |
|5       | 49             |


#### Teste
- Tamanho (medido em notícias): 261
- Número de palavras: 186426
- Número de sentenças: 6967
- Número de documentos gerados: 89

Número de notícias por categoria


|Categoria | Quantidade |  Porcentagem de composição |
|--------|------------|------------------------------------|
|brasil  | 18         | 6,9%                               |
|carros  | 20         | 7,7%                               |                                        
|economia| 18         | 6,9%                               |                                        
|educacao| 23         | 8,8%                               |                                        
|loterias| 22         | 8,4%                               |                                        
|mundo   | 13         | 5,0%                               |                                        
|musica  | 20         | 7,7%                               |                                        
|natureza| 19         | 7,3%                               |                                        
|planeta-bizarro| 19  | 7,3%                               |                                        
|politica| 20         | 7,7%                               |                                        
|pop-arte| 25         | 9,6%                               |                                        
|tecnologia| 24       | 9,2%                               |                                        
|turismo-e-viagem| 20 | 7,7%                               |

Distribuição de documentos aglutinados por tamanho (medido em notícias)

|Número de notícias| Frequência |
|--------|---------------|
|1       | 19             |
|2       | 21             |
|3       | 14             |
|4       | 16             |
|5       | 19             |

#### Validação
- Tamanho (medido em notícias): 130
- Número de palavras: 91984
- Número de sentenças: 3295
- Número de documentos gerados: 46


Número de notícias por categoria - conjunto de validação:


|Categoria | Quantidade |  Porcentagem de composição |
|--------|------------|------------------------------------|
|brasil  | 11         | 8,5%                               |
|carros  | 12         | 9,2%                               |                                        
|economia| 10         | 7,7%                               |                                        
|educacao| 12         | 9,2%                               |                                        
|loterias| 7         | 5,4%                               |                                        
|mundo   | 15         | 11,5%                               |                                        
|musica  | 11         | 8,5%                               |                                        
|natureza| 6         | 4,6%                               |                                        
|planeta-bizarro| 7  | 5,4%                               |                                        
|politica| 8         | 6,2%                               |                                        
|pop-arte| 10         | 7,7%                               |                                        
|tecnologia| 9       | 6,9%                               |                                        
|turismo-e-viagem| 12 | 9,2%                               |

Distribuição de documentos aglutinados por tamanho (medido em notícias)

|Número de notícias| Frequência |
|--------|---------------|
|1       | 11             |
|2       | 8             |
|3       | 11             |
|4       | 8             |
|5       | 8             |



