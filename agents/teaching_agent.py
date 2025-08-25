class TeachingAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def explain_topic(self, topic, max_new_tokens=256):
        input_text = f"""
Explain the following topic in 3-4 sentences in clear, simple English suitable for a student learning for the first time.
Include what it is, why it is important, and an example if possible.

Topic: {topic}
"""
        result = self.model(input_text, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7)
        return result[0]['generated_text'].strip()
