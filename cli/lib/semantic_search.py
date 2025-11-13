from sentence_transformers import SentenceTransformer


class SemanticSearch:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> SentenceTransformer:
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str):
        if len(text.strip()) == 0:
            raise ValueError("text must container a alpha chars")
        embedding = self.model.encode([text])[0]
        return embedding


def verify_model() -> None:
    search_instance = SemanticSearch()
    print(f"Model loaded: {search_instance.model}")
    print(f"Max sequence length: {search_instance.model.max_seq_length}")


def embed_text(text):
    search_instance = SemanticSearch()
    embedding = search_instance.generate_embedding(text)
    print(f"Text: {text}")
    print(f"First 3 dimensions: {embedding[:3]}")
    print(f"Dimensions: {embedding.shape[0]}")
    return embedding
