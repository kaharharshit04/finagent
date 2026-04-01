from app.services.embeddings import get_embedding
from app.services.vector_store import query_vectorstore

def retrieve_context(question):
    embedding = get_embedding(question)
    results = query_vectorstore(embedding, top_k=5)
    return results