

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Evaluation import Evaluation
from Model2 import ReadEval

class Prompting(BaseModel):
    question:str

class Template(BaseModel):
    faithfulness:float
    answer_relevancy:float
    context_precision:float
    context_recall:float
    answer_correctness:float
    harmfulness:float

# from Model import ChatBot
from Model2 import ChatBot

app=FastAPI()

origins = [
    "localhost",
    "localhost:8080",
    "http://localhost:5173",   #vue!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"Message": "It's Home page"}

@app.post("/model")
async def Boot(ans: Prompting):
    try:
        value=ChatBot(ans.question)
        result=value.Bot()
        return {'result':result}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@app.get("/evaluation")
async def evalution():
    try:
        value=ReadEval()
        result=value.Read()

        evaluation_data = {
            'faithfulness': float(result['faithfulness']),
            'answer_relevancy': float(result['answer_relevancy']),
            'context_precision': float(result['context_precision']),
            'context_recall': float(result['context_recall']),
            'harmfulness': float(result['harmfulness']),
            'answer_correctness': float(result['answer_correctness'])
        }
        return {'result': evaluation_data}
    except Exception as e:
        print(str(e))
        return str(e)

