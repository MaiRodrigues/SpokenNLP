# Versão em português do modelo oficial apresentado no Paper "**Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling**".

## Dados Gerais

- **Nome:** Segmentação de Tópicos para o Português Brasileiro
- **Tipo:** Bidirectional Encoder-only
- **Licença:** [Apache License 2.0](https://github.com/alibaba-damo-academy/SpokenNLP/blob/main/LICENSE)
- **Modelo base:** [emnlp2023-topic_segmentation](https://github.com/alibaba-damo-academy/SpokenNLP/tree/main/emnlp2023-topic_segmentation)

## Utilização Pretendida

Este modelo deve ser utilizado para segmentação de texto baseada em tópicos onde o objetivo é a identificação de fronteiras semânticas em um texto longo. Não deve ser utilizado para Extração de Tópicos onde dado um texto longo, busca-se extrair tópicos através de palavras-chave.

## Arquiteturas

- **neuralmind/bert-base-portuguese-cased**:         Arq: BERT-Base        Layers: 12         Parâmetros: 110M
- **neuralmind/bert-large-portuguese-cased**:        Arq: BERT-Large       Layers: 24         Parâmetros: 335M

## Preparação do Ambiente

- **Clonar o repositório**: descarregar o repositório com o código fonte do modelo em máquina local;
- **Requisitos**: requisitos mínimos da máquina para processar o modelo;
- **Pré-processamento**: etapas para processamento dos dados de entrada para o formato esperado pelo modelo;
- **Treinamento**: etapas para realização do treinamento do modelo propriamente dito, explicitando os seus parâmetros de entrada com suas respectivas descrições.

## Clonar o repositório
O código fonte do modelo **Longformer []** está disponível no repositório acessível por https://github.com/alibaba-damo-academy/SpokenNLP, hospedado na plataforma **Github**. Para descarregá-lo em máquina local, execute:

```bash
git clone git@github.com:alibaba-damo-academy/SpokenNLP.git
```

**Obs.:** Caso utilize outra forma para a operação de *clone* (**HTTPS** ou *CLI* do *Github*, por exemplo), executar o comando correspondente.

Depois, mova para a pasta **SpokenNLP/emnlp2023-topic_segmentation**:

```bash
cd ./SpokenNLP/emnlp2023-topic_segmentation
```

## Requisitos

Versão python=3.8

## Instalação de dependências
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

## Pré-processamento

Antes da realização das seguintes etapas de pré-processamento, deve-se descarregar os *datasets* utilizados para treinar o modelo https://github.com/CPqD/resid2023-nlp-6/tree/main/datasets/wikisection. Estes fazem parte da coleção **WikiSection** (https://github.com/sebastianarnold/WikiSection), conjunto de verbetes da **Wikipedia** em inglês que foram traduzidos para o português. O artefato descarregado é um arquivo compactado; para utilizá-los, deve-se extrai-los e colocá-los na raiz deste repositório. Cada um dos diretórios gerados da extração corresponde a um *dataset* específico:

- **pt_city**: *dataset* de cidades;
- **pt_disease**: *dataset* de doenças;

O modelo também utiliza mais três *datasets* para treinamento e avaliação: **Elements** (https://groups.csail.mit.edu/rbg/code/mallows/) e **WIKI-50** (https://github.com/koomri/text-segmentation). Seguindo os procedimentos para geração/extração dos conjuntos, deve-se especificar a localização deles no arquivo `./config/config.ini` (para o caso de **Wikisection**, deve-se extrair o arquivo **wikisection_dataset_json.tar.gz**, onde **_dataset** corresponde a um conjunto dos quatro supracitados que se deseja utilizar).

Concluídas as últimas etapas, executar o script **run_proccess_data.sh**:

```bash
./run_process_data.sh
```

As saídas do pré-processamento dos *datasets* será automaticamente depositada na pasta **./data**.
## Utilização de modelos pré-treinados

Caso seja necessário realizar download dos modelos pré-treinados, descarregue-os e insira-os no diretório `./pretrained_models`.

- **neuralmind/bert-large-portuguese-cased**: https://huggingface.co/neuralmind/bert-large-portuguese-cased;
- **neuralmind/bert-base-portuguese-cased**: https://huggingface.co/neuralmind/bert-base-portuguese-cased;

Estes dois modelos estão disponíveis em **HuggingFace**. Para utilização no treinamento deste, ao abrir a respectiva página do modelo, vá até a seção **Files and Versions** e descarregue o arquivo denominado **pytorch_model.bin**.

## Treinamento

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

## Teste

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
