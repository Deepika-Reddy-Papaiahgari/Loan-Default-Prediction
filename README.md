Loan Default Prediction (Jupyter Notebook Project):

This project uses Machine Learning to predict whether a loan application will be approved or rejected based on applicant details.

The entire workflow is implemented in a Jupyter Notebook, including data preprocessing, model training, and evaluation.


Project Overview:

The goal of this project is to build a classification model that predicts loan approval using historical loan application data.

The model learns patterns from features like income, credit history, education, and property area.


Machine Learning Model:

Algorithm: Random Forest Classifier
Framework: Scikit-learn
Type: Binary Classification
Target Variable: Loan_Status (Y/N)


Dataset Description:

The dataset contains applicant information such as:

Feature	Description:
Gender:	Male / Female
Married: Marital status
Dependents:	Number of dependents
Education:	Graduate / Not Graduate
Self_Employed: Employment status
ApplicantIncome: Applicant salary
CoapplicantIncome: Co-applicant salary
LoanAmount:	Loan amount requested
Loan_Amount_Term: Loan duration
Credit_History: Past credit record
Property_Area: Urban / Semiurban / Rural
Loan_Status: Target variable (Y/N)


Workflow:

1. Data Loading
Load dataset using Pandas
2. Data Cleaning
Handle missing values
Fix categorical inconsistencies (e.g., "3+" in Dependents)
3. Feature Engineering
Convert categorical variables into numeric form
4. Model Training
Train Random Forest Classifier
Split data into training and testing sets
5. Model Evaluation
Accuracy score
Classification report
6. Model Saving
Save trained model using joblib


Data Preprocessing Steps:

Filled missing values
Converted categorical variables:
Male → 1, Female → 0
Yes → 1, No → 0
Graduate → 1, Not Graduate → 0
Urban → 2, Semiurban → 1, Rural → 0
Converted 3+ dependents to numeric value

Model Training

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)


Evaluation Metrics
Accuracy Score
Precision / Recall

Save Model:

import joblib
joblib.dump(model, "models/loan_model.pkl")

Sample Prediction

sample = [[
    1, 1, 2, 1, 0,
    5000, 2000, 150,
    360, 1, 2
]]

model.predict(sample)


Tools & Libraries:
Python 
Pandas
NumPy
Scikit-learn
Jupyter Notebook
Joblib

Key Learnings:

Data preprocessing is critical for ML success
Handling missing values properly prevents training errors
Feature consistency is required for correct predictions
Model saving allows reuse in deployment applications

Streamlit Web Application

A web-based interface is built using Streamlit to interact with the trained ML model.

Run Locally

```bash
streamlit run app.py


Author:
Deepika Reddy Papaiahgari
