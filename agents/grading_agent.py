class GradingAgent:
    def __init__(self, model_pipeline):
        self.model = model_pipeline

    def grade_answer(self, student_answer, expected_answer):
        # Combine question + reference into input for classification
        prompt = f"Student answer: {student_answer} | Reference: {expected_answer}"
        result = self.model(prompt)[0]
        label = result['label']
        score = result['score']

        if label == "POSITIVE":
            grade = "Correct"
        else:
            grade = "Incorrect"

        return {"grade": grade, "confidence": round(score, 2)}
