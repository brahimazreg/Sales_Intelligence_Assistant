from app.rag.documents import load_files



def main():
    path="rag_documents/"
    # "C:\Sales_Intelligence_Assistant\app\rag\documents.py"
    response= load_files(path)
    print(response)



if __name__ == "__main__":
    main()