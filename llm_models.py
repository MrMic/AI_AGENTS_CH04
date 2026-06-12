from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

import os

# load_env()
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

def get_llm():
    return ChatOpenAI(api_key=OPEN_API_KEY, model="gpt-5-nano")
