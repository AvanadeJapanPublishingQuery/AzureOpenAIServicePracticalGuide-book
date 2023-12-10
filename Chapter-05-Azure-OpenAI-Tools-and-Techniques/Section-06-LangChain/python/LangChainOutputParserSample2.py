from typing import List
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage

# Azure OpenAI APIの設定
AZURE_OPENAI_ENDPOINT="YOUR AZURE OPENAI ENDPOINT"
AZURE_OPENAI_API_KEY="YOUR AZURE OPENAI API KEY"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"

# Jobというクラスで出力形式を定義
class Job(BaseModel):
 name: str = Field(description="仕事の名前")
 skill_list: List[str] = Field(description="その仕事が必要なスキルのリスト")

# pydantic_objectでJobクラスを指定
parser = PydanticOutputParser(pydantic_object = Job)
prompt = PromptTemplate(
 template="{query}\n\n{format_instructions}\n",
 input_variables=["query"],
 partial_variables={"format_instructions": parser.get_format_instructions()}
)
_input = prompt.format_prompt(query="フロントエンジニアに必要なスキルを教えて。")

llm = AzureChatOpenAI(
 openai_api_base=AZURE_OPENAI_ENDPOINT,
 openai_api_version="2023-07-01-preview",
 deployment_name=DEPLOYMENT_NAME,
 openai_api_key=AZURE_OPENAI_API_KEY,
 openai_api_type="azure"
)

output = llm([HumanMessage(content = _input.to_string())]).content
print(output)