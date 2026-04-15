import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_index():
    index = faiss.read_index("faiss_index/index.bin")
    with open("faiss_index/metadata.pkl", "rb") as f:
        docs = pickle.load(f)
    return index, docs

def search(query, k=2):
    index, docs = load_index()
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), k)
    return [docs[i] for i in indices[0]]

def generate_response(query, docs):
    context = "\n".join(docs)
    return f"Answer based on data:\n{context}"