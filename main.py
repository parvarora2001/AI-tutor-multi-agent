from models.model_loader import ModelLoader
from agents.teaching_agent import TeachingAgent
from agents.feedback_agent import FeedbackAgent
from agents.grading_agent import GradingAgent
from utils.text_processing import clean_text

# Load shared models
loader = ModelLoader()
text_pipeline = loader.get_text_pipeline()
grading_pipeline = loader.get_grading_pipeline()

# Initialize agents (shared models)
teacher = TeachingAgent(text_pipeline)
feedback = FeedbackAgent(text_pipeline)
grader = GradingAgent(grading_pipeline)

# Sample lesson
lesson_text = "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water."

print("\n📘 Teaching Agent Output:")
explanation = teacher.explain_topic(lesson_text)
print(explanation)

student_answer = "Photosynthesis is when plants make food using sunlight and give out oxygen."
expected_answer = "Plants use sunlight, water, and CO2 to make food and release oxygen."

print("\n📝 Grading Agent Output:")
grade = grader.grade_answer(student_answer, expected_answer)
print(grade)

print("\n💡 Feedback Agent Output:")
fb = feedback.give_feedback(student_answer)
print(fb)
