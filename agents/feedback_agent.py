class FeedbackAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def give_feedback(self, student_answer, max_new_tokens=80):
        if self.model is None:
            return "Sorry, the AI feedback model is not available. Please review your answer and check for grammar, clarity, and completeness."
        
        try:
            input_text = f"Provide constructive feedback to improve this student answer: {student_answer}"
            result = self.model(input_text, max_new_tokens=max_new_tokens, do_sample=True)
            return result[0]['generated_text']
        except Exception as e:
            return f"Error generating feedback: {str(e)}"
