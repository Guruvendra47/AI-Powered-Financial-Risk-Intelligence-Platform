from src.rag.load_documents import (
    load_documents
)

from src.rag.chunk_documents import (
    chunk_documents
)


def main():

    documents = load_documents()

    chunks = chunk_documents(
        documents
    )

    print(
        f"\nChunks Created: "
        f"{len(chunks)}"
    )

    if chunks:

        print("\nFirst Chunk:\n")

        print(
            chunks[0].page_content[:500]
        )


if __name__ == "__main__":
    main()