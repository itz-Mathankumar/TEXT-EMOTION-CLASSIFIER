from fastapi import FastAPI

import joblib

from pydantic import BaseModel

app = FastAPI()

class request_body(BaseModel):
    
    data: str
    
model = joblib.load('./Models/text_emotion_classifier.pkl')
    
@app.post('/predict')

def predict(data: request_body):
     
	data = list(data.dict().values())

	emotion = model.predict(data)

	return { 'emotion': emotion[0]}

@app.post('/predict/{emotion}')

def predict_emotion(emotion: str, request_body: request_body):
    
    valid_emotions = ['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'shame', 'surprise']
    
    if emotion not in valid_emotions:
        
        return {'error': 'Invalid emotion'}

    data = [request_body.data]
    
    class_probabilities = model.predict_proba(data)
    
    emotion_index = valid_emotions.index(emotion)
    
    emotion_score = class_probabilities[0][emotion_index]

    return {emotion: emotion_score}

@app.get('/')

def main():
    
    return {'message': 'Welcome to Text Emotion Classifier API'}
