# Data Scientist Salary Prediction

This project aims to predict the average salary of data scientists based on various input features.


## Introduction

The Data Scientist Salary Prediction application provides an interactive user interface using Streamlit, allowing users to input specific characteristics and receive a predicted average salary. This model leverages multiple machine learning algorithms trained on data scrapped from glassdoor.



## Data
The data is scrapped from glassdoor and it's columns are: 
"Job Title",
"Salary Estimate",
'Job Description', 
'Rating',
'Company Name', 
'Location', 
'Headquarters', 
'Size', 
'Founded',       
'Type of ownership', 
'Industry',
'Sector', 
'Revenue', 
'Competitors'




After preprocessing, The following columns are extracted:

job_simp: Simplified job title (e.g., "Data Scientist", "Data Engineer").

Hourly_Pay: Indicates if the salary is hourly.
Employer_Provided: Indicates if the salary was provided by the employer.

Maximum Salary: The maximum salary.

Minimum Salary: The minimum salary.

Average Salary: The average salary.

Skills and Qualifications:
(python, scala, java, sql, scikit-learn, tensorflow, keras, matplotlib, tableau, powerbi, plotly, d3.js, apache spark, hadoop, aws, google cloud, pandas, numpy, excel)
Binary indicators for whether the job description mentions the corresponding skills or technologies.

Extracted Skills: A list of skills extracted from the job description.

Educational Requirements: The minimum educational requirements specified in the job description.

Company Information:
Company: The name of the company.
State: The state where the job is located.
Same State: Indicates if the job location matches the company's headquarters.
Classified Size: The classified size of the company (e.g., "Small", "Medium", "Large").
Age_of_company: The age of the company.
Num_Competitors: The number of competitors listed in the job description.
Revenue Numeric: The company's revenue, converted to a numerical value.

These columns provide a comprehensive dataset for analyzing factors that influence data science salaries and building a predictive model.
       	


## Machine Learning Models

This project implements several regression models to predict salaries:

1. **Linear Regression**
   - A basic regression model that establishes a relationship between the input features and the salary.

2. **Lasso Regression**
   - Uses L1 regularization to prevent overfitting and enhance model interpretability.
   - **Grid Search Parameters**:
     - `param_grid`: A set of hyperparameters to optimize, including the regularization strength.

3. **Ridge Regression**
   - Uses L2 regularization to handle multicollinearity and improve model performance.
   - **Grid Search Parameters**:
     - `alpha`: Different values for the regularization strength (`[0.01, 0.1, 1, 10, 100]`).

4. **Random Forest Regressor**
   - An ensemble model that improves prediction accuracy by averaging multiple decision trees.
   - **Grid Search Parameters**:
     - `n_estimators`: Number of trees in the forest (`[50, 100]`).
     - `max_features`: The number of features to consider when looking for the best split (`['auto', 'sqrt']`).
     - `max_depth`: Maximum depth of the tree (`[None, 10, 20, 30]`).
     - `min_samples_split`: Minimum number of samples required to split an internal node (`[2, 5, 10]`).
     - `min_samples_leaf`: Minimum number of samples required to be at a leaf node (`[1, 2, 4]`).



## Model Deployment Using Streamlit:
The final step involved deploying the selected machine learning model using a Streamlit application. This interactive web app allows users to input launch parameters and receive real-time predictions

## Conclusion

This project successfully developed a machine learning model capable of predicting data scientist salaries based on various input features. The model can be used as a valuable tool for job seekers and employers to understand salary trends and make informed decisions.
