import streamlit as st
import random

st.title("Simple Prediction App")

mode = st.radio("Choose Prediction Type", ["Yes / No", "Red / Green"])

if st.button("Predict"):
    prediction = random.choice(["Yes", "No"]) if mode == "Yes / No" else random.choice(["Red", "Green"])
    st.success(f"Prediction: {prediction}")
