from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_documents():

    document_folders = [
        "data/ai_documents/regulations",
        "data/ai_documents/compliance",
        "data/ai_documents/risk_reports"
    ]

    documents = []

    for folder in document_folders:

        pdf_files = Path(folder).glob("*.pdf")

        for pdf_file in pdf_files:

            logger.info(
                f"Loading document: {pdf_file}"
            )

            loader = PyPDFLoader(
                str(pdf_file)
            )

            documents.extend(
                loader.load()
            )

    logger.info(
        f"Total documents loaded: {len(documents)}"
    )

    return documents
