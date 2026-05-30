from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()


def query_documents(question):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    results = vector_store.similarity_search(
        question,
        k=3
    )

    return results


if __name__ == "__main__":

    query = (
        "What are the major compliance risks "
        "for financial institutions?"
    )

    documents = query_documents(query)

    print("\nQUESTION:")
    print(query)

    print("\nRESULTS:\n")

    for i, doc in enumerate(documents, start=1):

        print(f"\n--- Result {i} ---\n")

        print(
            doc.page_content[:1000]
        )
