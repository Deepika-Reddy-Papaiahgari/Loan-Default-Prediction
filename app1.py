import joblib
import numpy as np
import os
import streamlit as st

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

model_path = os.path.join(BASE_DIR,"Loan-default-prediction", "models", "loan_model.pkl")

model = joblib.load(model_path)

st.title("🏦 Loan Default Prediction System")
st.write("Enter applicant details to predict loan approval")


gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["Yes", "No"])

dependents = st.selectbox("Dependents",[0, 1, 2, 3])

education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income")

coapplicant_income = st.number_input("Coapplicant Income")

loan_amount = st.number_input("Loan Amount")

loan_term = st.number_input("Loan Term (in months)")

credit_history = st.selectbox("Credit History", [1, 0])

property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

gender = 1 if gender == "Male" else 0

married = 1 if married == "Yes" else 0

education = 1 if education == "Graduate" else 0

self_employed = 1 if self_employed == "Yes" else 0

if property_area == "Urban":
    property_area = 2
elif property_area == "Semiurban":
    property_area = 1
else:
    property_area = 0

features = np.array([[
    gender,
    married,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    property_area
]])

if st.button("Predict Loan Status"):
    
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")