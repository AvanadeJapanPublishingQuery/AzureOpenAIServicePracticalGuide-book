import openai
import os
openai.api_key = "YOUR AZURE OPENAI API KEY"
openai.api_base = "YOUR AZURE OPENAI ENDPOINT"
openai.api_type = 'azure'
openai.api_version = '2023-09-15-preview' 
training_file_id="file-xxxxxxxxxxxx"
validation_file_id="file-xxxxxxxxxxx"
response = openai.FineTuningJob.create(
 training_file=training_file_id,
 validation_file=validation_file_id,
 model="gpt-35-turbo-0613",
)
job_id = response["id"]

print("Job ID:", response["id"])
print("Status:", response["status"])
print(response)
