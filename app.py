import streamlit as st
import pickle
import pandas as pd

# Load your trained model and the encoder
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the cleaned data to get options for select boxes
df = pd.read_csv('Cleaned_Data.csv')

# Streamlit UI components
st.title("Data Scientist Salary Prediction")

# User input fields
rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1)
classified_size = st.selectbox("Classified Size", options=["Small", "Medium", "Large", "Enterprise", "Very Large", "Micro"])
type_of_ownership = st.selectbox("Type of Ownership", options=df['Type of ownership'].value_counts().index)
industry = st.selectbox("Industry", options=df['Industry'].value_counts().index)
sector = st.selectbox("Sector", options=df['Sector'].value_counts().index)
revenue = st.number_input("Revenue Numeric", min_value=-1)

# New features: job_simp, Age_of_company, Num_Competitors
job_simp = st.selectbox("Job Simplification", options=df['job_simp'].value_counts().index)
age_of_company = st.number_input("Age of Company (Years)", min_value=0)
num_competitors = st.number_input("Number of Competitors", min_value=0)

# Binary feature inputs
hourly_pay = st.radio("Hourly Pay", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
employer_provided = st.radio("Employer Provided", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
python = st.radio("Python", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
scala = st.radio("Scala", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
java = st.radio("Java", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
sql = st.radio("SQL", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
tableau = st.radio("Tableau", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
powerbi = st.radio("Power BI", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
apache_spark = st.radio("Apache Spark", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
hadoop = st.radio("Hadoop", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
aws = st.radio("AWS", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
google_cloud = st.radio("Google Cloud", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
excel = st.radio("Excel", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
same_state = st.radio("Same State", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Button to predict
if st.button("Predict Salary"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'Rating': [rating],
        'Classified Size': [classified_size],
        'Type of ownership': [type_of_ownership],
        'Industry': [industry],
        'Sector': [sector],
        'Revenue': [revenue],
        'job_simp': [job_simp],
        'Hourly_Pay': [hourly_pay],
        'Employer_Provided': [employer_provided],
        'python': [python],
        'scala': [scala],
        'java': [java],
        'sql': [sql],
        'tableau': [tableau],
        'powerbi': [powerbi],
        'apache spark': [apache_spark],
        'hadoop': [hadoop],
        'aws': [aws],
        'google cloud': [google_cloud],
        'excel': [excel],
        'Same State': [same_state],
        'Age_of_company': [age_of_company],
        'Num_Competitors': [num_competitors]
    })

    # One-hot encode the categorical features
    input_data_encoded = pd.get_dummies(input_data, drop_first=True)

    # Align the input data with the model's expected input
    input_data_encoded = input_data_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    # Make prediction
    prediction = model.predict(input_data_encoded)
    st.success(f"Predicted Average Salary: ${prediction[0]:,.2f}")