from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import uvicorn

app= FastAPI()
# Modell
modelpath="./BERT_model_Class_Weights"
tokenizer = AutoTokenizer.from_pretrained(modelpath)
model=AutoModelForSequenceClassification.from_pretrained(modelpath)

class Input(BaseModel):
    text:str
@app.post("/predict")
def predict(input: Input):
    tokens=tokenizer(input.text,return_tensor="pt",padding=True,truncation=True, max_length=175)
    with torch.no_grad():
        output=model(**tokens)
        logits=output.logits
        prob=torch.sigmoid(logits)[0].item()
    label="Hasskommentar" if prob >=0.5 else "Kein Hasskommentar"
    return{
        "label":label,
        "confidence":prob
    }