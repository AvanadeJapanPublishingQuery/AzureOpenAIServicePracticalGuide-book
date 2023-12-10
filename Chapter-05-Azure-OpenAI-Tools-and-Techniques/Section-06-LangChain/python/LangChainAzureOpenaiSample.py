from langchain.chat_models import AzureChatOpenAI
from langchain.schema import (
 SystemMessage,
 HumanMessage,
)
# Azure OpenAI APIの設定
AZURE_OPENAI_ENDPOINT="YOUR AZURE OPENAI ENDPOINT"
AZURE_OPENAI_API_KEY="YOUR AZURE OPENAI API KEY"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"
chat = AzureChatOpenAI(
 openai_api_base=AZURE_OPENAI_ENDPOINT,
 openai_api_version="2023-07-01-preview",
 deployment_name=DEPLOYMENT_NAME,
 openai_api_key=AZURE_OPENAI_API_KEY,
 openai_api_type="azure"
)

output = chat([
 SystemMessage(content="日本語で回答して。"),
 HumanMessage(content="ChatGPTについて30文字で教えて。"),
])

print(output.content)