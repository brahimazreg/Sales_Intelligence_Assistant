from langchain_community.document_loaders import DirectoryLoader, TextLoader
from app import config

def load_files(path: str = config.PATH_DOCUMENTS_FILES):
    loader = DirectoryLoader(
        path=path,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        
    )

    documents = loader.load()

    return documents