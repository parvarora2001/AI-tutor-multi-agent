from sentence_transformers import util

class GradingAgent:
    def __init__(self, similarity_model):
        self.model = similarity_model

    def grade_answer(self, student_answer, expected_answer, threshold=0.7):
        if self.model is None:
            return {"grade": "Unable to grade", "confidence": 0.0, "message": "Grading model not available"}
        
        try:
            # Compute semantic similarity
            embeddings_student = self.model.encode(student_answer, convert_to_tensor=True)
            embeddings_expected = self.model.encode(expected_answer, convert_to_tensor=True)
            similarity = util.cos_sim(embeddings_student, embeddings_expected).item()

            grade = "Correct" if similarity >= threshold else "Incorrect"
            return {"grade": grade, "confidence": round(similarity, 2)}
        except Exception as e:
            return {"grade": "Error", "confidence": 0.0, "message": f"Grading error: {str(e)}"}
