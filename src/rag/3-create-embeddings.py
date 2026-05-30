from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from src.rag.chunk_documents import chunk_documents

load_dotenv()


def create_vector_store():

    chunks = chunk_documents()

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_store/chroma_db"
    )

    print(
        f"Vector Store Created: {len(chunks)} chunks"
    )

    return vector_store


if __name__ == "__main__":

    create_vector_store()
