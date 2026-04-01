from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

VECTOR_STORE = {
    "documents": [],
    "embeddings": []
}

def add_documents_to_vectorstore(docs, embeddings):
    VECTOR_STORE["documents"].extend(docs)
    VECTOR_STORE["embeddings"].extend(embeddings)

def query_vectorstore(query_embedding, top_k=5):
    if not VECTOR_STORE["embeddings"]:
        return []

    similarities = cosine_similarity([query_embedding], VECTOR_STORE["embeddings"])[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = [VECTOR_STORE["documents"][i] for i in top_indices]
    return results

def clear_vectorstore():
    global VECTOR_STORE
    VECTOR_STORE["documents"] = []
    VECTOR_STORE["embeddings"] = []
    print("🧹 Vector store cleared!")