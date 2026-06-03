from fastapi import FastAPI
from pydantic import BaseModel

from src.rag.rag_chain import build_rag_chain

app = FastAPI(
    title="Financial Risk Intelligence API",
    version="1.0.0"
)

rag_chain = build_rag_chain()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():

    return {
        "status": "healthy",
        "application":
        "Financial Risk Intelligence Platform"
    }


@app.post("/api/v1/ask")
def ask_question(
    request: QuestionRequest
):

    response = rag_chain.invoke(
        {
            "input":
            request.question
        }
    )

    return {
        "question":
        request.question,

        "answer":
        response["answer"]
    }
