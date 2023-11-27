import json
import tiktoken
import numpy as np
from collections import defaultdict
# gpt-4, turbo, text-embedding-ada-002のモデルで使われるデフォルトのエンコーディングを設定する
encoding = tiktoken.get_encoding("cl100k_base") 
def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens

def num_assistant_tokens_from_messages(messages):
    num_tokens = 0
    for message in messages:
        if message["role"] == "assistant":
            num_tokens += len(encoding.encode(message["content"]))
    return num_tokens

def print_distribution(values, name):
    print(f"\n#### Distribution of {name}:")
    print(f"min / max: {min(values)}, {max(values)}")
    print(f"mean / median: {np.mean(values)}, {np.median(values)}")
    print(f"p5 / p95: {np.quantile(values, 0.1)}, {np.quantile(values, 0.9)}")

files = ['training_set.jsonl', 'validation_set.jsonl']

for file in files:
    print(f"Processing file: {file}")
    with open(file, 'r', encoding='utf-8') as f:
        dataset = [json.loads(line) for line in f]
        total_tokens = []
        assistant_tokens = []
 
    for ex in dataset:
        messages = ex.get("messages", {})
        total_tokens.append(num_tokens_from_messages(messages))
        assistant_tokens.append(num_assistant_tokens_from_messages(messages))
 
    print_distribution(total_tokens, "total tokens")
    print_distribution(assistant_tokens, "assistant tokens")
    print('*' * 50)