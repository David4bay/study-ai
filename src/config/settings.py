import os
from dotenv import load_dotenv 

load_dotenv()

class Settings():
    GQ_API_KEY = os.getenv("GQ_API_KEY")
    MODEL_NAME = os.getenv("LLM_MODEL")
    TEMPERATURE = 1
    MAX_RETRIES = 3

settings = Settings()