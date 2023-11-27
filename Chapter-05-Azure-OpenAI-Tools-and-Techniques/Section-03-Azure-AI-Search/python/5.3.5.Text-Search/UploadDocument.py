from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
# インデックス名の指定
index_name = "artworks"
# Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"
# アップロードするドキュメントの指定
DOCUMENT = [{
    'Id': '1', 
    'title': '泣く女', 
    'artist': 'パブロ・ピカソ', 
    'description': '「泣く女」は、ピカソのキュビスムの時期に描かれた作品の一つです。この作品は、彼の愛人であったドラ・マールの肖像と言われています。', 
    'category': '絵画', 
    'creation_date': '1937年', 
}, 
{ 
     'Id': '2', 
    'title': 'ゲルニカ', 
    'artist': 'パブロ・ピカソ', 
    'description': '「ゲルニカ」は、スペイン内戦中の無差別爆撃を描いた反戦作品で、ピカソの代表作の一つです。', 
    'category': '絵画', 
    'creation_date': '1937年',
}, 
{ 
    'Id': '3', 
    'title': '老いたギタリスト', 
    'artist': 'パブロ・ピカソ', 
    'description': '「老いたギタリスト」は、ピカソの青の時期に描かれた作品で、苦境に立つ老人を描いています。', 
    'category': '絵画', 
    'creation_date': '1903-1904年',
}]
# インデックスの内容を格納
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
# ドキュメントのアップロード
result = search_client.upload_documents(documents=DOCUMENT) 
# アップロードの結果を表示
print("ドキュメントの登録結果（Trueなら成功）: {}".format(result[0].succeeded))