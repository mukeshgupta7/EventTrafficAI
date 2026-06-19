import streamlit as st
from recommendation_engine import recommend_resources
import joblib
import numpy as np

st.set_page_config(page_title="Traffic Congestion Management", page_icon="🚦")

st.title("🚦 Event-Driven Congestion Management")
st.markdown("Forecast traffic impact and get resource recommendations")

@st.cache_resource
def load_models():
    model = joblib.load('traffic_model.pkl')
    cause_encoder = joblib.load('cause_encoder.pkl')
    corridor_encoder = joblib.load('corridor_encoder.pkl')
    return model, cause_encoder, corridor_encoder

model, cause_encoder, corridor_encoder = load_models()

col1, col2 = st.columns(2)

with col1:
    event_type = st.selectbox("Event Type", ["unplanned", "planned"])
    event_cause = st.selectbox("Event Cause", cause_encoder.classes_)
    corridor = st.selectbox("Corridor", corridor_encoder.classes_)

with col2:
    hour = st.slider("Hour (0-23)", 0, 23, 9)
    day = st.slider("Day (0=Mon, 6=Sun)", 0, 6, 0)
    month = st.slider("Month", 1, 12, 6)

road_closure = st.checkbox("Road Closure Required")

if st.button("🔍 Predict Impact & Get Recommendations", type="primary"):
    is_weekend = 1 if day >= 5 else 0
    is_peak = 1 if hour in [8,9,17,18,19] else 0
    is_planned = 1 if event_type == 'planned' else 0
    
    try:
        cause_enc = cause_encoder.transform([event_cause])[0]
        corridor_enc = corridor_encoder.transform([corridor])[0]
    except:
        cause_enc = 0
        corridor_enc = 0
    
    features = np.array([[hour, day, month, is_weekend, is_peak, is_planned, cause_enc, corridor_enc]])
    impact = int(model.predict(features)[0])
    
    result = recommend_resources(impact, event_type, road_closure, event_cause, corridor, hour, day, is_peak, is_weekend)
    
    level = "Low" if impact <= 1 else "Medium" if impact <= 3 else "High"
    st.success(f"**Impact Level**: {level} (Score: {impact})")
    
    st.subheader("🚦 Traffic Impact Assessment")
    col1, col2, col3 = st.columns(3)
    col1.metric("Expected Delay", f"{result['traffic_impact_assessment']['expected_delay_minutes']} min")
    col2.metric("Affected Radius", f"{result['traffic_impact_assessment']['affected_radius_km']} km")
    col3.metric("Congestion Level", result['traffic_impact_assessment']['congestion_level'])
    
    st.subheader("👮 Manpower Deployment")
    col1, col2 = st.columns(2)
    col1.metric("Total Personnel", result['total_personnel'])
    col2.metric("Setup Time", f"{result['estimated_setup_time_minutes']} min")
    
    with st.expander("📋 Deployment Strategy"):
        for key, value in result['manpower_deployment']['deployment_strategy'].items():
            st.write(f"**{key.replace('_', ' ').title()}**: {value}")
        st.write("**Deployment Points:**")
        for point in result['manpower_deployment']['deployment_points']:
            st.write(f"📍 {point}")
    
    st.subheader("🚧 Barricading Plan")
    col1, col2 = st.columns(2)
    col1.metric("Total Barricades", result['barricades'])
    
    with st.expander("📊 Distribution & Signage"):
        st.write("**Distribution:**")
        for key, value in result['barricade_plan']['distribution'].items():
            st.write(f"- {key.replace('_', ' ').title()}: {value} barricades")
        st.write("\n**Signage Required:**")
        for sign in result['barricade_plan']['signage']:
            st.write(f"🪧 {sign}")
    
    st.subheader("🔀 Alternate Routes")
    for route in result['alternate_routes']:
        st.info(f"🛣️ {route}")
    
    st.subheader("📋 Action Plan")
    for i, action in enumerate(result['diversions'], 1):
        st.write(f"{i}. {action}")
    
    with st.expander("📊 Historical & Real-Time Data"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Historical Insights:**")
            st.write(f"- Past events: {result['historical_insights']['similar_past_events']}")
            st.write(f"- Avg impact: {result['historical_insights']['historical_avg_impact']}")
        with col2:
            st.write("**Real-Time Factors:**")
            st.write(f"- Multiplier: {result['real_time_factors']['current_multiplier']}x")
            st.write(f"- Adjusted impact: {result['real_time_factors']['adjusted_impact_score']}")
