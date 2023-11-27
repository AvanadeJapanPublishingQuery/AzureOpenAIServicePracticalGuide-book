from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Azure OpenAI APIの設定
BASE_URL = "AZURE_OPENAI_ENDPOINT"
API_KEY = "AZURE_OPENAI_API_KEY"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"

llm = AzureChatOpenAI(
 openai_api_base=BASE_URL,
 openai_api_version="2023-07-01-preview",
 deployment_name=DEPLOYMENT_NAME,
 openai_api_key=API_KEY,
 openai_api_type="azure"
)
prompt = PromptTemplate(
 input_variables=["job"],
 template="{job}がよく使うMicrosoft製品を一つ教えて"
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain("AIエンジニア"))