
from random import randint
import os
import pandas as pd
from nltk import sent_tokenize, word_tokenize
from statistics import median

def generate_segformer_docs(
    dataframe: pd.DataFrame, 
    folder: str, 
    text_body_field: str, 
    max_doc_size: int = 5, 
    category_field: str = "category",
    number_docs_list: list[int] = []
) -> pd.DataFrame:
    file_index: int = 0
    doc_order: int = 0
    
    statistics: list[dict] = []

    while doc_order < len(dataframe):
        random_doc_size: int = randint(1, max_doc_size) if len(number_docs_list) == 0 \
                                else number_docs_list[file_index]
        
        subset = dataframe.iloc[doc_order: doc_order + random_doc_size].to_dict("records")
        
        text: str = ""
        pure_text: str = ""
        
        for doc in subset:
            text += "========== ; " + doc.get(category_field, "No category") + "; " + doc.get(category_field, "")  \
            + "\n" + str(doc.get(text_body_field, "No text")) + "\n"
            
            pure_text += str(doc.get(text_body_field, "No text"))
            
        with open(os.path.join(folder, str(file_index) + ".txt" ), 'w', encoding="utf-8") as f:
            f.write(text)
            
        statistics.append(
            {
                "fulltext": pure_text,
                "number_sentences": len(sent_tokenize(pure_text)),
                "number_words": len(word_tokenize(pure_text)),
                "number_docs": random_doc_size,
                "average_words_per_sentence": len(word_tokenize(pure_text)) / len(sent_tokenize(pure_text)),
                "median_words_per_sentence": median([len(word_tokenize(st)) for st in sent_tokenize(pure_text)])
            }
        )
           
        file_index += 1
        doc_order += random_doc_size
        
    return pd.DataFrame(statistics)