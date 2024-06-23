# Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling

Versão em português do modelo oficial apresentado no Paper "**Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling**".

# Ambiente

```json
git clone git@github.com:alibaba-damo-academy/SpokenNLP.git
cd ./SpokenNLP/emnlp2023-topic_segmentation
conda create -n torch1.12.1 python=3.8
source activate torch1.12.1
pip install -r requirements.txt
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
Além disso, faça o download do Punkt Tokenizer Model em [here](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip),
então `unzip punkt.zip` e mova para a pasta `path/to/your/anaconda3/envs/torch1.12.1/share/nltk_data/tokenizers`.
# Dataset

Depois de baixar e descompactar os dados, incluindo WikiSection, Elements e WIKI-50, você precisa especificar o caminho dos dados-fonte em ./config/config.ini. Note que, após descompactar WikiSection executando unzip WikiSection-master.zip, você precisará executar cd WikiSection-master && tar -xvzf wikisection_dataset_json.tar.gz para obter os dados.

Então, você pode executar bash run_process_data.sh para processar os dados no formato unificado necessário na pasta ./data.


# Treinamento
Altere alguns parâmetros-chave como model_name e dataset em run_finetune.py.

Depois, execute run_finetune.py.

# Inferência
Altere alguns parâmetros-chave como model_name e model_path em run_inference.py

Depois, execute bash run_inference.py


# Citação

```
@article{improving,
  title={Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling},
  author={Hai Yu, Chong Deng, Qinglin Zhang, Jiaqing Liu, Qian Chen, Wen Wang},
  journal={arXiv preprint arXiv:2310.11772},
  year={2023}
}
```

# Licença

Licenciado sob a [Apache License 2.0](https://github.com/alibaba-damo-academy/SpokenNLP/blob/main/LICENSE). Este projeto contém vários componentes de terceiros sob outras licenças de código aberto.
=======
# Projeto: Segmentação textual automática

Residência Tecnológica em 2023

Time 6 - Projeto: Segmentação textual automática baseada em tópicos
