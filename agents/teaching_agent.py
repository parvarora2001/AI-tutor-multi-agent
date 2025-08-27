class TeachingAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def explain_topic(self, topic, max_new_tokens=256):
        if self.model is None:
            return f"Sorry, the AI model is not available. Here's a basic explanation of {topic}: {topic} is an important concept that you should study further with your teacher or textbook."
        
        try:
            input_text = f"Explain {topic} in simple terms for a student. Include what it is, why it matters, and an example."
            result = self.model(input_text, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7)
            return result[0]['generated_text'].strip()
        except Exception as e:
            return f"Error generating explanation for {topic}: {str(e)}"
