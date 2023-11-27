from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# Azure OpenAI APIの設定
BASE_URL = "AZURE_OPENAI_ENDPOINT"
API_KEY = "AZURE_OPENAI_API_KEY"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
 template="今後おすすめの{subject}は? n{format_instructions}",
 input_variables=["subject"],
 partial_variables={"format_instructions": format_instructions}
)

llm = AzureChatOpenAI(
 openai_api_base=BASE_URL,
 openai_api_version="2023-07-01-preview",
 deployment_name=DEPLOYMENT_NAME,
 openai_api_key=API_KEY,
 openai_api_type="azure"
)
_input = prompt.format(subject = "プログラミング言語")
output = llm([HumanMessage(content = _input)]).content
print(output)