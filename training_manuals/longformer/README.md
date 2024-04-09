# Segformer - manual de treinamento

Este documento traz um manual com os passos necessários para realizar o treinamento do modelo LongFormer [2]. As subseções se seguem conforme a lista a seguir:

- **Requisitos**: requisitos mínimos da máquina para processar o modelo;
- **Pré-processamento**: etapas para processamento dos dados de entrada para o formato esperado pelo modelo;
- **Treinamento**: etapas para realização do treinamento do modelo propriamente dito, explicitando os seus parâmetros de entrada com suas respectivas descrições.

## Requisitos

## Instalação de dependências
São necessárias algumas bibliotecas externas em linguagem Python, que são instaladas executando o comando:

`pip install -r requirements.txt`

Instalar também bibliotecas do **PyTorch** na seguinte versão:

```bash
pip install torch==1.12.1+cu113
```

Também deve-se descarregar o tokenizador presente em https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip, descompactar o arquivo e movê-lo para o diretório interno **/share/nltk_data/tokenizer** da biblioteca do **PyTorch** recém instalada.

## Pré-processamento

Antes da realização das seguintes etapas de pré-processamento, deve-se descarregar os *datasets* utilizados para treinar o modelo através da *URL* https://github.com/sebastianarnold/WikiSection (usar o arquivo **wikisection_dataset_ref.tar.gz**). Estes fazem parte da coleção **WikiSection**, conjunto de verbetes da **Wikipedia** em inglês e alemão. O artefato descarregado é um arquivo compactado; para utilizá-los, deve-se extrai-los e colocá-los na raiz deste repositório. Cada um dos diretórios gerados da extração corresponde a um *dataset* específico:

- **en_city**: *dataset* de cidades (inglês);
- **en_disease**: *dataset* de doenças (inglês);
- **de_disease**: *dataset* de doenças (alemão);
- **de_city**: *dataset* de cidades (alemão);

No projeto em desenvolvimento, foram utilizados os conjuntos de dados em inglês (**en_disease** e **en_city**). A partir deste ponto, siga os passos:

--TODO--

## Utilização de modelos pré-treinados

--TODO--

## Treinamento

Para executar o treinamento do modelo, execute o *script* **run_finetune.sh**, modificando alguns de seus parâmetros, como **model_name** e **num_train_epochs**, por exemplo:


```bash
./run_finetune.sh
```

## Teste

Para executar o treinamento do modelo, execute o *script* **run_inference.sh**, modificando alguns de seus parâmetros, como **model_name** e **max_seq_length**, por exemplo:


```bash
./run_inference.sh
```

