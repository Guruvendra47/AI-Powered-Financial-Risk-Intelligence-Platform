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

    vector_store = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    batch_size = 50

    for i in range(0, len(chunks), batch_size):

        batch = chunks[i:i + batch_size]

        vector_store.add_documents(batch)

        print(
            f"Processed Batch "
            f"{i // batch_size + 1}"
        )

    print(
        f"Vector Store Created: {len(chunks)} chunks"
    )

    return vector_store


if __name__ == "__main__":

    create_vector_store()
