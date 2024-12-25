from transformers import AutoTokenizer
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
api_url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-32B-Instruct")
def ask(web="", message=False, mnt=1000):
    if message == False:
        message = [
            {
                "role": "system",
                "content": "You are an expert at understanding the html code behind websites"
            },
            {
                "role": "user",
                "content": f"Outline the Buttons, Text, Input fields, Tables and links in this html {web}, return your response in json format"
            }
        ]
    prompt = tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True)
    data = {
        "inputs":prompt,
        "parameters": {
            "max_new_tokens": mnt,
            "return_full_text":False
        }
    }
    output = query(data)
    return output[0]['generated_text']