from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from app import config

def split_into_chunks(documents):
    # 1. Définir les en-têtes sur lesquels couper (ici, le niveau H2 '##')
    headers_to_split_on = [
        ("##", "Header 2"),
    ]
    
    # 2. Premier découpage basé strictement sur les structures '##'
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on, 
        strip_headers=False # Garde le '##' dans le texte du chunk
    )
    
    # 3. Deuxième découpage pour respecter la taille max si un bloc '##' est trop grand
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    
    final_chunks = []
    
    # Parcourir vos documents initiaux
    for doc in documents:
        # split_text prend une chaîne de caractères (str)
        header_splits = markdown_splitter.split_text(doc.page_content)
        
        # Sous-découper chaque bloc pour respecter config.CHUNK_SIZE
        splits = text_splitter.split_documents(header_splits)
        final_chunks.extend(splits)
        
    return final_chunks