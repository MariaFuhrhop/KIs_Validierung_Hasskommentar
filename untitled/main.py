from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import uvicorn


app = FastAPI()

print("APP ID:", id(app))

# Modell laden
modelpath = "./BERT_model_Class_Weights"
tokenizer = AutoTokenizer.from_pretrained(modelpath)
model = AutoModelForSequenceClassification.from_pretrained(modelpath)

# Modell in den Evaluierungsmodus setzen
model.eval()

print("Model device:", next(model.parameters()).device)
print("Model labels:", model.config.id2label)
print("Number of labels:", model.config.num_labels)
print("TEST MAIN WIRD GELADEN")

class Input(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "message": "API läuft"
    }
@app.post("/predict")
def predict(input: Input):

    print("1. Request angekommen")
    print("Text:", input.text)

    inputs = tokenizer(input.text,return_tensors="pt",truncation=True,padding=True)
    print("2. Tokenisierung erfolgreich")
    print(inputs)
    with torch.no_grad():
        outputs = model(**inputs)
    print("3. Modell erfolgreich ausgeführt")
    print("Logits:", outputs.logits)
    probabilities = torch.softmax(outputs.logits, dim=1)
    print("4. Softmax erfolgreich")
    print("Probabilities:", probabilities)
    prediction = torch.argmax(probabilities, dim=1).item()
    print("5. Prediction:", prediction)
    confidence = probabilities[0][prediction].item()
    print("Model labels:", model.config.id2label)
    if prediction == 1:
        label = "Hasskommentar"
    else:
        label = "Kein Hasskommentar"
    print("Prediction:", prediction)
    print("Confidence:", confidence)
    print("Label:", label)
    print("Probabilities:", probabilities.tolist())
    return {
        "label": label,
        "confidence": confidence,
        "hateProbability": probabilities[0][1].item(),
        "notHateProbability": probabilities[0][0].item()
    }

for route in app.routes:
    print(route.path)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)