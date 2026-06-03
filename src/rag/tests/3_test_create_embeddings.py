from src.rag.create_embeddings import (
    create_vector_store
)


def main():

    vector_store = create_vector_store()

    print(
        "\nVector Store Created Successfully"
    )

    print(
        f"Total Vectors: "
        f"{vector_store._collection.count()}"
    )


if __name__ == "__main__":
    main()