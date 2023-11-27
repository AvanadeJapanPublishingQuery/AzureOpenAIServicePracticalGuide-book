from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

# Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"
# Cognitive Search Clientの作成
client = SearchIndexClient(endpoint, AzureKeyCredential(key))
# インデックス名の指定
name = "artworks"
# インデックスのフィールドを定義
fields = [
    SimpleField(name="Id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="title", type=SearchFieldDataType.String,searchable=True), 
    SearchableField(name="artist", type=SearchFieldDataType.String,searchable=True), 
    SearchableField(name="description", type=SearchFieldDataType.String,searchable=True), 
    SearchableField(name="category", type=SearchFieldDataType.String,searchable=True), 
    SimpleField(name="creation_date", type=SearchFieldDataType.String)
]
cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
scoring_profiles = []
# インデックスの作成
index = SearchIndex(
     name=name,
    fields=fields,
    scoring_profiles=scoring_profiles,
    cors_options=cors_options)
result = client.create_index(index)