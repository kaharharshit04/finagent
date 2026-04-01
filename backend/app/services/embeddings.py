from sentence_transformers import SentenceTransformer
import os

# Load a small, fast model locally
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    # This returns a list of floats
    embedding = model.encode(text).tolist()
    return embedding