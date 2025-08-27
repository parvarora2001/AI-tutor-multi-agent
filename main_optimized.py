import os
import gc
import torch

# Memory optimization settings
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
os.environ["HF_HOME"] = "/tmp/hf_cache"

# Force garbage collection before loading models
gc.collect()
torch.cuda.empty_cache() if torch.cuda.is_available() else None

from models.model_loader import ModelLoader
from agents.teaching_agent import TeachingAgent
from agents.feedback_agent import FeedbackAgent
from agents.grading_agent import GradingAgent
from utils.text_processing import clean_text
import json

def main():
    print("🚀 Starting Tutor Agent with optimized memory management...")
    
    try:
        # Load shared models with error handling
        print("📦 Loading AI models...")
        loader = ModelLoader()
        text_pipeline = loader.get_text_pipeline()
        similarity_model = loader.get_similarity_model()
        
        if text_pipeline is None or similarity_model is None:
            print("❌ Failed to load models. Please check your internet connection and try again.")
            return
        
        # Initialize agents
        teacher = TeachingAgent(text_pipeline)
        feedback = FeedbackAgent(text_pipeline)
        grader = GradingAgent(similarity_model)
        
        print("✅ Models loaded successfully!")
        
        # Sample topics
        topics = [
            {
                "topic": "Photosynthesis",
                "expected_answer": "Plants use sunlight, water, and CO2 to make food and release oxygen."
            },
            {
                "topic": "Gravity",
                "expected_answer": "Gravity is the force by which objects attract each other towards the Earth."
            }
        ]
        
        results = []
        
        # CLI workflow
        for i, t in enumerate(topics, 1):
            topic_text = t["topic"]
            expected_answer = t["expected_answer"]
            
            print(f"\n📘 Teaching Agent Output for {topic_text}:")
            explanation = teacher.explain_topic(topic_text)
            print(explanation)
            
            student_answer = input("\n📝 Enter your answer: ")
            student_answer = clean_text(student_answer)
            
            grade = grader.grade_answer(student_answer, expected_answer)
            print("\n📝 Grading Agent Output:")
            print(grade)
            
            fb = feedback.give_feedback(student_answer)
            print("\n💡 Feedback Agent Output:")
            print(fb)
            
            results.append({
                "topic": topic_text,
                "student_answer": student_answer,
                "grade": grade,
                "feedback": fb
            })
            
            # Clear memory after each topic
            gc.collect()
        
        # Save session results
        with open("session_results.json", "w") as f:
            json.dump(results, f, indent=2)
        
        print("\n✅ Session complete! Results saved to session_results.json")
        
    except KeyboardInterrupt:
        print("\n\n👋 Session interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("💡 Try running with Docker for better stability.")

if __name__ == "__main__":
    main()
