
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.mistral_wrapper import MistralChain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    query: str

qa_chain = MistralChain()

@app.post("/ask")
def ask_question(question: Question):
    try:
        response = qa_chain.invoke(question.query)
        return {"response": response}
    except Exception as e:
        return {"response": f"Erreur : {e}"}
