from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "gpt-4o-mini"   # You can change to "gpt-4o" if you want

settings = Settings()