from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template("{keyword}を解説する書籍のタイトル案は?")
prompt = template.format(keyword="ChatGPT")
BASE_URL = "AZURE_OPENAI_ENDPOINT"
API_KEY = "AZURE_OPENAI_API_KEY"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"

output = chat = AzureChatOpenAI(
 openai_api_base=BASE_URL,
 openai_api_version="2023-07-01-preview",
 deployment_name=DEPLOYMENT_NAME,
 openai_api_key=API_KEY,
 openai_api_type="azure"
)

output = chat.predict(prompt)
print(output)