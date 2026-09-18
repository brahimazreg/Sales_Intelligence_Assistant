import os
import socket

from langchain_ollama import ChatOllama


def get_llm():
    ollama_base_url = os.getenv(
        "OLLAMA_BASE_URL",
        "http://127.0.0.1:11434"
    )

    print("=" * 60)
    print("OLLAMA DEBUG")
    print("OLLAMA_BASE_URL =", os.getenv("OLLAMA_BASE_URL"))
    print("URL utilisée     =", ollama_base_url)
    print("localhost        =", socket.gethostbyname("localhost"))
    print("127.0.0.1        =", socket.gethostbyname("127.0.0.1"))
    print("=" * 60)

    return ChatOllama(
        model="qwen3:8b",
        temperature=0,
        base_url=ollama_base_url,
    )