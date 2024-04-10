
from random import randint
import os
import pandas as pd

def generate_segformer_docs(dataframe: pd.DataFrame, folder: str, text_body_field: str, max_doc_size: int = 5, category_field: str = "category") -> None:
    file_index: int = 0
    doc_order: int = 0

    while doc_order < len(dataframe):
        random_doc_size: int = randint(1, max_doc_size)
        
        subset = dataframe.iloc[doc_order: doc_order + random_doc_size].to_dict("records")
        print(subset)
        text: str = ""
        
        for doc in subset:
            text += "========== ; " + doc.get(category_field, "No category") + "; " + doc.get(category_field, "")  \
            + "\n" + str(doc.get(text_body_field, "No text")) + "\n"
            
        with open(os.path.join(folder, str(file_index) + ".txt" ), 'w', encoding="utf-8") as f:
            f.write(text)
                        
        file_index += 1
        doc_order += random_doc_size