from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import Vector
import openai
from openai import util
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

# 検索ワードの指定
search_word = "楽器を含む絵画"

# 検索ワードのベクトル化
response_search_word_vector = openai.Embedding.create(input = search_word,
engine = model_name)

# 検索クライアントの作成
client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

# 検索クエリの実行
results = client.search(
    search_text='',
    include_total_count=True,
    vectors = [Vector(
        value = response_search_word_vector['data'][0]['embedding'],
        k=3,
        fields='description_vector'
    )]
)

# 検索結果件数の表示
print ('検索結果件数:', results.get_count())
# 検索結果の表示
for result in results:
 print("Id: " + result["Id"])
 print("title: " + result["title"])
 print("artist: " + result["artist"])
 print("description: " + result["description"])
 print("category: " + result["category"])
 print("creation_date: " + result["creation_date"])