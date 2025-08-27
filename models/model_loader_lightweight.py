from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import torch

class ModelLoader:
    """
    Loads and shares lightweight open-source models across agents.
    """

    def __init__(self):
        print("Loading lightweight shared models (this may take a minute)...")
        
        try:
            # Use the smallest possible model to prevent memory issues
            model_name = "google/flan-t5-small"  # Smallest flan-t5 model
            
            # Load tokenizer and model separately for better memory management
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForSeq2SeqLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,  # Use float32 for better compatibility
                low_cpu_mem_usage=True
            )
            
            # Teaching + Feedback model with minimal configuration
            self.text_model_pipeline = pipeline(
                "text2text-generation",
                model=model,
                tokenizer=tokenizer,
                device="cpu",  # Force CPU to avoid MPS/GPU issues
                do_sample=True,
                temperature=0.7,
                generation_kwargs={
                    "max_new_tokens": 64,  # Very short responses
                    "do_sample": True,
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "repetition_penalty": 1.1
                }
            )

            # Use the smallest sentence transformer model
            self.similarity_model = SentenceTransformer(
                'sentence-transformers/all-MiniLM-L6-v2',
                device='cpu'
            )
            
            print("✅ Lightweight models loaded successfully!")
            
        except Exception as e:
            print(f"❌ Error loading models: {e}")
            print("Falling back to dummy implementations...")
            
            # Fallback: Dummy implementations
            self.text_model_pipeline = None
            self.similarity_model = None

    def get_text_pipeline(self):
        return self.text_model_pipeline

    def get_similarity_model(self):
        return self.similarity_model
