import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("insurance.csv")

# Convert categorical columns into numerical columns
df = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True,
    dtype=int
)

X = df.drop("charges", axis=1)
y = df["charges"]

model = LinearRegression()
model.fit(X, y)



st.title("Medical Insurance Cost Prediction")

st.write("Enter the details below to estimate medical insurance cost.")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

sex = st.selectbox(
    "Gender",
    ["female", "male"]
)

smoker = st.selectbox(
    "Smoking Status",
    ["no", "yes"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)


if st.button("Predict Insurance Cost"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [1 if sex == "male" else 0],
        "smoker_yes": [1 if smoker == "yes" else 0],
        "region_northwest": [1 if region == "northwest" else 0],
        "region_southeast": [1 if region == "southeast" else 0],
        "region_southwest": [1 if region == "southwest" else 0]
    })

    
    input_data = input_data[X.columns]

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Insurance Cost: ${prediction[0]:,.2f}"
    )