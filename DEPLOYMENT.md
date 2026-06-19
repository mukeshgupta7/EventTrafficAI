# Quick Deployment Guide

## For Demo

### Easiest Method (Local):
1. Open terminal in this directory
2. Run: `start_api.bat`
3. Open `index.html` in your browser
4. Start entering event details and get predictions

### Docker Method:
```bash
docker-compose up -d
```
Then access:
- Dashboard: http://localhost
- API: http://localhost:8000

## Testing the System

### Example Event Scenarios:

**Scenario 1: Morning Vehicle Breakdown (Peak Hour)**
- Event Type: Unplanned
- Cause: vehicle_breakdown
- Corridor: Hosur Road
- Hour: 9
- Day: 0 (Monday)
- Road Closure: No

*Expected Results:*
- Historical: 170 past incidents at this location
- Real-time multiplier: 1.4x (peak hour)
- Resources: 15 personnel, 20 barricades
- Diversions include high-frequency location warning

**Scenario 2: Planned Cricket Match (Weekend Evening)**
- Event Type: Planned
- Cause: public_event
- Corridor: CBD 2
- Hour: 18
- Day: 6 (Sunday)
- Road Closure: Yes

*Expected Results:*
- Real-time multiplier: 1.2x (peak hour, weekend)
- Resources: 19 personnel, 30 barricades
- Pre-event advisory included

**Scenario 3: Late Night Weekend Breakdown**
- Event Type: Unplanned
- Cause: vehicle_breakdown
- Corridor: Hosur Road
- Hour: 23
- Day: 6 (Sunday)
- Road Closure: No

*Expected Results:*
- Real-time multiplier: 1.1x (weekend, late night)
- Resources: 10 personnel, 12 barricades (reduced)
- Lower adjusted impact score

## What Gets Predicted

1. **Impact Score** (1-5 scale)
2. **Impact Level** (Low/Medium/High)
3. **Manpower Requirements**:
   - Traffic Police
   - Supervisors
   - Support Staff
4. **Infrastructure**:
   - Number of barricades
   - Estimated setup time
5. **Diversion Plans**:
   - Specific action items for traffic management

## API Usage

### Get Prediction:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "event_type": "unplanned",
    "event_cause": "vehicle_breakdown",
    "corridor": "Hosur Road",
    "hour": 9,
    "day_of_week": 0,
    "month": 6,
    "is_weekend": 0,
    "is_peak_hour": 1,
    "requires_road_closure": false
  }'
```

### List Available Options:
```bash
curl http://localhost:8000/causes
curl http://localhost:8000/corridors
```

## Stopping the System

**Local**: Press Ctrl+C in the terminal running uvicorn

**Docker**: 
```bash
docker-compose down
```
