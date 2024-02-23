

import requests, uuid, os
from dotenv import load_dotenv


# Add your key and endpoint
key = os.environ["AZURE_TRANSLATION_API_KEY"]
endpoint = os.environ["AZURE_TRANSLATION_API_BASE_URL"]

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = os.environ["AZURE_TRANSLATION_API_RESOURE_LOCATION"]

input_location = "segformer/en_disease_validation" # pasta com dataset original
output_location = "segformer/output_azure_train" # pasta com as traduções

params = {
    "api-version": "3.0",
    "from": "en",
    "to": ["pt"]
}

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Ocp-Apim-Subscription-Region": location,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4())
}


for root, dir, files in os.walk(input_location):
    for file in files:
        if file.endswith('.ref'):
            new_file = "{}_translated.txt".format(file.split('.')[0])

            # faz a leitura dos arquivos
            with open(os.path.join(root, file), 'r') as f:
                file_contents = f.read()
                
            body = {
                "text": file_contents
            }    

            # traduz os arquivos
            api_response = requests.post(endpoint + "/translate", params=params, headers=headers, json=body).json()

            # salva os novos arquivos traduzidos em outra pasta
            with open(os.path.join(output_location, new_file), 'w') as f:
                f.write(api_response.text)
