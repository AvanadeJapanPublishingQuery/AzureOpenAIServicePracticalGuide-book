import openai
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.azuresearch import AzureSearch
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import time

# Azure OpenAIのエンドポイントとAPIキー
AZURE_OPENAI_ENDPOINT="YOUR AZURE OPENAI ENDPOINT"
AZURE_OPENAI_API_KEY="YOUR AZURE OPENAI API KEY"

#Embeddingモデルのデプロイ名
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME="YOUR AZURE OPENAI EMBEDDINGS DEPLOYMENT NAME"

# Azure SearchのエンドポイントとAPIキー
AZURE_SEARCH_ENDPOINT="YOUR AZURE SEARCH ENDPOINT"
AZURE_SEARCH_SERVICE_NAME="YOUR AZURE SEARCH SERVICE NAME"
AZURE_SEARCH_API_KEY_ADMIN="YOUR AZURE SEARCH API KEY ADMIN"

embeddings = OpenAIEmbeddings(
    openai_api_type="azure",
    model='text-embedding-ada-002',
    openai_api_base=AZURE_OPENAI_ENDPOINT,
    openai_api_key=AZURE_OPENAI_API_KEY,
    deployment=AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME
)


#Cognitive Searchのインデックス名、ベクトルストアの設定
index_name = "langchain-search-demo"

vector_store = AzureSearch(
 azure_search_endpoint=AZURE_SEARCH_ENDPOINT,
 azure_search_key=AZURE_SEARCH_API_KEY_ADMIN,
 index_name=index_name,
 embedding_function=embeddings.embed_query,
)
loader = TextLoader("long_text.txt", encoding="utf-8")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
vector_store.add_documents(documents=docs)

#インデックスに登録されるまでの時間を設ける
time.sleep(5)

# ベクター検索の実施
docs = vector_store.similarity_search(
    query="GPT-4を使ってどんなことができるの？ ",
    k=3,
    search_type="similarity",
)
print(docs[0].page_content)