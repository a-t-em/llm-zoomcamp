import requests
import json
import tiktoken

url = "http://localhost:11434/api/generate"
#prompt = "10 * 10"
prompt = "What's the formula for energy?"
llm_response = requests.post(url, json={"model": "gemma:2b", "prompt": prompt})

decoded_content = llm_response.content.decode("utf-8")
json_objects = decoded_content.split("\n")

sentence = ""
for i in range(len(json_objects)):
    parsed_text = json.loads(json_objects[i])['response']
    sentence += parsed_text
print(sentence)

encoding = tiktoken.get_encoding("o200k_base")
result = encoding.encode(sentence)
print('number of tokens in the response', len(result))
