FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .
COPY recommendation_engine.py .
COPY traffic_model.pkl .
COPY cause_encoder.pkl .
COPY corridor_encoder.pkl .
COPY processed_data.csv .
COPY index.html .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
