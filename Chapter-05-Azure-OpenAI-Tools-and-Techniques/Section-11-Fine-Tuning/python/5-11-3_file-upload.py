import openai
import os
openai.api_key = "YOUR AZURE OPENAI API KEY"
openai.api_base = "YOUR AZURE OPENAI ENDPOINT"
openai.api_type = 'azure'
# ファインチューニングするためにはこのバージョン移行のAPIを指定する必要があります。
openai.api_version = '2023-09-15-preview' 
training_file_name = 'training_set.jsonl'
validation_file_name = 'validation_set.jsonl'
# SDKを使いAzure OpenAIにトレーニング用とバリデーション用のファイルをアップロードする。

training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine-tune", user_provided_filename="training_set.jsonl"
)
training_file_id = training_response["id"]
validation_response = openai.File.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune", user_provided_filename="validation_set.jsonl"
)
validation_file_id = validation_response["id"]
print("Training file ID:", training_file_id)
print("Validation file ID:", validation_file_id)