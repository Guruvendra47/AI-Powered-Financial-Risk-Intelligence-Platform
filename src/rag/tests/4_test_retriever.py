from src.rag.retriever import get_retriever


def main():

    retriever = get_retriever()

    query = (
        "What are consumer protections "
        "for credit card disputes?"
    )

    results = retriever.invoke(
        query
    )

    print(
        f"\nRetrieved Chunks: {len(results)}"
    )

    for i, doc in enumerate(
        results,
        start=1
    ):

        print(
            f"\n========== Result {i} ==========\n"
        )

        print(
            doc.page_content[:500]
        )


if __name__ == "__main__":
    main()
