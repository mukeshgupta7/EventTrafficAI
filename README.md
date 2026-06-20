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

## Future Scope of Improvement

### 🔮 Planned Enhancements (See [FUTURE_ENHANCEMENTS.md](FUTURE_ENHANCEMENTS.md) for detailed roadmap)

#### Phase 1: Real-Time Integration (Q3 2026)
- **Live GPS feeds** from vehicles (Uber, Waze, city sensors)
- **IoT sensor network** for traffic lights, crowd density, barricade status
- **Real-time manpower tracking** with GPS badges
- **Dynamic weather integration** (rain, fog, visibility effects)

#### Phase 2: Advanced ML & Forecasting (Q4 2026)
- **Time-series forecasting** (LSTM/GRU models for 15-min to 4-hour predictions)
- **What-if scenario analysis** ("If we deploy X officers, delay reduces by Y minutes")
- **Deep learning integration** (Computer vision for crowd counting, NLP for auto-extraction)
- **Anomaly detection** for sudden incidents

#### Phase 3: Personalization & UX (Q1 2027)
- **Stakeholder dashboards** (Police Commissioner, Traffic Officers, Event Organizers, Public)
- **Mobile app** (Android/iOS) with real-time diversion routes
- **Voice assistant integration** (Alexa/Google Assistant for quick queries)
- **Multi-language support** and accessibility features

#### Phase 4: Optimization & Automation (Q2 2027)
- **Resource optimization engine** using Linear Programming to minimize cost & delay
- **Automated permit approval system** for event organizers (self-service portal)
- **Auto-scaling infrastructure** with cloud-native architecture

#### Phase 5: Analytics & Learning (Q3 2027)
- **Post-event feedback loops** (QR codes, officer reports, social media sentiment)
- **Continuous model retraining** with monthly event learnings
- **Predictive analytics dashboard** (trends, seasonality, comparative metrics)

#### Phase 6: Multi-City Expansion (Q4 2027)
- **Transfer learning** across cities (Bangalore → Delhi, Mumbai, Hyderabad)
- **Federated learning** for privacy-preserving data sharing
- **External API integrations** (Uber, Google Maps, Emergency Services)

#### Phase 7: Governance & Compliance (Ongoing)
- **Audit trails** for every prediction and decision
- **GDPR/India DPA compliance** with encryption and anonymization
- **Fairness audits** to prevent bias against specific corridors/communities
- **Transparency reports** on system accuracy and resource efficiency

#### Phase 8: Advanced Features (2028+)
- **Multi-event coordination** (overlapping festivals + road work)
- **Sustainability tracking** (carbon footprint calculations, green routing)
- **Chaos engineering** for system resilience testing
- **Automatic incident response** with pre-planned playbooks

### 📊 Success Metrics for Enhancements

| Phase | Target KPI |
|-------|-----------|
| Phase 1 | Live data latency < 30 sec, prediction accuracy 85% |
| Phase 2 | Forecast RMSE < 10%, sensitivity analysis provided |
| Phase 3 | 50% app adoption, NPS > 60 |
| Phase 4 | 20% reduction in deployment cost, approval time < 4 hours |
| Phase 5 | 15% model accuracy improvement, user satisfaction 4.5/5 |
| Phase 6 | Expansion to 3+ cities, API revenue $100K/year |
| Phase 7 | 100% audit coverage, zero security incidents |
| Phase 8 | 30% emission reduction, 5-min avg response time |

### 💡 Key Innovations Under Development

1. **Self-learning system** that improves from every event
2. **Predictive permit approval** (auto-approve low-risk events)
3. **Inter-city intelligence** (learn from Mumbai patterns to improve Delhi)
4. **Carbon-aware routing** (balance efficiency with sustainability)
5. **Emergency service optimization** (ambulance/fire routing integrated)

### 🎯 Long-Term Vision (2028+)

Transform from a **static prediction tool** to an **autonomous city-wide traffic management platform** that:
- Detects events automatically from news/social media
- Predicts impact in real-time
- Recommends & executes optimal strategies
- Learns and improves continuously
- Operates across multiple cities

**For detailed technical specifications, architecture diagrams, and timeline, see [FUTURE_ENHANCEMENTS.md](FUTURE_ENHANCEMENTS.md)**
