from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel

app = FastAPI()

class request_body(BaseModel):
    
    data: str
    
@app.post('/predict')

def predict(data: request_body):
     
	data = list(data.dict().values())

	model = joblib.load('./Models/text_emotion_classifier.pkl')

	emotion = model.predict(data)

	return { 'emotion': emotion[0]}

@app.get('/')

def main():
    
    return {'message': 'Welcome to Text Emotion Classifier API'}
