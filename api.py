from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from recommendation_engine import recommend_resources

app = FastAPI(title="Event-Driven Congestion Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('traffic_model.pkl')
cause_encoder = joblib.load('cause_encoder.pkl')
corridor_encoder = joblib.load('corridor_encoder.pkl')

class EventInput(BaseModel):
    event_type: str
    event_cause: str
    corridor: str
    hour: int
    day_of_week: int
    month: int
    is_weekend: int
    is_peak_hour: int
    requires_road_closure: bool

@app.get("/")
def root():
    return {"message": "Event-Driven Congestion Management API", "version": "1.0"}

@app.post("/predict")
def predict_impact(event: EventInput):
    is_planned = 1 if event.event_type == 'planned' else 0
    
    try:
        cause_enc = cause_encoder.transform([event.event_cause])[0]
    except:
        cause_enc = 0
    
    try:
        corridor_enc = corridor_encoder.transform([event.corridor])[0]
    except:
        corridor_enc = 0
    
    features = np.array([[
        event.hour, event.day_of_week, event.month, 
        event.is_weekend, event.is_peak_hour, is_planned,
        cause_enc, corridor_enc
    ]])
    
    impact_score = int(model.predict(features)[0])
    
    resources = recommend_resources(
        impact_score, 
        event.event_type, 
        event.requires_road_closure,
        event_cause=event.event_cause,
        corridor=event.corridor,
        hour=event.hour,
        day_of_week=event.day_of_week,
        is_peak_hour=event.is_peak_hour,
        is_weekend=event.is_weekend
    )
    
    return {
        "predicted_impact_score": impact_score,
        "impact_level": "Low" if impact_score <= 1 else "Medium" if impact_score <= 3 else "High",
        "recommendations": resources
    }

@app.get("/causes")
def get_causes():
    return {"causes": list(cause_encoder.classes_)}

@app.get("/corridors")
def get_corridors():
    return {"corridors": list(corridor_encoder.classes_)}
