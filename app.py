import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("Student Placement Prediction")

def load_models():
    model = joblib.load("placement_model.pkl")
    scaler = joblib.load("placement_model_scaler.pkl")
    le_extracurricular = joblib.load("le_extracaricular.pkl")
    le_department = joblib.load("le_department.pkl")
    return model, scaler, le_extracurricular, le_department

model, scaler, le_extracurricular, le_department = load_models()

st.header("Enter Student Details...")

cgpa=st.slider("Select your CGPA", min_value=5, max_value=10, value=7)
iq=st.slider("IQ", min_value=80, max_value=140, value=110)
commu=st.slider("Communication Skills", min_value=0, max_value=10, value=7)
tech=st.slider("Technical Skills", min_value=0, max_value=10, value=7)
interships=st.slider("Internships", min_value=0, max_value=3, value=2)
projects=st.slider("Projects", min_value=0, max_value=5, value=3)
extracurricular=st.selectbox("Extracurricular", options=["Low", "Medium", "High"])
department=st.selectbox("Department", options=["CSE", "ME", "CE", "IT", "EEE", "ECE"])

if st.button("Predict Placement"):
    # Encode categorical variables
    extracurricular_encoded = le_extracurricular.transform([extracurricular])[0]
    department_encoded = le_department.transform([department])[0]

    # convert to numpy array to ensure all values are numerical.
    features= np.array([[cgpa, iq, commu, tech, interships, projects, extracurricular_encoded, department_encoded]])

    features_scaled = scaler.transform(features)

    # Make prediction
    prediction = model.predict(features_scaled)

    if prediction[0] == 1:
        st.success("The student is likely to be placed.")
    else:
        st.error("The student is unlikely to be placed.")