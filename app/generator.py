import re

from app import config
from app.llm import get_llm


def generate_sql(question, schema):

    llm = get_llm()

    prompt = config.PROMPT.format(
        schema=schema,
        question=question
    )

    print("Appel de Qwen via Ollama...")

    response = llm.invoke(prompt)

    print("Réponse reçue.")

    # Récupérer le contenu textuel
    content = response.content

    # Si le modèle retourne une liste de blocs
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))
            elif isinstance(block, str):
                text_parts.append(block)

        content = "\n".join(text_parts)

    # Supprimer les balises Markdown ```sql ... ```
    content = re.sub(r"```sql\s*", "", content, flags=re.IGNORECASE)
    content = re.sub(r"```\s*$", "", content)

    return content.strip()