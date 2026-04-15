# create_index.py

import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load docs
with open("data/docs.txt", "r") as f:
    docs = f.readlines()

embeddings = model.encode(docs)

# Create index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save
faiss.write_index(index, "faiss_index/index.bin")

with open("faiss_index/metadata.pkl", "wb") as f:
    pickle.dump(docs, f)

print("✅ FAISS index created")