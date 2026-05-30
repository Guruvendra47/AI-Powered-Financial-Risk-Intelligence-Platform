from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma

load_dotenv()


def ask_question(question):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
You are a financial compliance and risk analyst.

Use the provided context to answer
the question.

Context:
{context}

Question:
{question}

Provide:

1. Summary
2. Compliance Insight
3. Risk Assessment
4. Recommendation
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    question = (
        "What are the major compliance risks "
        "for financial institutions?"
    )

    answer = ask_question(question)

    print("\nQUESTION:\n")
    print(question)

    print("\nANSWER:\n")
    print(answer)
