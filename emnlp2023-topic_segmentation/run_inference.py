import subprocess
import os
import random

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
NUM_GPU = 1
print(os.environ['CUDA_VISIBLE_DEVICES'])
print(NUM_GPU)

PORT_ID = random.randint(1000, 9999)
os.environ['OMP_NUM_THREADS'] = '8'

metric_name = './src/metrics/seqeval.py'

max_seq_length = 512

model_name = 'neuralmind/bert-large-portuguese-cased'

model_path = './output/neuralmind/bert-large-portuguese-cased-finetune-wiki_section_disease/seed42-seq512-lr5e-05-epoch1-bs4-ts1.0-tssp1.0-cl0.5-2024-05-08_12:14:51'

dataset = 'wiki50'

for dataset in ['wiki50']:
    dataset_cache_dir = f'./cached_data/{dataset}_{model_name}_{max_seq_length}'
    LOGFILE = f'{model_path}/infer.log'
    print(f"write log into {LOGFILE}")
    with open(LOGFILE, 'a') as log_file:
        log_file.write(f"{os.environ['CUDA_VISIBLE_DEVICES']}\n")

        subprocess.run([
            'python', './src/ts_sentence_seq_labeling.py',
            f'--model_name_or_path={model_path}',
            f'--dataset_name=./src/datasets/{dataset}',
            f'--dataset_cache_dir={dataset_cache_dir}',
            f'--metric_name={metric_name}',
            '--gradient_checkpointing=False',
            '--do_train=False',
            '--do_eval=False',
            '--do_predict=True',
            f'--max_seq_length={max_seq_length}',
            f'--num_gpu={NUM_GPU}',
            '--per_device_eval_batch_size=4',
            '--overwrite_output_dir=False',
            '--preprocessing_num_workers=5',
            f'--output_dir={model_path}'
        ], stdout=log_file, stderr=subprocess.STDOUT)

        if dataset == 'wiki50':
            log_file.write("run postprocess_predictions to get_wiki_section_sent_level_metric\n")
            log_file.write(f"then save sent level metric in {LOGFILE}\n")
            data_file = f'./data/{dataset}/test'
            pred_file = f'{model_path}/predict_wiki_section_disease_max_seq{max_seq_length}_ts_score_lt.txt'
            subprocess.run(['python', './src/postprocess_predictions.py', data_file, pred_file], stdout=log_file, stderr=subprocess.STDOUT)

    print("Inference completed.")
