# Segformer - manual de treinamento

Este documento traz um manual com os passos necessários para realizar o treinamento do modelo Segformer [1]. As subseções se seguem conforme a lista a seguir:

- **Requisitos**: requisitos mínimos da máquina para processar o modelo;
- **Pré-processamento**: etapas para processamento dos dados de entrada para o formato esperado pelo modelo;
- **Treinamento**: etapas para realização do treinamento do modelo propriamente dito, explicitando os seus parâmetros de entrada com suas respectivas descrições.

## Requisitos

## Instalação de dependências
São necessárias algumas bibliotecas externas em linguagem Python, que são instaladas executando o comando:

`pip install -r requirements.txt`

## Pré-processamento

Antes da realização das seguintes etapas de pré-processamento, deve-se descarregar os *datasets* utilizados para treinar o modelo através da *URL* https://github.com/sebastianarnold/WikiSection (usar o arquivo **wikisection_dataset_ref.tar.gz**). Estes fazem parte da coleção **WikiSection**, conjunto de verbetes da **Wikipedia** em inglês e alemão. O artefato descarregado é um arquivo compactado; para utilizá-los, deve-se extrai-los e colocá-los na raiz deste repositório. Cada um dos diretórios gerados da extração corresponde a um *dataset* específico:

- **en_city**: *dataset* de cidades (inglês);
- **en_disease**: *dataset* de doenças (inglês);
- **de_disease**: *dataset* de doenças (alemão);
- **de_city**: *dataset* de cidades (alemão);

No projeto em desenvolvimento, foram utilizados os conjuntos de dados em inglês (**en_disease** e **en_city**). A partir deste ponto, siga os passos:

- Mova os diretórios gerados para a raiz do repositório **transformers** (o mesmo no qual se situa o *script* **splittrainvaltest.py**). **Obs.:** Para cada *dataset*, a extração produz três diretórios: um com amostras de treino, outro de teste e um terceiro de validação. Exemplo: para **en_disease**, são produzidas as pastas **en_disease_train**, **en_disease_test** e **en_disease_validation**;

- Edite o *script* **splittrainvaltest.py** na linha 3, alterando o valor presente na lista **datasets** para o *dataset* a ser pré-processado. Exemplo: se desejar submeter **en_disease** ao pré-processamento, insira **en_disease_** no elemento da lista. É possível fornecer como entrada mais de um *dataset*, o que motiva a formatação da variável como lista.

- Definido o *dataset*, execute o *script* de pré-processamento:
`python splittrainvaltest.py`

- No mesmo diretório do *script*, são produzidos três diretórios: **train** (conjunto de treino), **test** (conjunto de teste) e **val** (conjunto de validação). Dentro de cada um deles, para cada documento do conjunto, existe um correspondente nas pastas **label1**, **label2** e **text**, que consistem em:

    - **label1**: indica se a sentença do documento na respectiva linha representa uma fronteira de tópico (1) ou não (0). Deve-se ressaltar que as sentenças dos documentos dos *datasets* estão divididas em linhas separadas;
    - **label2**: define a qual tópico a sentença pertence. Ao longo da execução do *script* de pré-processamento, cada novo tópico que vai sendo identificado é representado por um número incrementado automaticamente (0, 1, 2, etc.);
    - **text**: o texto do documento propriamente dito.

Mova os diretórios mencionados para dentro de **examples/pytorch/sequence_labeling**:

```bash
mv train examples/pytorch/sequence_labeling
mv test examples/pytorch/sequence_labeling
mv val examples/pytorch/sequence_labeling
```

## Treinamento

Para executar o treinamento do modelo:

- Mova-se para dentro do diretório **examples/pytorch/sequence_labeling**;
- Execute o *script* **run_language_modeling.py** passando os seguintes parâmetros:

| Parâmetro | Descrição |
|-------------|---------------|
| output_dir | Diretório de saída do modelo |
| model_type | Tipo do modelo (*e.g*: **bert**) |
| model_name_or_path | Nome ou caminho do modelo (*e.g*: **bert_base_uncased**) |
| do_train | Realizar treinamento (caso apenas passado, assume valor padrão **True**) |
| do_eval | Realizar avaliação sobre o conjunto de avaliação (caso apenas passado, assume valor padrão **True**) |
| evaluate_during_training | Realizar processos de treinamento e avaliação simultaneamente |
| train_data_file | Nome e caminho do arquivo no qual será salvo os *checkpoints* de treinamento |
| eval_data_file | Nome e caminho do arquivo no qual será salvo os *checkpoints* de teste |
| block_size | Tamanho do bloco de entrada do *BERT* |
| num_train_epochs | Número de épocas de treinamento |
| warmup_steps | Número de passos de aquecimento |
| logging_steps | Intervalo (medido em passos) para cada *log* no console |
| save_steps | Número de passos de salvamento de *checkpoints* |
| per_device_train_batch_size | Tamanho do lote de treinamento por dispositivo (no caso, por processador) |
| gradient_accumulation_steps | Número de passos de acumulação de gradiente |
| evaluation_strategy | Estratégia de avaliação (se o valor for *step*, por exemplo, a avaliação é realizada a cada passo) |
| per_device_train_batch_size | Tamanho do lote de avaliação por dispositivo (no caso, por processador) |
| label_num | Número total de rótulos de tópicos existentes no *dataset* |
| line_by_line | Indica se cada linha do documento deve ser considerada como uma sequência distinta. Se passado, assume valor **True** por padrão |
| overwrite_output_dir | Indica se o conteúdo do diretório de saída deve ser sobrescrito a cada ponto de controle. Se passado, assume valor **True** por padrão |
| save_total_limit | Limite de *checkpoints* no diretório de saída |
