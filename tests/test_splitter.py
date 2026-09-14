from app.rag.documents import load_files
from app.rag.splitters import split_into_chunks
from app import  config

def main():
    documents = load_files(config.PATH_DOCUMENTS_FILES)
    response= split_into_chunks(documents)

    print(f"Number of chunks: {len(response)}")
    print("=" * 50)

    for i, chunk in enumerate(response[:5]):
        print(f"\n--- Chunk {i} ---")
        print(f"Length: {len(chunk.page_content)}")        
        print(chunk.page_content[:1000])  

if __name__ == "__main__":
    main()