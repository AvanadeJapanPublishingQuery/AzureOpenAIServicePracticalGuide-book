from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai
from openai import util
import time

# インデックス名の指定
index_name = "artworks-vector"
# Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"

# OpenAIのAPIキーを設定 
openai.api_type = 'azure'
openai.api_key = "YOUR AZURE OPENAI API KEY"
openai.api_base = "YOUR AZURE OPENAI ENDPOINT"
model_name = "YOUR AZURE OPENAI MODELNAME"
openai.api_version = "2023-05-15"
# アップロードするドキュメントの指定
DOCUMENT = [{
    'Id': '1', 
    'title': '泣く女', 
    'title_vector': '', 
    'artist': 'パブロ・ピカソ', 
    'description': '「泣く女」は、ピカソのキュビスムの時期に描かれた作品の一つです。この作品は、彼の愛人であったドラ・マールの肖像と言われています。', 
    'description_vector': '', 
    'category': '絵画', 
    'creation_date': '1937年', 
}, 
{ 
    'Id': '2', 
    'title': 'ゲルニカ', 
    'title_vector': '', 
    'artist': 'パブロ・ピカソ', 
    'description': '「ゲルニカ」は、スペイン内戦中の無差別爆撃を描いた反戦作品で、ピカソの代表作の一つです。', 
    'description_vector': '', 
    'category': '絵画', 
    'creation_date': '1937年',
}, 
{ 
    'Id': '3', 
    'title': '老いたギタリスト', 
    'title_vector': '', 
    'artist': 'パブロ・ピカソ', 
    'description': '「老いたギタリスト」は、ピカソの青の時期に描かれた作品で、苦境に立つ老人を描いています。', 
    'description_vector': '', 
    'category': '絵画', 
    'creation_date': '1903-1904年',
}]
for doc in DOCUMENT: 
 # タイトルをベクトル化 
    response_title = openai.Embedding.create(input=doc['title'],engine=model_name)
    doc['title_vector'] = response_title['data'][0]['embedding']
    time.sleep(10)
    # 説明をベクトル化
    response_description = openai.Embedding.create(input=doc['description'],engine=model_name)
    doc['description_vector'] = response_description['data'][0]['embedding']
    time.sleep(10)

# インデックスの内容を格納
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
# ドキュメントのアップロード
result = search_client.upload_documents(documents=DOCUMENT) 
# アップロードの結果を表示
print("ドキュメントの登録に成功しました: {}".format(result[0].succeeded))