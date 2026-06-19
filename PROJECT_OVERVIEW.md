# Project Overview: Event-Driven Congestion Management

## 🎯 Mission
Answer: **"How can historical and real-time data be used to forecast event-related traffic impact and recommend optimal manpower, barricading, and diversion plans?"**

## 📁 Project Structure

### Core Application Files
```
├── api.py                      # FastAPI REST service
├── recommendation_engine.py    # Historical + real-time intelligence
├── index.html                  # Interactive web dashboard
├── train_model.py             # ML model training script
├── preprocess.py              # Data preprocessing script
└── test_scenarios.py          # Verification tests
```

### Data & Models
```
├── Astram event data...csv    # Original 8,173 events (raw data)
├── processed_data.csv         # Cleaned & feature-engineered data
├── traffic_model.pkl          # Trained RandomForest (91% accuracy)
├── cause_encoder.pkl          # Event cause label encoder
└── corridor_encoder.pkl       # Corridor label encoder
```

### Deployment
```
├── Dockerfile                 # Container definition
├── docker-compose.yml         # Multi-service orchestration
├── start_api.bat             # Windows quick-start script
├── requirements.txt          # Python dependencies
└── .dockerignore             # Docker build exclusions
```

### Documentation
```
├── README.md                  # Main project documentation
├── SOLUTION_SUMMARY.md       # Comprehensive solution overview
├── HOW_IT_WORKS.md           # Technical deep-dive
├── DEPLOYMENT.md             # Quick deployment guide
└── DEMO_GUIDE.md             # Presentation script
```

## 🚀 Quick Start Commands

### For Demo/Testing
```bash
# Windows
start_api.bat

# Then open index.html in browser
# Click "Load Example Scenario" → "Predict"
```

### For Production
```bash
docker-compose up -d
# Access at http://localhost
```

### For Development
```bash
pip install -r requirements.txt
python preprocess.py          # Process data
python train_model.py         # Train model
python test_scenarios.py      # Test scenarios
uvicorn api:app --reload      # Start API
```

## 📊 System Capabilities

### What It Does
✅ Predicts traffic impact (1-5 scale) with 91% accuracy
✅ Analyzes 8,173 historical events for patterns
✅ Applies real-time multipliers (peak hour, weekend, etc.)
✅ Recommends personnel (2-19), barricades (5-30), setup time
✅ Generates context-aware diversion plans
✅ Explains every decision with historical and real-time data

### Key Features
- **Historical Learning**: "170 past incidents at Hosur Road inform this"
- **Real-Time Intelligence**: Peak hour +40%, Weekend -20% adjustments
- **Transparent AI**: Shows why it made each recommendation
- **Deployable**: Docker-ready, production-grade API
- **Interactive**: User-friendly dashboard with visual indicators

## 🎓 How to Read the Documentation

### For Quick Understanding
1. **README.md** - Start here for overview and features
2. **DEPLOYMENT.md** - Try the demo scenarios
3. **DEMO_GUIDE.md** - Perfect for presentations

### For Technical Deep-Dive
1. **HOW_IT_WORKS.md** - Detailed algorithm explanation
2. **SOLUTION_SUMMARY.md** - Complete technical overview
3. **test_scenarios.py** - See it in action with code

### For Presentation/Demo
1. **DEMO_GUIDE.md** - Step-by-step demo script
2. Load example scenario in dashboard
3. Show contrast (9 AM vs 11 PM)

## 🔑 Key Statistics

- **Model Accuracy**: 91%
- **Historical Data**: 8,173 events
- **Event Types**: Planned (6%) & Unplanned (94%)
- **Top Cause**: Vehicle breakdown (60%)
- **Corridors Tracked**: 14+ major Bangalore corridors
- **Resource Range**: 2-19 personnel, 5-30 barricades
- **Impact Adjustments**: -30% to +40% based on real-time factors

## 🎬 Demo Scenarios

### Scenario 1: Peak Hour Breakdown
**Input:** Hosur Road, vehicle_breakdown, 9 AM Monday
**Result:** 15 personnel (1.4x multiplier, 170 past incidents)

### Scenario 2: Late Night Weekend
**Input:** Hosur Road, vehicle_breakdown, 11 PM Sunday  
**Result:** 10 personnel (1.1x multiplier, reduced resources)

### Scenario 3: Planned Event + Closure
**Input:** CBD 2, public_event, 6 PM Sunday, road closure
**Result:** 19 personnel, 30 barricades, proactive advisories

## 🏆 Problem Statement Addressed

| Challenge | Solution |
|-----------|----------|
| ❌ Event impact not quantified | ✅ ML predicts 1-5 impact score (91% accurate) |
| ❌ Experience-driven deployment | ✅ Data-driven recommendations from 8,173 events |
| ❌ No post-event learning | ✅ Historical database + pattern recognition |

## 🔧 Technology Stack

- **ML**: scikit-learn RandomForest
- **API**: FastAPI with CORS
- **Frontend**: Vanilla JS + HTML5
- **Data**: pandas, numpy
- **Deployment**: Docker + docker-compose
- **Platform**: Python 3.11

## 📈 System Flow

```
User Input → API → ML Model → Base Impact Score
                               ↓
                    Recommendation Engine
                    ├── Historical Analysis (8,173 events)
                    ├── Real-Time Multiplier (peak, weekend, etc.)
                    └── Resource Calculation
                               ↓
                    Response: Personnel + Barricades + Diversions
                               ↓
                    Dashboard Display with Insights
```

## 🎯 Next Steps After Demo

1. ✅ System is production-ready
2. ✅ Deploy with `docker-compose up -d`
3. ✅ Integrate with existing traffic management systems
4. ✅ Start collecting new events to improve accuracy
5. ⏭️ Future: Real-time traffic API, weather data, GIS visualization

## 📞 Getting Started Checklist

- [ ] Read README.md for overview
- [ ] Run `start_api.bat` (Windows) or `uvicorn api:app`
- [ ] Open `index.html` in browser
- [ ] Click "Load Example Scenario"
- [ ] Click "Predict Impact & Get Recommendations"
- [ ] See historical data (170 past events) + real-time factors (1.4x multiplier)
- [ ] Try changing time to 11 PM - watch resources adjust
- [ ] Run `python test_scenarios.py` to see programmatic testing
- [ ] Deploy with Docker: `docker-compose up -d`

## 📚 Files to Share in Demo

**Essential:**
- index.html (interactive demo)
- DEMO_GUIDE.md (presentation script)
- SOLUTION_SUMMARY.md (technical overview)

**If Technical Audience:**
- recommendation_engine.py (see the algorithm)
- test_scenarios.py (run live tests)
- HOW_IT_WORKS.md (deep-dive explanation)

---

**Built to solve:** Event-driven congestion with historical learning + real-time intelligence
**Accuracy:** 91% impact prediction
**Data:** 8,173 historical events
**Status:** ✅ Production-ready, deployable prototype
