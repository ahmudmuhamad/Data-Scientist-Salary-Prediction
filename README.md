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
  - **State**: The state
