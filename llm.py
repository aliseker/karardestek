import os
from langchain_openai import ChatOpenAI
import config

def get_llm(temperature=0.0):
    """
    Returns an instance of ChatOpenAI configured with project settings.
    """
    if not config.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in the environment or .env file.")
        
    return ChatOpenAI(
        model=config.LLM_MODEL_NAME,
        temperature=temperature,
        api_key=config.OPENAI_API_KEY
    )
