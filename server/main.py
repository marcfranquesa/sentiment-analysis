from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from typing import Dict

sentiment_pipeline = pipeline("sentiment-analysis")
app = FastAPI()


class Text(BaseModel):
    text: str

@app.post("/")
async def inference(text: Text) -> Dict[str, str]:
    out = sentiment_pipeline(text.text)
    return {"LABEL": out[0]["label"]}

@app.get("/")
async def root() -> Dict[str, str]:
    return "hi"