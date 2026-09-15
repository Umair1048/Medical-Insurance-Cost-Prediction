import pandas as pd

df = pd.read_csv("D:/Downloads/Medical insurance/insurance.csv")

print("Original Dataset:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)


print("\nData Types Before Preprocessing:")
print(df.dtypes)


print("\nCategorical Columns Before Encoding:")
print(df[["sex", "smoker", "region"]].head())


df = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True
)


d

# 8. Final dataset
print("\nDataset After Preprocessing:")
print(df.head())

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Column Names:")
print(df.columns)

print("\nFinal Data Types:")
print(df.dtypes)

# 9. Check missing values again
print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())