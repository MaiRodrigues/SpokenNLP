# Versão em português do modelo oficial apresentado no Paper "**Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling**".

## Dados Gerais

- **Nome:** Segmentação de Tópicos para o Português Brasileiro
- **Tipo:** Bidirectional Encoder-only
- **Licença:** [Apache License 2.0](https://github.com/alibaba-damo-academy/SpokenNLP/blob/main/LICENSE)
- **Modelo base:** [emnlp2023-topic_segmentation](https://github.com/alibaba-damo-academy/SpokenNLP/tree/main/emnlp2023-topic_segmentation)

## Utilização Pretendida

Este modelo deve ser utilizado para segmentação de texto baseada em tópicos onde o objetivo é a identificação de fronteiras semânticas em um texto longo. Não deve ser utilizado para Extração de Tópicos onde dado um texto longo, busca-se extrair tópicos através de palavras-chave.

## Arquiteturas

A Figura 1 exibe uma visão geral da arquitetura do modelo, composta por três principais componentes: uma camada de geração de *embeddings*, um codificador e um modelo de aprendizado profundo. A reunião dos três, em conjunto, pode ser realizada por meio de *transformers* bidirecionais (como *BERT*, por exemplo).

<div align = center>
  <img src="./img/modelo.png" />
  <figcaption>Figura 1: Esquemático em alto nível da proposta. Adaptado de [1].</figcaption>
</div>
<br> <br>

O treinamento do modelo é realizado de forma iterativa visando minimizar uma função de perda (denotada na figura mencionada como **Lts**). Além da mensuração da perda por entropia cruzada, outras duas funções são aplicadas para aprimorar a assertividade do segmentador, tratadas nas tarefas TSSP e CSSL . Para a primeira o texto de entrada é submetido a um processo de aumento de dados, no qual suas sentenças e tópicos são intercambiados internamente; a segunda, em contrapartida, é alimentada pelos documentos originais. Para mais informações sobre as funções de perda mencionadas, consultar [1].

Apesar de [1] ter avaliado uma série de diferentes modelos, a equipe de trabalho, a princípio, concentrou-se em realizar treinamento e inferência com o modelo base do BERT [2] e o BERTimbau [3], variação do primeiro treinado com conjuntos de dados em Língua Portuguesa de diferentes domínios temáticos. Ao longo da evloução do trabalho, escolheu-se o segundo modelo como ponto de partida para treinamento, o qual é disponibilizado em duas versões: **Base** e **Large**. Seguem as especificações de ambas:

- **neuralmind/bert-base-portuguese-cased**:
    -  BERT-Base
    -  Layers: 12
    -  Parâmetros: 110M

- **neuralmind/bert-large-portuguese-cased**:
    - Arq: BERT-Large
    - Layers: 24
    - Parâmetros: 335M

## Guia rápido de utilização

### Preparação do Ambiente

- **Clonar o repositório**: descarregar o repositório com o código fonte do modelo em máquina local;
- **Requisitos**: requisitos mínimos da máquina para processar o modelo;
- **Pré-processamento**: etapas para processamento dos dados de entrada para o formato esperado pelo modelo;
- **Treinamento**: etapas para realização do treinamento do modelo propriamente dito, explicitando os seus parâmetros de entrada com suas respectivas descrições.

### Clonar o repositório

O código fonte do projeto está disponível no repositório acessível por https://github.com/MaiRodrigues/SpokenNLP, hospedado na plataforma **Github**. Este, por sua vez, foi derivado de https://github.com/alibaba-damo-academy/SpokenNLP.  Para descarregá-lo em máquina local, execute:

```bash
git clone git@github.com:MaiRodrigues/SpokenNLP.git
```

**Obs.:** Caso utilize outra forma para a operação de *clone* (**HTTPS** ou *CLI* do *Github*, por exemplo), executar o comando correspondente.

Depois, mova para a pasta **SpokenNLP/emnlp2023-topic_segmentation**:

```bash
cd ./SpokenNLP/emnlp2023-topic_segmentation
```

### Requisitos

Versão python=3.8

### Instalação de dependências
São necessárias algumas bibliotecas externas em linguagem Python, que são instaladas executando o comando:

`pip install -r requirements.txt`

Instalar também bibliotecas do **PyTorch** na seguinte versão:

```bash
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```

Também deve-se descarregar o tokenizador **punkt**, que utiliza o sinal gráfico de ponto final para segmentar o documento em sentenças. Para tanto, abra um terminal interativo do **Python** e execute:

```python
>>> import nltk
>>> nltk.download("punkt")
```

### Pré-processamento

Antes da realização das seguintes etapas de pré-processamento, deve-se descarregar os *datasets* utilizados para treinar o modelo (https://github.com/CPqD/resid2023-nlp-6/tree/main/datasets/wikisection). Estes fazem parte da coleção **WikiSection** (https://github.com/sebastianarnold/WikiSection), conjunto de verbetes da **Wikipedia** em inglês que foram traduzidos para o português. O artefato descarregado é um arquivo compactado; para utilizá-los, deve-se extrai-los e colocá-los na raiz deste repositório. Cada um dos diretórios gerados da extração corresponde a um *dataset* específico:

- **pt_city**: *dataset* de cidades;
- **pt_disease**: *dataset* de doenças;

O modelo também utiliza mais um dataset para avaliação: **WIKI-50** (https://github.com/CPqD/resid2023-nlp-6/tree/main/datasets/wiki50). Seguindo os procedimentos para geração/extração dos conjuntos, deve-se especificar a localização no arquivo `./config/config.ini`.

Concluídas as últimas etapas, executar o script **run_proccess_data.sh**:

```bash
./run_process_data.sh
```

As saídas do pré-processamento dos *datasets* será automaticamente depositada na pasta **./data**.
### Utilização de modelos pré-treinados

Caso seja necessário realizar download dos modelos pré-treinados, descarregue-os e insira-os no diretório `./pretrained_models`.

- **neuralmind/bert-large-portuguese-cased**: https://huggingface.co/neuralmind/bert-large-portuguese-cased;
- **neuralmind/bert-base-portuguese-cased**: https://huggingface.co/neuralmind/bert-base-portuguese-cased;

Estes dois modelos estão disponíveis em **HuggingFace**. Para utilização no treinamento deste, ao abrir a respectiva página do modelo, vá até a seção **Files and Versions** e descarregue o arquivo denominado **pytorch_model.bin**.

### Treinamento

Para executar o treinamento do modelo, execute o *script* **run_finetune.py**, modificando alguns de seus parâmetros, como **model_name** e **num_train_epochs**, por exemplo:


```bash
./run_finetune.sh
```

Os possíveis parâmetros de configuração da execução do treinamento são:

- **metric_name**: nome da métrica. Pode-se modificar para quaisquer uma delas disponíves em `./src/metrics/`
- **ma_seq_length**: comprimento máximo de sequência analisado pelo modelo;
- **dataset_name**: nome do *dataset*;
- **num_gpu**: número de processadores de GPU para executar paralelamente o treinamento;
- **gradient_checkpoing**: booleano para indiciar se os *checkpoints do gradiente descendente devem ser salvos;
- **learning_rate**: *learning rate* do treinamento;
- **num_train_epochs**: número de épocas de treinamento;

**OBS.:** Para utilizar o modelo descrito por este cartão, preencha a variável **model_name** com o valor "cpqd/residencia_time_6_nlp".

### Teste

Para executar o treinamento do modelo, execute o *script* **run_inference.py**, modificando alguns de seus parâmetros, como **model_name** e **max_seq_length**, por exemplo:


```bash
./run_inference.sh
```

Os possíveis parâmetros de configuração da execução do teste são:

- **metric_name**: nome da métrica. Pode-se modificar para quaisquer uma delas disponíves em `./src/metrics/`
- **ma_seq_length**: comprimento máximo de sequência analisado pelo modelo;
- **dataset_name**: nome do *dataset*;
- **num_gpu**: número de processadores de GPU para executar paralelamente o treinamento;
- **gradient_checkpoing**: booleano para indiciar se os *checkpoints do gradiente descendente devem ser salvos;

**OBS.:** Para utilizar o modelo descrito por este cartão, preencha a variável **model_name** com o valor "cpqd/residencia_time_6_nlp".

## Referências

- [1] Hai Yu, Chong Deng, Qinglin Zhang, Jiaqing Liu, Qian Chen, and Wen Wang. 2023. Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 5592–5605, Singapore. Association for Computational Linguistics. 

- [2] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, Minneapolis, Minnesota. Association for Computational Linguistics. 

- [3] F.C. Souza, R.F. Nogueira, R.A. Lotufo, BERT models for Brazilian Portuguese: Pretraining, evaluation and tokenization analysis, Applied Soft Computing, Volume 149, Part A, 2023, 110901, ISSN 1568-4946, https://doi.org/10.1016/j.asoc.2023.110901. (https://www.sciencedirect.com/science/article/pii/S1568494623009195).  
