from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    CorsOptions,
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswVectorSearchAlgorithmConfiguration,
)

# Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"

# Cognitive Search Clientの作成
client = SearchIndexClient(endpoint, AzureKeyCredential(key))

# インデックス名の指定
name = "artworks-vector"

# インデックスのフィールドを定義
fields = [
    SimpleField(
        name="Id", 
        type=SearchFieldDataType.String, 
        key=True
    ),
    SearchableField(
        name="title", 
        type=SearchFieldDataType.String, 
        searchable=True
    ), 
    SearchField(
        name="title_vector", 
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single), 
        searchable=True,
        vector_search_dimensions=1536, #ベクトル化した際の次元数
        vector_search_configuration='vectorConfig'
    ), 
    SearchableField(
        name="artist", 
        type=SearchFieldDataType.String, 
        searchable=True
    ), 
    SearchableField(
        name="description", 
        type=SearchFieldDataType.String, 
        searchable=True
    ), 
    SearchField(
        name="description_vector", 
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single), 
        searchable=True,
        vector_search_dimensions=1536, #ベクトル化した際の次元数
        vector_search_configuration='vectorConfig'
    ), 
    SearchableField(
        name="category", 
        type=SearchFieldDataType.String, 
        searchable=True
    ), 
    SimpleField(
        name="creation_date", 
        type=SearchFieldDataType.String
    )
]
cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
scoring_profiles = []

# ベクター検索用の設定を定義
vector_search = VectorSearch(
    algorithm_configurations=[
        HnswVectorSearchAlgorithmConfiguration(
            name="vectorConfig",
            kind="hnsw",
            parameters={
                "m": 4,
                "efConstruction": 400,
                "efSearch": 500,
                "metric": "cosine"
            }
        )
    ]
)

# インデックスの作成
index = SearchIndex(
    name=name,
    fields=fields,
    scoring_profiles=scoring_profiles,
    vector_search=vector_search,
    cors_options=cors_options)

result = client.create_index(index)