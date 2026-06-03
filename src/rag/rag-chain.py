import os
from dotenv import load_dotenv

# Use these exact paths for modern LangChain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# ... rest of your code
# Import your custom retriever
from src.rag.retriever import get_retriever

# Load environment variables (ensure OPENAI_API_KEY is in your .env)
load_dotenv()

def build_rag_chain():
    """
    Builds a modern RAG chain using LCEL-compatible components.
    """
    # 1. Initialize the retriever
    retriever = get_retriever()

    # 2. Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # or "gpt-4o"
        temperature=0
    )

    # 3. Define the Prompt Template
    # Using a ChatPromptTemplate with clear system and human roles
    system_prompt = (
        "You are a financial risk and compliance assistant. "
        "Answer the question using ONLY the provided context."
        "\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # 4. Create the document-stuffing chain
    # This takes the retrieved documents and "stuffs" them into the context
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    # 5. Create the retrieval chain
    # This orchestrates the retriever and the stuffing chain
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return rag_chain

# Example usage for testing:
if __name__ == "__main__":
    chain = build_rag_chain()
    # Note: Use 'input' as the key for the query
    result = chain.invoke({"input": "What are the latest FDIC compliance requirements?"})
    print(result["answer"])
