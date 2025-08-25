class FeedbackAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def give_feedback(self, student_answer, max_new_tokens=80):
        input_text = f"Improve this answer in clear, correct English: {student_answer}"
        result = self.model(input_text, max_new_tokens=max_new_tokens, do_sample=True)
        return result[0]['generated_text']
