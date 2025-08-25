from transformers import pipeline

class ModelLoader:
    """
    Loads open-source models once and shares them across agents.
    """

    def __init__(self):
        print("Loading shared open-source models (this may take a minute)...")

        # Shared Teaching/Feedback model
        self.text_model_pipeline = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            device=0  # MPS device
        )

        # Shared Grading model
        self.grading_pipeline = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=0
        )

    def get_text_pipeline(self):
        return self.text_model_pipeline

    def get_grading_pipeline(self):
        return self.grading_pipeline
