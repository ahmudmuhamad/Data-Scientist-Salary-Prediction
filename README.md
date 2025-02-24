# Data Scientist Salary Prediction

## Introduction

The **Data Scientist Salary Prediction** application provides an interactive user interface built with Streamlit. Users can input specific characteristics and receive a predicted average salary based on their inputs. This model employs multiple machine learning algorithms trained on data scraped from Glassdoor.

## Data

The dataset is sourced from Glassdoor and includes the following columns:

- **Job Title**
- **Salary Estimate**
- **Job Description**
- **Rating**
- **Company Name**
- **Location**
- **Headquarters**
- **Size**
- **Founded**
- **Type of Ownership**
- **Industry**
- **Sector**
- **Revenue**
- **Competitors**

After preprocessing, the following columns are extracted:

- **job_simp**: Simplified job title (e.g., "Data Scientist", "Data Engineer").
- **Hourly_Pay**: Indicates if the salary is hourly.
- **Employer_Provided**: Indicates if the salary was provided by the employer.
- **Maximum Salary**: The maximum salary.
- **Minimum Salary**: The minimum salary.
- **Average Salary**: The average salary.
- **Skills and Qualifications**: Binary indicators for whether the job description mentions specific skills or technologies (e.g., Python, Scala, Java, SQL, etc.).
- **Extracted Skills**: A list of skills extracted from the job description.
- **Educational Requirements**: The minimum educational requirements specified in the job description.
- **Company Information**:
  - **Company**: The name of the company.
  - **State**: The state where the job is located.
  - **Same State**: Indicates if the job location matches the company's headquarters.
  - **Classified Size**: The classified size of the company (e.g., "Small", "Medium", "Large").
  - **Age of Company**: The age of the company.
  - **Num Competitors**: The number of competitors listed in the job description.
  - **Revenue Numeric**: The company's revenue, converted to a numerical value.

These columns provide a comprehensive dataset for analyzing factors influencing data science salaries and for building a predictive model.

## Machine Learning Models

This project implements several regression models to predict salaries:

1. **Linear Regression**
   - A basic regression model that establishes a relationship between the input features and the salary.

2. **Lasso Regression**
   - Utilizes L1 regularization to prevent overfitting and enhance model interpretability.
   - **Grid Search Parameters**:
     - `param_grid`: A set of hyperparameters to optimize, including the regularization strength.

3. **Ridge Regression**
   - Employs L2 regularization to handle multicollinearity and improve model performance.
   - **Grid Search Parameters**:
     - `alpha`: Various values for the regularization strength (`[0.01, 0.1, 1, 10, 100]`).

4. **Random Forest Regressor**
   - An ensemble model that enhances prediction accuracy by averaging multiple decision trees.
   - **Grid Search Parameters**:
     - `n_estimators`: Number of trees in the forest (`[50, 100]`).
     - `max_features`: The number of features to consider when looking for the best split (`['auto', 'sqrt']`).
     - `max_depth`: Maximum depth of the tree (`[None, 10, 20, 30]`).
     - `min_samples_split`: Minimum number of samples required to split an internal node (`[2, 5, 10]`).
     - `min_samples_leaf`: Minimum number of samples required to be at a leaf node (`[1, 2, 4]`).

## Model Deployment Using Streamlit

The final step involved deploying the selected machine learning model using a Streamlit application. This interactive web app allows users to input parameters and receive real-time predictions.

## Conclusion

This project successfully developed a machine learning model capable of predicting data scientist salaries based on various input features. The model serves as a valuable tool for job seekers and employers to understand salary trends and make informed decisions.
