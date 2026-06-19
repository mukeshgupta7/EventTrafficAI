import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv')

# Parse datetime
df['start_datetime'] = pd.to_datetime(df['start_datetime'], errors='coerce')
df['end_datetime'] = pd.to_datetime(df['end_datetime'], errors='coerce')

# Extract features
df['hour'] = df['start_datetime'].dt.hour
df['day_of_week'] = df['start_datetime'].dt.dayofweek
df['month'] = df['start_datetime'].dt.month
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
df['is_peak_hour'] = df['hour'].isin([8, 9, 17, 18, 19]).astype(int)

# Duration
df['duration_hours'] = (df['end_datetime'] - df['start_datetime']).dt.total_seconds() / 3600

# Event impact score (proxy based on priority and road closure)
df['impact_score'] = 0
df.loc[df['priority'] == 'High', 'impact_score'] = 3
df.loc[df['priority'] == 'Low', 'impact_score'] = 1
df.loc[df['requires_road_closure'] == True, 'impact_score'] += 2

# Encode categorical
df['is_planned'] = (df['event_type'] == 'planned').astype(int)
event_causes = df['event_cause'].fillna('unknown')

# Save processed data
processed = df[['event_type', 'event_cause', 'latitude', 'longitude', 'requires_road_closure',
                'hour', 'day_of_week', 'month', 'is_weekend', 'is_peak_hour', 
                'duration_hours', 'priority', 'corridor', 'impact_score', 'is_planned']].dropna(subset=['latitude', 'longitude'])

processed.to_csv('processed_data.csv', index=False)
print(f"Processed {len(processed)} events")
print(f"\nEvent types: {processed['event_type'].value_counts().to_dict()}")
print(f"\nEvent causes: {processed['event_cause'].value_counts().to_dict()}")
