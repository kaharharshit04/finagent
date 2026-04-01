from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agent import run_agent

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
async def query_agent(req: QueryRequest):

    result = run_agent(req.question)

    return {
        "answer": result["answer"],
        "plan": result["plan"],
        "retrieved": result["retrieved"],
        "tool": result["tool"]
    }

@router.post("/clear-data")
async def clear_data():
    from app.services.vector_store import clear_vectorstore
    clear_vectorstore()
    return {"message": "Backend memory wiped"}