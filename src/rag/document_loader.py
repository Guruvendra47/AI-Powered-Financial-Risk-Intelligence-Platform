from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

def load_documents():

    document_paths = []

    folders = [
        "data/documents/regulations",
        "data/documents/compliance",
        "data/documents/risk_reports"
    ]

    for folder in folders:

        pdf_files = Path(folder).glob("*.pdf")

        for file in pdf_files:
            document_paths.append(str(file))

    documents = []

    for pdf_file in document_paths:

        loader = PyPDFLoader(pdf_file)

        documents.extend(
            loader.load()
        )

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(
        f"Documents Loaded: {len(docs)}"
    )
