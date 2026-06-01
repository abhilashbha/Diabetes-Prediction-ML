import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ===============================
# LOAD MODEL (FAST)
# ===============================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ===============================
# UI
# ===============================
st.title("Diabetes Prediction System")

st.write("Enter patient details:")

# Inputs
HighBP = st.selectbox("High Blood Pressure (0/1)", [0,1])
HighChol = st.selectbox("High Cholesterol (0/1)", [0,1])
CholCheck = st.selectbox("Cholesterol Check (0/1)", [0,1])
BMI = st.number_input("BMI", 10.0, 60.0)
Smoker = st.selectbox("Smoker (0/1)", [0,1])
Stroke = st.selectbox("Stroke (0/1)", [0,1])
HeartDisease = st.selectbox("Heart Disease (0/1)", [0,1])
PhysActivity = st.selectbox("Physical Activity (0/1)", [0,1])
Fruits = st.selectbox("Fruits Intake (0/1)", [0,1])
Veggies = st.selectbox("Vegetables Intake (0/1)", [0,1])
HvyAlcohol = st.selectbox("Heavy Alcohol (0/1)", [0,1])
AnyHealthcare = st.selectbox("Healthcare Access (0/1)", [0,1])
NoDocbcCost = st.selectbox("No Doctor due to Cost (0/1)", [0,1])
GenHlth = st.slider("General Health (1-5)", 1, 5)
MentHlth = st.number_input("Mental Health Days", 0, 30)
PhysHlth = st.number_input("Physical Health Days", 0, 30)
DiffWalk = st.selectbox("Difficulty Walking (0/1)", [0,1])
Sex = st.selectbox("Sex (0=F,1=M)", [0,1])
Age = st.slider("Age Group (1-13)", 1, 13)
Education = st.slider("Education Level (1-6)", 1, 6)
Income = st.slider("Income Level (1-8)", 1, 8)

# ===============================
# PREDICTION
# ===============================
if st.button("Predict"):
    
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke,
                            HeartDisease, PhysActivity, Fruits, Veggies,
                            HvyAlcohol, AnyHealthcare, NoDocbcCost,
                            GenHlth, MentHlth, PhysHlth, DiffWalk,
                            Sex, Age, Education, Income]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")