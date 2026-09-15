import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Downloads/Medical insurance/insurance.csv")


plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["charges"])
plt.xlabel("Age")
plt.ylabel("Insurance Charges")
plt.title("Age vs Insurance Charges")
plt.show()


 
plt.figure(figsize=(8, 5))
plt.scatter(df["bmi"], df["charges"])
plt.xlabel("BMI")
plt.ylabel("Insurance Charges")
plt.title("BMI vs Insurance Charges")
plt.show()



average_charges = df.groupby("smoker")["charges"].mean()

plt.figure(figsize=(7, 5))
average_charges.plot(kind="bar")
plt.xlabel("Smoking Status")
plt.ylabel("Average Insurance Charges")
plt.title("Average Insurance Charges by Smoking Status")
plt.xticks(rotation=0)
plt.show()

 
 
df_encoded = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True
)

df_encoded = df_encoded.astype(int)

print("\nCorrelation Matrix:")
print(df_encoded.corr())

print("\nCorrelation with Insurance Charges:")
print(df_encoded.corr()["charges"].sort_values(ascending=False))