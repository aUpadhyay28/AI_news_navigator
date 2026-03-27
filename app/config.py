import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")  # groq / openai / ollama

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME", "llama3-70b-8192")

settings = Settings()