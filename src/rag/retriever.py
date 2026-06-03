from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from src.ingestion.utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)


def get_retriever():

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        collection_name="financial_risk_documents",
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5
        }
    )

    logger.info(
        "Retriever initialized successfully."
    )

    return retriever
