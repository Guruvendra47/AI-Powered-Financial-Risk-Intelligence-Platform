from src.rag.rag_chain import build_rag_chain

def main():
    # Build the chain
    rag_chain = build_rag_chain()

    question = (
        "What are consumer protections "
        "for credit card disputes?"
    )

    # Use 'input' instead of 'query' to match the default 
    # expected key of create_retrieval_chain
    response = rag_chain.invoke(
        {"input": question}
    )

    print("\nQUESTION:\n")
    print(question)

    print("\nANSWER:\n")
    # Note: Modern chains typically return the answer under the key 'answer',
    # not 'result'. If you get a KeyError here, print 'response' to 
    # inspect the dictionary keys.
    print(response.get("answer", "Answer key not found. Inspecting response..."))
    
    # If "answer" doesn't work, uncomment the line below to debug:
    # print(response.keys())

if __name__ == "__main__":
    main()