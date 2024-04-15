# Dataset Card para [Notícias do IBGE]

## Dados Gerais

<!-- Se você está apenas usando um dataset já existente, coloque aqui os dados
do dataset original. Se você está combinando ou alterando datasets, ou está
construindo um dataset novo, preencha apenas o nome do dataset. -->

- **Nome:** Dataset de notícias extraídas da *API* de notícias IBGE

## Resumo

<!-- Elabore uma breve descrição do dataset, informando: 
* Se foram usados datasets já existentes (quais são esses datasets?).
* O uso principal pretendido (classificação de texto, reconhecimento de entidades, etc.).
* Os principais idiomas presentes.
* O domínio dos dados. -->

Este conjunto de dados foi feito com base em notícias obtidas da *API* de notícias do *IBGE (https://servicodados.ibge.gov.br/api/docs/noticias?versao=3), extraindo-se os textos delas através de técnicas de *web-scrapping*. Ele pode ser encontrado em (https://drive.google.com/file/d/14bF1uEUii2EWRwpt8IFhtfqce0aSyM9n/view?usp=drive_link).

## Utilização Pretendida

<!-- Indique quais as tarefas de NLP podem utilizar este dataset. Por exemplo, 
classificação de texto, reconhecimento de entidades, etc. 
Nesta seção, você pode detalhar e expandir o que foi apresentado no resumo. -->

O conjunto de dados será utilizado para treinar modelos de segmentação de textos em tópicos.

## Idiomas

<!-- Indique os idiomas presentes no dataset. -->
Os textos do *dataset* criado são escritos em Língua Portuguesa.

## Criação

Extraiu-se as notícias através de requisição à API disponibilizada pelo fornecedor (`http://servicodados.ibge.gov.br/api/v3/noticias/`). A resposta dela retorna uma lista com, entre outros campos, a *URL* da notícia. Para extrair seu texto, foi realizado processo de *web-scrapping* no *HTML* presente na página apontada pela *URL*.

O campo **editoria** representa o tema da notícia, e seus valores possíveis são: **economicas**, **geociencias**, **sociais**, **revistaretratos**, **ibge;censo2020**, **ibge**, **seriesespeciais**, **revistaretratos;ibge**, **sociais;ibge**, **sociais;economicas**, **seriesespeciais;censo2020**, **censo2020**, **sociais;censo2020**, **ibge;geociencias** e **sociais;geociencias**.

Percebeu-se que, das 5722 notícias extraídas, grande parte delas possuíam um valor nulo no campo **editoria**. Portanto, elas foram removidas, totalizando um conjunto deduzido de 3776 delas.

Cada notícia foi armazenada na linha de um *dataframe* **Pandas**. Para aleatorizar as notícias nele armazenadas e evitar o surgimento de grandes blocos contíguos de notícias de mesma categoria, ele foi aleatorizado utilizando-se o método **.sample**, passando como argumentos **frac=1**.

Para prepará-lo para as etapas de treinamento, realizou-se as seguintes etapas:
- Tokenização dos textos das notícias a nível de sentença e posterior concatenação delas com o caractere de quebra de linha (**\n**);
- Divisão do conjunto em outros três: **treino** (contendo 70% das amostras), **teste** (com 20%) e **validação** (com 10%).
- Aglutinação das notícias para criação de textos maiores em arquivos (cada arquivo contém de uma a cinco notícias, quantia atribuída aleatoriamente), respeitando o formato de entrada do **Segformer**;


## Estrutura

Seguem algumas características gerais do conjunto de dados:

|dataset|Historico_de_materias| 
|-------|---------------------|
|idioma|Portuguese|
|Número de notícias|5722|
|Número de notícias utilizadas| 3376 |
Tabela 1: Estatísticas Gerais do *dataset*.

Na próxima seção, são exibidas amostras do *dataset* nos dois estágios descritos.

### Amostras

Segue uma amostra do conjunto de dados no primeiro estágio (como registro de um *dataframe* **Pandas**). Nele, cada linha do *dataframe* corresponde a uma notícia. **Obs.:** A amostra abaixo é exibida no formato **JSON** apenas para efeitos de visualização.

```json
{
    "editorias": "economicas",
    "texto": "Mais da metade dos filhos (51,4%) tiveram ascensão sócio-ocupacional em relação à mãe (mobilidade intergeracional), enquanto 47,4% ascenderam em relação ao pai.\nA presença da mãe no domicílio contribuiu para um nível mais ..."
}
```

Um exemplo de arquivo com notícias de diferentes tópicos aglutinadas segue abaixo:

```text
========== ; economicas; economicas
O IBGE realizou mais uma atualização semestral da listagem dos municípios que compõem as regiões metropolitanas (RMs), regiões integradas de desenvolvimento (RIDEs) e aglomerações urbanas definidas pelos estados e pela União, com base em informações de 31 de dezembro de 2016.
Desde 2013, o IBGE atualiza semestralmente, em seu site, a composição das diferentes RMs, RIDEs e Aglomerações Urbanas instituídas no país.
Outras informações sobre os recortes regionais podem ser acessadas aqui.Revisão mostra criação de RMs nos estados de São Paulo, Ceará e RondôniaAtualmente, existem 73 regiões metropolitanas no país, sendo que o estado com maior número é a Paraíba (12), seguida por Santa Catarina (9) e Alagoas (8).
A revisão atual do IBGE mostra a criação da RM de Ribeirão Preto (SP), com 34 municípios, instituída pela Lei Complementar nº 1.290, de 06 de julho de 2016.Além disso, foi criada a RM de Sobral (CE), com 18 municípios, instituída pela Lei Complementar nº 168, de 27 de dezembro de 2016.
Por fim, foi registrada a primeira Região Metropolitana rondoniense, que inclui a capital do estado, Porto Velho, e o município de Candeias do Jamari, conforme Lei nº 3.654, de 09 de novembro de 2015.A revisão do IBGE não traz mudanças nas listagens de municípios das regiões integradas de desenvolvimento (RIDEs): a de Petrolina/Juazeiro, a da Grande Teresina e a do Distrito Federal e Entorno.As regiões metropolitanas e aglomerações urbanas são recortes instituídos por lei complementar estadual, de acordo com a determinação da Constituição Federal de 1988, visando integrar a organização, o planejamento e a execução de funções públicas de interesse comum.
É competência dos estados a definição das regiões metropolitanas e aglomerações urbanas, nos termos do Artigo 25, Parágrafo 3° da Constituição Federal.
Já as Regiões Integradas de Desenvolvimento (RIDEs) são definidas como regiões administrativas que abrangem diferentes unidades da federação.
As RIDEs são criadas por legislação específica, na qual os municípios que as compõem são elencados, além de definir a estrutura de funcionamento e os interesses das unidades político-administrativas participantes.
No caso das RIDEs, a competência de criá-las é da União, dada pelo Artigo 43, Parágrafo 1° da Constituição Federal.
Comunicação Social23 de maio de 2017


```


### Campos dos Dados

<!-- Indique e descreva os campos presentes no dataset. Informe o tipo do campo. 
Se for um campo de categoria, informe os valores possíveis. -->

A resposta da requisição à *API* contêm uma lista de notícias chamada **items**. Cada elemento dela possui dois campos que vale destacar para a construção deste conjunto:

- **editorias**: categoria à qual a notícia pertence;
- **link**: *URL* da página *web* da notícia;

Para informações sobre os outros atributos da resposta, consultar a documentação da *API* presente em (https://servicodados.ibge.gov.br/api/docs/noticias?versao=3). 

O primeiro estágio do conjunto (*dataframe* **Pandas**) possui a seguinte estrutura:

- **texto:** corpo da notícia (extraído a partir de *web-scrapping* da página hospedada na *URL* do campo **link**);
- **editorias:** categoria da notícia (mesmo campo de cada item da resposta);

Os arquivos gerados para entrada ao modelo **Segformer** possuem o seguinte formato:

```text
========== ; editorias_1; editorias_1
texto_1
========== ; editorias_2; editorias_2
texto_2
.....
```
, no qual **editorias_n** representa a categoria da notícia **n** (campo **editorias**) do arquivo e **texto_n** o texto do mesmo (campo **texto**, com 1 <= **n** <= 4). O modelo escolhido utiliza apenas a primeira ocorrência de **editorias_n** no arquivo (entre os delimitadores "========== ;" e ";"), sendo a segunda necessária apenas porque a entrada do modelo a atribui como obrigatória (não a utilizando no processamento interno). 


### Divisão dos Dados

<!-- Descreva as divisões existentes no dataset. Por exemplo, conjuntos de
treinamento, validação e teste. Forneça os tamanhos das divisões. Se achar
pertinente, forneça também estatísticas úteis de cada divisão. -->

Nas próximas subseções, seguem informações e estatísticas acerca dos subconjuntos gerados a partir da divisão do *dataset*.

#### Treino
- Tamanho (medido em notícias): 2643
- Número de palavras: 3047504
- Número de sentenças: 64881
- Número de documentos gerados: 1062


Número de notícias por categoria:


|Categoria | Quantidade |  Porcentagem de composição |
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

Distribuição de documentos aglutinados por tamanho (medido em notícias):

|Número de notícias| Frequência |
|--------|---------------|
|1       | 258             |
|2       | 282             |
|3       | 267             |
|4       | 255             |


#### Teste
- Tamanho (medido em notícias): 755
- Número de palavras: 889779
- Número de sentenças: 17918
- Número de documentos gerados: 299

Número de notícias por categoria:


|Categoria | Quantidade |  Porcentagem de composição |
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


Distribuição de documentos aglutinados por tamanho (medido em notícias):

|Número de notícias| Frequência|
|--------|---------------|
|1       | 65             |
|2       | 79             |
|3       | 87             |
|4       | 68             |

#### Validação
- Tamanho (medido em notícias): 378
- Número de palavras: 435643
- Número de sentenças: 9021
- Número de documentos gerados: 156


Número de notícias por categoria:


|Categoria | Quantidade |  Porcentagem de composição |
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

Distribuição de documentos aglutinados por tamanho (medido em notícias):

|Número de notícias| Frequência |
|--------|---------------|
|1       | 44             |
|2       | 42             |
|3       | 30             |
|4       | 40             |



