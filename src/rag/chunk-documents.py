from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.logger import get_logger

logger = get_logger(__name__)

def chunk_documents(documents):
    """
    Splits a list of loaded documents into manageable semantic chunks.
    """
    logger.info(f"Starting chunking process for {len(documents)} documents")

    # Clean configuration utilizing updated package defaults
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)
    
    logger.info(f"Generated {len(chunks)} chunks successfully")
    return chunks
