class TeachingAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def explain_topic(self, text, max_new_tokens=256):
        input_text = f"Explain in simple English: {text}"
        result = self.model(input_text, max_new_tokens=max_new_tokens, do_sample=False)
        return result[0]['generated_text']
