import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("D:/Downloads/Medical insurance/insurance.csv")

 
df = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True
)

 
df = df.astype(int)

X = df.drop("charges", axis=1)
y = df["charges"]

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:")
print(X_train.shape)

print("\nTesting data shape:")
print(X_test.shape)

 
model = LinearRegression()

# 6. Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 7. Make predictions
y_pred = model.predict(X_test)

print("\nSample Predictions:")
print(y_pred[:5])