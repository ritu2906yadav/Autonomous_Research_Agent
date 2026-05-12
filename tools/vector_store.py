from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    collection_name ="research_memory",
    embedding_function = embeddings,
    persist_directory ="./chroma.db"

)