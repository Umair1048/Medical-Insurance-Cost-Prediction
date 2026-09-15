# Medical Insurance Cost Prediction

## Project Overview

This project predicts medical insurance costs using Machine Learning.

The application allows a user to enter personal information such as age, BMI, number of children, gender, smoking status, and region. A Linear Regression model then predicts the estimated medical insurance cost.

## Problem Statement

Medical insurance costs vary depending on several factors such as age, BMI, smoking status, number of children, gender, and geographical region.

The goal of this project is to build a machine learning model that can estimate medical insurance charges based on these features.

## Dataset

The project uses the Medical Cost Personal Dataset.

The dataset contains the following columns:

- age
- sex
- bmi
- children
- smoker
- region
- charges

The target variable is `charges`.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Linear Regression
- GitHub

## Data Preprocessing

The following preprocessing steps were performed:

1. Checked for missing values.
2. Checked for duplicate records.
3. Examined data types.
4. Converted categorical variables into numerical variables using one-hot encoding.
5. Separated features from the target variable.

Categorical variables included:

- sex
- smoker
- region

## Exploratory Data Analysis

The relationships between insurance charges and important features were analyzed.

Visualizations included:

- Age vs Insurance Charges
- BMI vs Insurance Charges
- Average Insurance Charges by Smoking Status

The analysis showed that smoking status has a strong relationship with insurance charges, while age and BMI also show relationships with the target variable.

## Machine Learning Model

Multiple Linear Regression was used to predict insurance charges.

The dataset was divided into:

- 80% training data
- 20% testing data

The model was trained using the training dataset and then used to make predictions on the test dataset.

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

These metrics were used to measure how accurately the model predicts insurance charges.

## Prediction Application

A Streamlit web application was created where users can enter:

- Age
- BMI
- Number of children
- Gender
- Smoking status
- Region

The application then displays the estimated medical insurance cost.

## Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── app1.py
├── insurance.csv
├── requirements.txt
├── README.md
├── phase2.py
├── phase3.py
├── phase4.py
├── phase5.py
└── phase6.py
