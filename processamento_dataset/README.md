# Dataset Card para [Wikisection]

## Descrição

- *Nome:* [Wikisection]
- *Página WEB:* [https://github.com/CPqD/resid2023-nlp-6/tree/main/processamento_dataset]
- *Repositório:* [(https://github.com/sebastianarnold/WikiSection)]
- *Artigo:* [(https://ojs.aaai.org/index.php/AAAI/article/view/26477)]

### Resumo
es
<!--[Elabore uma breve descrição do dataset, informando: o uso pretendido, os
idiomas presentes, o domínio dos dados.] -->

[Grande conjunto de dados inédito com 38 mil artigos da Wikipedia em inglês e alemão rotulados com 242 mil seções, títulos originais e rótulos normalizados de tópicos para até 30 tópicos de dois domínios: doenças e cidades. Escolhemos esses subconjuntos para abranger tanto aspectos clínicos/biomédicos (por exemplo, sintomas, tratamentos, complicações) quanto tópicos baseados em notícias (por exemplo, história, política, economia, clima). Ambos os tipos de artigos estão razoavelmente bem estruturados de acordo com as diretrizes da Wikipedia (Piccardi et al., 2018), mas mostramos que também são complementares: Doenças é um domínio científico típico com baixa entropia (ou seja, tópicos muito específicos, linguagem precisa e baixa ambiguidade de palavras). Em contraste, cidades se assemelham a um domínio diversificado, com alta entropia (ou seja, tópicos mais amplos, linguagem comum e maior ambiguidade de palavras) e serão mais aplicáveis, por exemplo, a notícias, relatórios de risco ou análises de viagens.]

[Os documentos são originários de despejos recentes em inglês e alemão. Filtramos a coleção usando consultas SPARQL contra o Wikidata (Tanon et al., 2016). Recuperamos instâncias das categorias do Wikidata doença (Q12136) e suas subcategorias (por exemplo, Tricomoníase ou Coqueluche) ou cidade (Q515), por exemplo, Londres ou Madri. Nosso conjunto de dados contém os resumos dos artigos, texto simples do corpo, posições de todas as seções fornecidas pelos editores da Wikipedia com seus títulos originais (por exemplo, "Causas | Sequência genética") e um rótulo normalizado de tópico (por exemplo, doença. causa). Aleatorizamos a ordem dos documentos e os dividimos em 70% de conjuntos de treinamento, 10% de validação e 20% de conjuntos de teste.]
 
[Os documentos são originários de dumps da Wikipedia disponíveis como CC BY-SA 3.0 em  
[dumps.wikimedia.org/enwiki/20180101/](https://dumps.wikimedia.org/enwiki/) (inglês) e [dumps.wikimedia.org/dewiki/20180101/](https://dumps.wikimedia.org/dewiki/) (alemão).
[ Os conjuntos de dados são filtrados por instâncias das classes Wikidata [Q12136](https://www.wikidata.org/wiki/Q12136)  (doença) e [Q515](https://www.wikidata.org/wiki/Q515)  (cidade)]

 

### Utilização Pretendida

<!-- [Indique quais as tarefas de NLP podem utilizar este dataset.] -->

[O dataset pode ser utilizado em tarefas de classificação e segmentação textual.]

### Idiomas

<!-- [Indique os idiomas presentes no dataset] -->

[Inglês e português]

## Estrutura
[ O conjunto de dados WikiSection é fornecido no formato JSON.]


|Campo*          |Descrição*                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|type            | cityoudisease                                                                                                                                      |
|title           | Título do artigo                                                                                                                                   | 
|abstract        | Texto completo do resumo do artigo                                                                                                                 | 
|text           | Texto completo do corpo do documento sem resumo, títulos e elementos de estrutura.   Formato: utf-8   não tokenizado, inclui novas linhas          |
|annotations     | Lista de seções                                                                                                                                    |
|begin           | Comece o deslocamento no documento. Formato: número de caracteres começando em 0. Novas linhas e símbolos de escape contam como um caractere       |
|begin           | Comece o deslocamento no documento. Formato: número de caracteres começando em 0.  |Novas linhas e símbolos de escape contam como um caractere     |
|length          | Comprimento da seção. Formato: número de caracteres                                                                                                |
|sectionHeading	 | Título original da seção. Os títulos aninhados são desdobrados e segmentados por                                                                   |
|sectionLabel    | Rótulo de classe normalizado                                                                                                                       |

### Amostras

<!-- [Dê um exemplo usando uma estrutura JSON de uma amostra típica do dataset.] -->

Um exemplo de amostra do dataset:

``{
  "id" : "https://en.wikipedia.org/wiki/Autoimmune_polyendocrine_syndrome",
  "type" : "disease",
  "title" : "Autoimmune polyendocrine syndrome",
  "abstract" : "Autoimmune polyendocrine syndromes (APSs), also called [...]",
  "text" : "Each \"type\" of this condition has a different cause, in terms of [...]",
  "annotations" : [ {
    "class" : "SectionAnnotation",
    "begin" : 0,
    "length" : 238,
    "sectionHeading" : "Cause",
    "sectionLabel" : "disease.cause"
  }, ... ]
}

[Se achar importante, dê informações adicionais sobre os dados e que não estejam
em outras seções, por exemplo, estatísticas sobre as amostras do dataset,
distribuição dos dados coletados, etc.]

### Campos dos Dados

<!-- [Indique e descreva os campos presentes no dataset. Informe o tipo do campo. Se for um campo de categoria, informe os valores possíveis.] -->

<!-- - [nome do campo]: [Descrição do campo]
- [nome do campo]: [Descrição do campo]
- [nome do campo]: [Descrição do campo]
-->



[Tabela de rótulos de classe]
| *conjunto de dados| *pt_disease* | *de_doença* | *en_city * |  *de_cidade*| **total*   |
|:------------------:|:------------:|:-----------:|:----------:|:-----------:|:----------:|
|linguagem           |  Inglês      | português   | inglês     | português   |            |
|instancia de        |   Q12136     | Q12136      |  Q515      | Q515        |            |
|documentos          |   3.590      | 2.323       |  19.539    | 12.53       | 38k        |
|seções              |   27.838     | 14.784      |  133.642   | 65.907      | 242 mil    |
|frases              |   209.885    | 106.198	   | 1.104.619  | 500.100     | 1,9 milhão |
|títulos             |   8,5 mil    | 6,1 mil     |  23,0 mil  | 12,2k       |            |
|aulas               |   27         | 25          |  30        | 27          |            |
|cobertura           |   94,6%      | 96,6%  	   |  96,6%     | 96,1%       |            |


[Os números para documentos, seções e frases indicam o número total de instâncias no subconjunto. títulos denota o número de títulos distintos de seções e subseções entre documentos. classes denota o número de rótulos de classe após a normalização e remoção da cauda longa. cobertura denota a proporção de seções cobertas pelos rótulos de classe. As seções restantes são dadas à classe other.

 

[Para obter o texto do documento simples, usamos o Wikiextractor, dividimos as seções de resumo e removemos todos os títulos de seção e outras tags de estrutura, exceto caracteres de nova linha e listas.]

#### Discrepância de Vocabulário em Títulos de Seção
[A Tabela 2 mostra exemplos de títulos de seções de artigos sobre doenças separados em cabeça (mais comum), torso (usado frequentemente) e cauda (raro). Inicialmente, esperávamos que os artigos compartilhassem estrutura congruente em nomeação e ordem. Em vez disso, observamos uma alta variação com 8,5 mil títulos distintos no domínio das doenças e mais de 23 mil para cidades em inglês. Uma inspeção mais detalhada revela que os autores da Wikipedia utilizam títulos em diferentes níveis de granularidade, frequentemente copiam e colam de outros artigos, mas também introduzem sinônimos ou hipônimos, o que leva a um problema de discrepância de vocabulário (Furnas et al., 1987). Como resultado, a distribuição dos títulos é de cauda pesada em todos os artigos. Aproximadamente 1% dos títulos aparecem mais de 25 vezes, enquanto a grande maioria (88%) aparece apenas 1 ou 2 vezes.]

#### Agrupamento de Sinônimos
[Para usar os títulos da Wikipedia como fonte para rótulos de tópicos, utilizou-se um método de normalização para reduzir a alta variação dos títulos a poucos rótulos representativos com base no agrupamento de sinônimos do BabelNet (Navigli e Ponzetto, 2012). Criamos um conjunto H que contém todos os títulos no conjunto de dados e usamos a API do BabelNet para associar cada título h ∈ H aos seus sinônimos correspondentes Sh ⊂ S. Por exemplo, "Terapia cognitivo-comportamental" é atribuída ao sinônimo bn:03387773n. Em seguida, inserimos todos os sinônimos correspondentes em um grafo não direcionado G com nós s ∈ S e arestas e. Criamos arestas entre todos os sinônimos que correspondem entre si com um lemma h 0 ∈ H. Finalmente, aplicamos um algoritmo de detecção de comunidades (Newman, 2006) em G para encontrar clusters densos de sinônimos. Usamos esses clusters como tópicos normalizados e atribuímos ao sentido com mais arestas de saída como rótulo representativo, em nosso exemplo: terapia.
A partir deste passo de normalização, obtendo 598 sinônimos podados usando a regra de divisão de cabeça/cauda count(s) <1|S|Psi∈S count(si) (Jiang, 2012). ]

[Este método cobre mais de 94,6% de todos os títulos e gera 26 rótulos normalizados e uma outra classe no conjunto de dados de doenças em inglês. A Tabela 1 mostra os números correspondentes para os outros conjuntos de dados. Verificamos nosso processo de normalização por inspeção manual de 400 atribuições de títulos-rótulos escolhidas aleatoriamente por dois juízes independentes e relatamos uma precisão de 97,2% com um acordo inter-observador médio observado de 96,0%.]


##  Tabela de rótulos de classe
| pt_disease        | de_doença            | en_city                    | de_cidade        |  
|------------------ |----------------------|----------------------------|------------------|     
|causa              | definição            | arquitetura                |arquitetura       |
|classificação      | diagnosticar         | clima                      |clima             |
|complicação        | epidemiologia        | crime                      |demografia        |
|cultura            | fauna                | cultura                    |recreacção        |
|diagnóstico        | pesquisa             | demografia                 |etimologia        |
|epidemiologia      | genética             | distrito                   |município         |
|etimologia         | geografia            | economia                   |parceria municipal|
|fauna              | história             | Educação                   |geografia         | 
|genética           | infecção             | ambiente                   |história          |
|geografia          | categorização        | etimologia                 |infraestrutura    |
|história           | clínica              | instalação                 |igreja            |   
|infecção           | compilação           | fé                         |clima             |   
|gerenciamento      | ser humano           | geografia                  |criminalidade     |
|mecanismo          | órgãos               | saúde                      |cultura           |
|medicamento        | patologia            | história                   |pessoas           |
|patologia          | prevalência          | infraestrutura             |política          |
|fisiopatologia     | prognóstico          | assuntos internacionais    |imprensa          |
|prevenção          | risco                | lei                        |governo           |
|prognóstico        | sintoma              | meios de comunicação	     |religião          |
|pesquisa           | terminologia         | visão geral                |esporte           |
|risco              | terapia              | pessoas                    |paisagem urbana   | 
|triagem            | causa                | política                   |bairro            |
|cirurgia           | curso                | recreação                  |turismo           |
|sintoma            | prevenção            | ciência                    |visão geral       |
|tomografia         | outros               | pontos turísticos          |tráfego           |
|tratamento         |                      | sociedade                  |economia          |
|outros             |                      | esporte                    |outros            |
|                   |                      | turismo                    |                  |
|                   |                      | transporte                 |                  |
|                   |                      | outros                     |                  |


### Divisão dos Dados

<!-- [Descreva as divisões existentes no dataset. Por exemplo, conjuntos de
treinamento, validação e teste. Forneça os tamanhos das divisões. Se achar
pertinente, forneça também estatísticas úteis de cada divisão.] -->

[ O conjunto de dados contém os resumos dos artigos, texto simples do corpo, posições de todas as seções fornecidas pelos editores da Wikipedia com seus títulos originais (por exemplo, "Causas | Sequência genética" ) e um rótulo de tópico normalizado (por exemplo, doença.causa ). Randomizamos a ordem dos documentos e os dividimos em 70% de treinamento, 10% de validação e 20% de conjuntos de teste.]


## Criação do Dataset

<!-- [Se o dataset foi construído por você, indique a fonte dos dados usados e
descreva o processo de coleta e processamento.]

[Se for um dataset já existente, indique a URL do dataset original.]

[Se o dataset existente foi modificado, descreva a modificação realizada e as
ferramentas usadas.] -->

[Este conjunto de dados contém documentos de texto completo da Wikipedia em inglês anotados com seções. Cada seção contém dois rótulos: o título original da seção desdobrada fornecido pelo editor da Wikipedia (por exemplo, Tratamento | Cirurgia) e um rótulo de classe de seção normalizado (por exemplo, doença.tratamento).
A tarefa WikiSection é atribuir a cada frase do documento uma classe de seção correspondente na qual a frase aparece. O texto do documento em si não contém informações de estrutura, como seções, subseções, parágrafos ou títulos. Caracteres de nova linha são incluídos e ocorrem entre as seções e também dentro das seções.
Os documentos são originários de dumps da Wikipedia, como CC BY-SA 3.0, disponíveis em dumps.wikimedia.org/enwiki/20180101/ (inglês) .Os conjuntos de dados são filtrados por instâncias das classes Wikidata Q12136 (doença) e Q515 (cidade), aleatorizados e divididos em subconjuntos de treinamento (70% das amostras), teste (20% das amostras) e validação (10% das amostras).
Os datasets foram traduzidos para o Português utilizando Googletrans [3], uma biblioteca Python gratuita que faz chamadas para a API AJAX do Google Tradutor acionando métodos de tradução ou detecção de idioma.
Na Tabela 2, são exibidas métricas de tamanho do dataset Wikisection e da sua versão traduzida para Português realizada pelo time de desenvolvimento. Além disso, também é mostrada a quantidade de documentos não traduzidos pela biblioteca Googletrans.
]

[O dataset Pt_disease possui 307 documentos de validação, 630 de teste e 2172 de treino com os seguintes rótulos, dispostos na Tabela 4:

|Rótulo de entrada| Rótulo de saída do script de split|
|-----------------------------------------------------|
|doença.sintoma|	0|
|doença.genética|	1|
|doença.diagnóstico|	2|
|doença.tratamento	|3|
|doença.prognóstico	|4|
|doença.outro|	5|
|doença.mecanismo|	6|
|doença.causa|	7|
|doença.epidemiologia|	8|
|doença.fauna|	9|
|doença.pesquisa|	10|
|doença.classificação|	11|
|doença.história|	12|
|doença.etimologia|	13|
|doença.patologia|	14|
|doença.tomografia|	15|
|doença.fisiopatologia|	16|
|doença.prevenção|	17|
|doença.manejo|	18|
|doença.risco|	19|
|doença.triagem	|20|
|doença.cirurgia|	21|
|doença.geografia|	22
|doença.cultura|	23|
|doença.medicação|	24|
|doença.infecção|	25|
|doença.complicação	26|
[[abela 4: Rótulos gerados pelo script de tradução para o dataset de doenças (português).]



[O daset En_city possui 1953 documentos de validação, 771 documentos de teste e 13679 documentos de treino com rótulos colocados na Tabela 5:]
|Rótulo de entrada|	Rótulo de saída do script de split|
|-----------------------------------------------------|
|city.architecture|	0|
|city.economics|	1|
|city.history|2|
|city.culture|3|
|city.geography|	4|
|city.climate|	5|
|city.politics|	6|
|city.education|	7|
|city.media|	8|
|city.sport	|9|
|city.transport	|10|
|city.other|	11|
|city.demography|	12|
|city.sights|	13|
|city.recreation|	14|
|city.facility	|15|
|city.district|	16|
|city.etymology	|17|
|city.society|	18|
|city.health|	19|
|city.infrastructure|	20|
|city.environment|	21|
|city.tourism|	22|
|city.faith| 23|
|city.international_affairs|	24|
|city.crime	|25|
|city.people|	26|
|city.law	|27|
|city.overview|	28|
|city.science|	29|
[Tabela 5: Rótulos gerados pelo script de tradução para o dataset de cidades (inglês).]


[O daset Pt_city possui 1726 documentos de validação, 3476 documentos de teste e 12240 documentos de treino com os rótulos mostrados na Tabela 6:]
|Rótulo de entrada|	Rótulo de saída do script de split|
|-----------------------------------------------------|
|cidade.arquitetura	|0|
|cidade.economia|	1|
|cidade.história|	2|
|cidade.cultura	|3|
|cidade.geografia|	4|
|cidade.clima|	5|
|cidade.política|	6|
|cidade.educação|	7|
|cidade.mídia|	8|
|cidade.esporte|	9|
|cidade.transporte|	10|
|cidade.pontosturisticos|	11|
|cidade.outro|	12|
|cidade.demografia|	13|
|cidade.fé|	14|
|cidade.facilidade|	15|
|cidade.turismo	|16|
|cidade.etimologia|	17|
|cidade.distrito|	18|
|cidade.sociedade|	19|
|cidade.recreação|	20|
|cidade.infraestrutura|21|
|cidade.assuntosinternacionais|	22|
|cidade.pessoas	|23|
|cidade.ambiente|	24|
|cidade.visaogeral|	25|
|cidade.ciência	|26|
|cidade.saúde|	27|
|cidade.lei|	28|
|cidade.crime|	29|
[Tabela 6: Rótulos gerados pelo script de tradução para o dataset de cidades (português).]



 
## Licença

<!-- [Informe qual a licença associada a este dataset.]-->

[Este conjunto de dados usa material de artigos da Wikipedia listados no arquivo SOURCES, que são lançados sob a [licença Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) .]