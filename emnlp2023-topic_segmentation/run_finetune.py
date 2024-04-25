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
model_name = 'google-bert/bert-base-uncased'
dataset = 'wiki_section'
dataset_cache_dir = f'./cached_data/{dataset}_{model_name}_{max_seq_length}'

num_train_epochs = 5
lr = 5e-5
per_device_train_batch_size = 2
gradient_accumulation_steps = 2

do_da_ts = True
do_cssl = True
do_tssp = True

ts_loss_weight = 1.0
cl_loss_weight = 0.5
cl_temp = 0.1
cl_anchor_level = 'eop_list'
cl_positive_k = 1
cl_negative_k = 3
tssp_loss_weight = 1.0

for seed in [42, 59, 88]:
    bs = NUM_GPU * per_device_train_batch_size * gradient_accumulation_steps
    currentTime = subprocess.check_output(["date", "+%Y-%m-%d_%H:%M:%S"]).decode().strip()
    OUTPUT_DIR = f'./output/{model_name}-finetune-{dataset}/seed{seed}-seq{max_seq_length}-lr{lr}-epoch{num_train_epochs}-bs{bs}-ts{ts_loss_weight}-tssp{tssp_loss_weight}-cl{cl_loss_weight}-{currentTime}'
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    LOGFILE = f'{OUTPUT_DIR}/run.log'
    print(f"write log into {LOGFILE}")

    with open(LOGFILE, 'a') as log_file:
        log_file.write(f"{os.environ['CUDA_VISIBLE_DEVICES']}\n")

        subprocess.run([
            'python', './src/ts_sentence_seq_labeling.py',
            f'--dataset_name=./src/datasets/{dataset}',
            f'--model_name_or_path={model_name}',
            f'--dataset_cache_dir={dataset_cache_dir}',
            f'--metric_name={metric_name}',
            '--gradient_checkpointing=False',
            '--do_train=True',
            '--do_eval=True',
            '--do_predict=True',
            f'--seed={seed}',
            f'--max_seq_length={max_seq_length}',
            f'--num_gpu={NUM_GPU}',
            f'--learning_rate={lr}',
            f'--num_train_epochs={num_train_epochs}',
            f'--per_device_train_batch_size={per_device_train_batch_size}',
            f'--gradient_accumulation_steps={gradient_accumulation_steps}',
            '--per_device_eval_batch_size=4',
            '--evaluation_strategy=steps',
            f'--eval_cnt={num_train_epochs}',
            '--load_best_model_at_end',
            '--save_total_limit=2',
            '--metric_for_best_model=overall_f1',
            '--eval_accumulation_steps=1000',
            '--overwrite_output_dir',
            '--preprocessing_num_workers=5',
            f'--ts_loss_weight={ts_loss_weight}',
            f'--do_da_ts={do_da_ts}',
            f'--do_cssl={do_cssl}',
            f'--do_tssp={do_tssp}',
            f'--cl_loss_weight={cl_loss_weight}',
            f'--cl_temp={cl_temp}',
            f'--cl_anchor_level={cl_anchor_level}',
            f'--cl_positive_k={cl_positive_k}',
            f'--cl_negative_k={cl_negative_k}',
            f'--tssp_loss_weight={tssp_loss_weight}',
            f'--output_dir={OUTPUT_DIR}'
        ], stdout=log_file, stderr=subprocess.STDOUT)

        log_file.write("Run postprocess_predictions to get sent level metric\n")
        data_file = f'./data/{dataset}/test.jsonl'
        pred_file = f'{OUTPUT_DIR}/predict_wiki_section_max_seq{max_seq_length}_ts_score_lt.txt'
        subprocess.run(['python', './src/postprocess_predictions.py', data_file, pred_file], stdout=log_file, stderr=subprocess.STDOUT)

        log_file.write("Save sent level metric\n")

    print("Training and post-processing completed.")
