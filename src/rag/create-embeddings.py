from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.rag.load_documents import load_documents  
from src.rag.chunk_documents import chunk_documents
from src.ingestion.utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

def create_vector_store():
    # 1. Load the documents
    documents = load_documents()
    
    # 2. Pass the documents into chunk_documents
    chunks = chunk_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # 3. Initialize the DB
    vector_store = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    # 4. Batching Logic
    batch_size = 50
    total_chunks = len(chunks)
    
    logger.info(f"Adding {total_chunks} chunks to vector store...")

    for i in range(0, total_chunks, batch_size):
        batch = chunks[i:i + batch_size]
        vector_store.add_documents(batch)
        logger.info(f"Processed batch {i // batch_size + 1}")

    logger.info("Vector Store successfully created.")
    return vector_store

if __name__ == "__main__":
    create_vector_store()
