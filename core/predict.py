import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_path = "./model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

labels_map = {
    0: "remboursement",
    1: "problème technique",
    2: "positif",
    3: "livraison",
    4: "achat / commande",
    5: "autre"
}

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=1).item()

    return labels_map[pred]