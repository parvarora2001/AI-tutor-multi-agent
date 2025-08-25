from transformers import pipeline
from sentence_transformers import SentenceTransformer

class ModelLoader:
    """
    Loads and shares all open-source models across agents.
    """

    def __init__(self):
        print("Loading shared open-source models (this may take a minute)...")

        # Teaching + Feedback model
        self.text_model_pipeline = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            device=-1  # MPS if on Mac, GPU otherwise
        )

        # Semantic similarity model for grading
        self.similarity_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def get_text_pipeline(self):
        return self.text_model_pipeline

    def get_similarity_model(self):
        return self.similarity_model
