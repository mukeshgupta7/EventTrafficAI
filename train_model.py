import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('processed_data.csv')

# Encode categorical
le_cause = LabelEncoder()
le_corridor = LabelEncoder()
df['cause_encoded'] = le_cause.fit_transform(df['event_cause'].fillna('unknown'))
df['corridor_encoded'] = le_corridor.fit_transform(df['corridor'].fillna('unknown'))

# Features for prediction
features = ['hour', 'day_of_week', 'month', 'is_weekend', 'is_peak_hour', 
            'is_planned', 'cause_encoded', 'corridor_encoded']
X = df[features].fillna(0)
y = df['impact_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

joblib.dump(model, 'traffic_model.pkl')
joblib.dump(le_cause, 'cause_encoder.pkl')
joblib.dump(le_corridor, 'corridor_encoder.pkl')
print("Model saved")
