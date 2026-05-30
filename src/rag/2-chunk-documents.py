from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag.document_loader import load_documents


def chunk_documents():

    documents = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks


if __name__ == "__main__":

    chunks = chunk_documents()

    print(
        f"Chunks Created: {len(chunks)}"
    )
