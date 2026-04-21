import numpy as np
import faiss
import json
import os
from sentence_transformers import SentenceTransformer
import pickle
import logging

logger = logging.getLogger(__name__)

# Config
MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'  # Good for Vietnamese
DIM = 384  # Model embedding dim
TOP_K = 3
SIMILARITY_THRESHOLD = 0.75
INDEX_PATH = 'chatbot_index.faiss'
METADATA_PATH = 'chatbot_metadata.pkl'

model = None
index = None
metadata = []  # List of {"question": str, "answer": str, "score": float}

def load_model():
    global model
    if model is None:
        logger.info("Loading sentence-transformers model...")
        model = SentenceTransformer(MODEL_NAME)
    return model

def build_index(training_data):
    """Build FAISS index from Q&A pairs"""
    global index, metadata
    if not training_data:
        logger.warning("No training data")
        return
    
    model = load_model()
    questions = [pair["question"] for pair in training_data]
    
    # Embed questions
    embeddings = model.encode(questions, show_progress_bar=True, convert_to_numpy=True)
    
    # Create FAISS index
    index = faiss.IndexFlatIP(DIM)  # Inner product = cosine sim for normalized
    faiss.normalize_L2(embeddings)  # Normalize for cosine
    index.add(embeddings.astype('float32'))
    
    metadata = [{"question": q, "answer": pair["answer"]} for q, pair in zip(questions, training_data)]
    
    # Save
    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, 'wb') as f:
        pickle.dump(metadata, f)
    
    logger.info(f"Index built: {len(training_data)} pairs, dim={DIM}")

def load_index():
    """Load existing index"""
    global index, metadata
    if os.path.exists(INDEX_PATH) and os.path.exists(METADATA_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(METADATA_PATH, 'rb') as f:
            metadata = pickle.load(f)
        logger.info(f"Loaded index: {len(metadata)} pairs")
        return True
    return False

def search_similar(question, k=TOP_K):
    """Find top-k similar answers"""
    if index is None or not metadata:
        return []
    
    model = load_model()
    query_emb = model.encode([question])
    faiss.normalize_L2(query_emb)
    
    scores, indices = index.search(query_emb.astype('float32'), k)
    
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < len(metadata) and score >= SIMILARITY_THRESHOLD:
            results.append({
                "answer": metadata[idx]["answer"],
                "question": metadata[idx]["question"],
                "similarity": float(score)
            })
    
    return results

def add_training_pair(question, answer):
    """Add new pair and rebuild (call periodically)"""
    global metadata
    metadata.append({"question": question.lower().strip(), "answer": answer})
    
    # Rebuild every 50
    if len(metadata) % 50 == 0:
        training_data = [{"question": m["question"], "answer": m["answer"]} for m in metadata]
        build_index(training_data)

def get_stats():
    return {
        "index_loaded": index is not None,
        "num_pairs": len(metadata) if metadata else 0,
        "dim": DIM if index else 0
    }

