from fastapi import FastAPI
from pydantic import BaseModel
from core.predict import predict

app = FastAPI(title="NLP Support Classifier API")

class RequestBody(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(req: RequestBody):
    result = predict(req.text)
    return {
        "input": req.text,
        "prediction": result
    }