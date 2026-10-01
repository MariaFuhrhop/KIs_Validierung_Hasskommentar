from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import uvicorn


app = FastAPI()

print("APP ID:", id(app))

#modell laden
modelpath = "./BERT_model_Class_Weights"
tokenizer = AutoTokenizer.from_pretrained(modelpath) #der tokenizer wird geladen
model = AutoModelForSequenceClassification.from_pretrained(modelpath) #das fingetunete Modell wird vom Modellpfad geladen

#Modell in den Evaluierungsmodus setzen
model.eval()

print("Model device:", next(model.parameters()).device)
print("Model labels:", model.config.id2label)
print("Number of labels:", model.config.num_labels)
print("TEST MAIN WIRD GELADEN")

class Input(BaseModel):
    text: str

@app.get("/") #API wird gebildet
def root():
    return {
        "message": "API läuft"
    }

#die Klassifizierung wird
@app.post("/predict")
def predict(input: Input): #die Klasse kriegt den Input vom Frontend

    print("1. Request angekommen")
    print("Text:", input.text)

    inputs = tokenizer(input.text,return_tensors="pt",truncation=True,padding=True) #der kommentar wird tokenisiert, gepadded und zur not auch abgeschnitten
    print("2. Tokenisierung erfolgreich")
    print(inputs)
    with torch.no_grad():
        outputs = model(**inputs) #input wird in das Modell eingegeben und der output als output gespeichert
    print("Logits:", outputs.logits)
    probabilities = torch.softmax(outputs.logits, dim=1) #die logist werden in wahrscheinlichkeiten umgerechenet
    print("Probabilities:", probabilities)
    prediction = torch.argmax(probabilities, dim=1).item() #die Klassifizierung wird gerechnet mit torch.argmax
    print("5. Prediction:", prediction)
    confidence = probabilities[0][prediction].item() #die Wahrscheinlichkeit der Klassifizierung wird gerechnet
    print("Model labels:", model.config.id2label)
    if prediction == 1: #die prediction wird von 0 & 1 in Kein Hasskommentar und Hasskommentar benannt
        label = "Hasskommentar"
    else:
        label = "Kein Hasskommentar"
    #Ausgabe der KI Infos
    print("Prediction:", prediction)
    print("Confidence:", confidence)
    print("Label:", label)
    print("Probabilities:", probabilities.tolist())
    #Rückgabe der ki infos für das frontend
    return {
        "label": label,
        "confidence": confidence,
        "hateProbability": probabilities[0][1].item(),
        "notHateProbability": probabilities[0][0].item()
    }

for route in app.routes: #app.routes enthält die registrierten Endpunkte der fast api
    print(route.path)

#es wird mit dem Run button laufen gelassen
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)