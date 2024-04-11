# Segformer - manual de treinamento

Este documento traz um manual com os passos necessários para realizar o treinamento do modelo LongFormer [2]. As subseções se seguem conforme a lista a seguir:

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

## Instalação de dependências
São necessárias algumas bibliotecas externas em linguagem Python, que são instaladas executando o comando:

`pip install -r requirements.txt`

Instalar também bibliotecas do **PyTorch** na seguinte versão:

```bash
pip install torch==1.12.1+cu113
```

Também deve-se descarregar o tokenizador **punkt**, que utiliza o sinal gráfico de ponto final para segmentar o documento em sentenças. Para tanto, abra um terminal interativo do **Python** e execute:

```python
>>> import nltk
>>> nltk.download("punkt")
```

## Pré-processamento

Antes da realização das seguintes etapas de pré-processamento, deve-se descarregar os *datasets* utilizados para treinar o modelo através da *URL* https://github.com/sebastianarnold/WikiSection (usar o arquivo **wikisection_dataset_ref.tar.gz**). Estes fazem parte da coleção **WikiSection**, conjunto de verbetes da **Wikipedia** em inglês e alemão. O artefato descarregado é um arquivo compactado; para utilizá-los, deve-se extrai-los e colocá-los na raiz deste repositório. Cada um dos diretórios gerados da extração corresponde a um *dataset* específico:

- **en_city**: *dataset* de cidades (inglês);
- **en_disease**: *dataset* de doenças (inglês);
- **de_disease**: *dataset* de doenças (alemão);
- **de_city**: *dataset* de cidades (alemão);

No projeto em desenvolvimento, foram utilizados os conjuntos de dados em inglês (**en_disease** e **en_city**). 

O modelo também utiliza mais três *datasets* para treinamento e avaliação: **Elements** (https://groups.csail.mit.edu/rbg/code/mallows/), **WIKI-727K** (https://github.com/koomri/text-segmentation) e **WIKI-50** (https://github.com/koomri/text-segmentation). Seguindo os procedimentos para geração/extração dos conjuntos, deve-se especificar a localização deles no arquivo `./config/config.ini` (para o caso de **Wikisection**, deve-se extrair o arquivo **wikisection_dataset_json.tar.gz**, onde **_dataset** corresponde a um conjunto dos quatro supracitados que se deseja utilizar).

Concluídas as últimas etapas, executar o script **run_proccess_data.sh**:

```bash
./run_process_data.sh
```

As saídas do pré-processamento dos *datasets* será automaticamente depositada na pasta **./data**.
## Utilização de modelos pré-treinados

Caso seja necessário utilizar modelos pré-treinados, descarregue-os e insira-os no diretório `./pretrained_models`. Os modelos suportados pelo projeto são:

- **longformer_base**: https://huggingface.co/allenai/longformer-base-4096/;
- **bigbird_base**: https://huggingface.co/google/bigbird-roberta-base/;
- **bert_base**: https://huggingface.co/bert-base-uncased/;
- **electra_base**: https://huggingface.co/google/electra-base-discriminator;

Estes quatro modelos estão disponíveis em **HuggingFace**. Para utilização no treinamento deste, ao abrir a respectiva página do modelo, vá até a seção **Files** e descarregue o arquivo com extensão **.bin**.

## Treinamento

Para executar o treinamento do modelo, execute o *script* **run_finetune.sh**, modificando alguns de seus parâmetros, como **model_name** e **num_train_epochs**, por exemplo:


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

Para executar o treinamento do modelo, execute o *script* **run_inference.sh**, modificando alguns de seus parâmetros, como **model_name** e **max_seq_length**, por exemplo:


```bash
./run_inference.sh
```

Os possíveis parâmetros de configuração da execução do teste são:

- **metric_name**: nome da métrica. Pode-se modificar para quaisquer uma delas disponíves em `./src/metrics/`
- **ma_seq_length**: comprimento máximo de sequência analisado pelo modelo;
- **dataset_name**: nome do *dataset*;
- **num_gpu**: número de processadores de GPU para executar paralelamente o treinamento;
- **gradient_checkpoing**: booleano para indiciar se os *checkpoints do gradiente descendente devem ser salvos;
- **learning_rate**: *learning rate* do treinamento;
- **num_train_epochs**: número de épocas de treinamento;


