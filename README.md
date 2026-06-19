# Event-Driven Congestion Management System

Deployable prototype for forecasting event-related traffic impact and recommending optimal resource allocation.

## Problem Statement

Political rallies, festivals, sports events, construction activities, and sudden gatherings create localized traffic breakdowns. This system uses **historical and real-time data** to:
- Forecast event-related traffic impact
- Recommend optimal manpower deployment
- Suggest barricading requirements
- Generate diversion plans

## How Historical & Real-Time Data Drive Predictions

### Historical Data Analysis
The system analyzes **8,173 past events** to identify patterns:
- **Location-based patterns**: Events at specific corridors (e.g., Hosur Road during peak hours)
- **Cause frequency**: Vehicle breakdowns (60%), construction (6%), public events (1%)
- **Peak hour correlation**: 85% of high-impact events occur during 8-9 AM or 5-7 PM
- **Historical impact scores**: Average impact by event type and location

### Real-Time Factors
Current conditions dynamically adjust predictions:
- **Time of day**: Peak hours increase impact by 40%
- **Day of week**: Weekend events have 20% lower impact
- **Seasonal patterns**: Month-based traffic variations
- **Road closure status**: Immediate +3 personnel, +10 barricades

### Combined Intelligence
```
Adjusted Impact = ML Prediction × Real-Time Multiplier + Historical Pattern Adjustment
```

**Example**: Vehicle breakdown on Hosur Road
- Base ML prediction: Impact 3
- Historical data: 120 similar incidents, avg impact 3.2
- Real-time: Peak hour (8 AM Monday) → 1.4x multiplier
- **Final adjusted impact**: 4.2 → Deploy 8 police, 20 barricades

## Features

- **ML-Based Impact Prediction**: 91% accuracy using Random Forest classifier
- **Traffic Impact Assessment**: Quantified delay (minutes), affected radius (km), congestion level
- **Optimal Manpower Deployment**: Detailed personnel allocation with specific deployment points
- **Strategic Barricading**: Calculated distribution (40% event, 30% approach, 30% diversion) with signage plan
- **Location-Specific Diversions**: Real alternate routes for major corridors (Hosur Road, Tumkur Road, ORR, etc.)
- **Actionable Plans**: Step-by-step deployment strategy, not generic recommendations
- **REST API**: Easy integration with existing systems
- **Interactive Dashboard**: Real-time predictions with complete traffic management plans

## Quick Start

### Option 1: Docker (Recommended)

```bash
docker-compose up -d
```

Access:
- API: http://localhost:8000
- Dashboard: http://localhost

### Option 2: Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start API:
```bash
python -m uvicorn api:app --host 0.0.0.0 --port 8000
```
Or on Windows:
```bash
start_api.bat
```

3. Open `index.html` in browser

## API Endpoints

- `GET /` - API info
- `POST /predict` - Get impact prediction and recommendations
- `GET /causes` - List available event causes
- `GET /corridors` - List available corridors

## System Components

1. **Data Preprocessing** (`preprocess.py`): Feature engineering from historical event data
2. **ML Model** (`train_model.py`): Random Forest classifier for impact prediction
3. **Recommendation Engine** (`recommendation_engine.py`): Resource allocation logic
4. **API** (`api.py`): FastAPI REST service
5. **Dashboard** (`index.html`): Interactive web UI

## Model Performance

- **Accuracy**: 91%
- **Training Data**: 8,173 events (7,706 unplanned, 467 planned)
- **Features**: Time-based, event type, cause, corridor, road closure

## Resource Scaling

| Impact Level | Personnel | Barricades | Setup Time |
|-------------|-----------|------------|------------|
| Low (1-2)   | 2-4       | 5-8        | 15-25 min  |
| Medium (3)  | 6-8       | 12         | 30 min     |
| High (4-5)  | 10-13     | 20+        | 40+ min    |

## Deployment Notes

- Trained models included (`.pkl` files)
- CORS enabled for frontend integration
- Supports both planned and unplanned events
- Handles road closure scenarios

## Future Enhancements

- Real-time traffic data integration
- Historical learning from resolved events
- Mobile app for field officers
- GIS integration for route visualization
