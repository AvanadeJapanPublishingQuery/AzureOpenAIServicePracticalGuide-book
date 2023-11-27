from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
# インデックス名の指定
index_name = "artworks"
# Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"
# 検索クライアントの作成
client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
# 検索クエリの実行
results = client.search(search_text="泣く女", include_total_count=True)
# 検索結果件数の表示
print ('Total Documents Matching Query:', results.get_count())
# 検索結果の表示
for result in results:
 print("Id: " + result["Id"])
 print("title: " + result["title"])
 print("artist: " + result["artist"])
 print("description: " + result["description"])
 print("category: " + result["category"])
 print("creation_date: " + result["creation_date"])