import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from src.rag.load_documents import load_documents
from src.rag.chunk_documents import chunk_documents
from src.ingestion.utils.logger import get_logger

# Initialize environment and logging
load_dotenv()
logger = get_logger(__name__)


def create_vector_store():
    # Validate API configuration
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")

    # Ingest and process documents
    logger.info("Loading documents...")
    documents = load_documents()

    logger.info("Chunking documents...")
    chunks = chunk_documents(documents)
    logger.info(f"Total chunks created: {len(chunks)}")

    # Cost optimization during development
    # In production, remove this line to embed all chunks 
    # code will replace chunks = chunks[:100] with chunks = chunks
    chunks = chunks[:100]
    logger.info(f"Using {len(chunks)} chunks for embedding generation")

    # Configure embedding model and database
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    vector_store = Chroma(
        collection_name="financial_risk_documents",
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    # Add documents to database in batches
    batch_size = 50
    total_chunks = len(chunks)
    logger.info(f"Adding {total_chunks} chunks to vector store...")

    for i in range(0, total_chunks, batch_size):
        batch = chunks[i : i + batch_size]
        vector_store.add_documents(batch)
        logger.info(f"Processed batch {i // batch_size + 1}")

    logger.info("Vector Store successfully created.")
    return vector_store


if __name__ == "__main__":
    create_vector_store()
