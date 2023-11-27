import openai
from azure.core.credentials import AzureKeyCredential  
from azure.search.documents import SearchClient  
from azure.search.documents.models import Vector 

# Azure OpenAIのAPIキー／エンドポイント等を設定する
openai.api_key = 'AZURE_OPENAI_API_KEY'
openai.api_base = 'AZURE_OPENAI_ENDPOINT'
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
gpt_model_name = 'AZURE_OPENAI_DEPLOYED_GPT_MODEL_NAME'
embedding_model_name = 'AZURE_OPENAI_DEPLOYED_EMBEDDING_MODEL_NAME'

# Cognitive SearchのAPIキー／エンドポイント等を設定する
search_service_endpoint = 'AZURE_COGNITIVE_SEARCH_ENDPOINT'
search_service_api_key = 'AZURE_COGNITIVE_SEARCH_ADMIN_KEY'
index_name = 'AZURE_COGNITIVE_SEARCH_INDEX_NAME'
credential = AzureKeyCredential(search_service_api_key)

# ユーザーの質問文を設定する
question = 'ミレーについて教えて'

# 質問文をAzure OpenAIに送信して、ベクトル化する
response = openai.Embedding.create(input=question, engine=embedding_model_name)
embeddings = response['data'][0]['embedding']

# Cognitive Searchのクライアントオブジェクトを作成する
search_client = SearchClient(search_service_endpoint, index_name, credential)  

# ハイブリッド検索を行う（テキスト検索とベクトル検索のハイブリッド検索）
results = search_client.search(  
    search_text=question,  
    vectors=[Vector(
        value=embeddings, 
        k=3, 
        fields='description_vector'
    )],
    select=["description"],
    top=1
)

# Cognitive Searchの検索結果を変数に格納します
search_result = ''
for result in results:  
    search_result += result['description']

system_prompt = f'''
あなたは優秀なサポートAIです。ユーザーから提供される情報をベースにあなたが学習している情報を付加して回答してください。
'''

user_prompt = f'''
{ question }\n参考情報：
{ search_result }
'''

# ChatCompletion経由でAzure OpenAIにリクエストする
# APIのパラメータとして、システムプロンプトとユーザーのプロンプトを設定する
response = openai.ChatCompletion.create(
  engine=gpt_model_name, 
  messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)
# 結果を画面上で出力する
text = response['choices'][0]['message']['content'].replace('\n', '').replace(' .', '.').strip()
print(text)
