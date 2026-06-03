from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

from src.rag.retriever import get_retriever

load_dotenv()


def build_rag_chain():

    retriever = get_retriever()

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a financial risk and compliance assistant.

Answer the question using ONLY the provided context.

If the answer cannot be found in the context, say:

'I could not find that information in the document repository.'

Context:
{context}

Question:
{question}
"""
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": prompt
        }
    )

    return qa_chain
