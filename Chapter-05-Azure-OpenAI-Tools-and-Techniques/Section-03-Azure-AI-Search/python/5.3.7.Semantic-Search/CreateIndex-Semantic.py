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
    SemanticConfiguration,
    SemanticField,
    PrioritizedFields,
    SemanticSettings,
    HnswVectorSearchAlgorithmConfiguration
)

#Cognitive SearchのエンドポイントとAPIキーを指定
endpoint = "YOUR COGNITIVE SEARCH ENDPOINT"
key = "YOUR COGNITIVE SEARCH API KEY"

# Cognitive Search Clientの作成
client = SearchIndexClient(endpoint, AzureKeyCredential(key))

# インデックス名の指定
name = "index-semantic"

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
        searchable=True,
        retrievable=True,
        analyzer_name='ja.microsoft' # Microsoft日本語アナライザーを指定
    ),
    SearchField(
        name="title_vector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536, #ベクトル化した際の次元数
        vector_search_configuration='vectorConfig'
    ),
    SearchableField(
        name="description",
        type=SearchFieldDataType.String,
        searchable=True,
        retrievable=True,
        analyzer_name='ja.microsoft' # Microsoft日本語アナライザーを指定
    ),
    SearchField(
        name="description_vector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536, #ベクトル化した際の次元数
        vector_search_configuration='vectorConfig'
    )
]

# ベクトル検索用の設定を定義
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

#セマンティック検索用の設定を定義
semantic_config = SemanticConfiguration(
    name="my-semantic-config",
    prioritized_fields=PrioritizedFields(
        title_field=SemanticField(field_name="title"),
        prioritized_content_fields=[SemanticField(field_name="description")]
    )
)
semantic_settings = SemanticSettings(configurations=[semantic_config])
cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds = 60)
scoring_profiles = []
# インデックスの作成
index = SearchIndex(
    name=name,
    fields=fields,
    semantic_settings=semantic_settings,
    scoring_profiles=scoring_profiles,
    vector_search=vector_search,
    cors_options=cors_options
)
result = client.create_index(index)