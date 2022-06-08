import yaml
from pathlib import Path
import os
import openai

BASE_DIR = Path(__file__).resolve().parent
data = open(f"{BASE_DIR}/keys.yaml", mode="r")
data = yaml.safe_load(data)

data_text = open(f"{BASE_DIR}/training_data.txt", mode="r", encoding="utf-8")
data_val = open(f"{BASE_DIR}/data_validar.txt", mode="r", encoding="utf-8")


openai.api_key = data["passkey"]

prompt = str(data_text.read()) + str(data_val.read())
response = openai.Completion.create(
    engine="text-davinci-002", prompt=prompt, max_tokens=20
)

print(response['choices'][0]['text'])