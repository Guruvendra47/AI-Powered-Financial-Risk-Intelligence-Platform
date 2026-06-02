from src.rag.load_documents import (
    load_documents
)


def main():

    documents = load_documents()

    print(
        f"\nLoaded Documents: {len(documents)}"
    )

    if documents:

        print("\nFirst Document Preview:\n")

        print(
            documents[0].page_content[:500]
        )


if __name__ == "__main__":
    main()
