from langchain.chat_models import AzureChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools import AIPluginTool
import time

# OpenAI APIの設定
BASE_URL = "https://demo-enterprise.openai.azure.com/"
API_KEY = "2a3cb13da860478ca656354a1d58048d"
DEPLOYMENT_NAME = "gpt-35-turbo-16k"
model = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-07-01-preview",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
)

# HTTPリクエストを行うためのツールをロード
tools = load_tools(["requests"])

# プラグインのロード
plugin_url = "http://localhost:8080/.well-known/ai-plugin.json"
tools.append(AIPluginTool.from_plugin_url(plugin_url))

#プラグインがロードされるまでの時間を設ける
time.sleep(5)

# エージェントのセットアップ
agent_chain = initialize_agent(
    tools=tools,
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    vebose=True,
)

# エージェント実行
result = agent_chain.run("現在のeventを表示して")
print(result)