from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware


sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)
app = FastAPI()

origins = ["http://localhost:8080", "null"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class Text(BaseModel):
    text: str

@app.post("/")
async def inference(text: Text) -> Dict[str, str]:
    try:
        out = sentiment_pipeline(text.text)
        label = out[0]["label"]
        
        returnLabel = "Negative 😔"
        if label == "POSITIVE":
            returnLabel = "Positive 😊"

        return {"LABEL": returnLabel}
    

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "hi"}