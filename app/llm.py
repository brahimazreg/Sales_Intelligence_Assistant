import os

from langchain_ollama import ChatOllama


def get_llm():
    ollama_base_url = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    return ChatOllama(
        model="qwen3:8b",
        temperature=0,
        base_url=ollama_base_url,
    )