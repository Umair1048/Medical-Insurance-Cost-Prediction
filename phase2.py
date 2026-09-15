import pandas as pd

# Load dataset
df = pd.read_csv("D:\Downloads\Medical insurance")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())
print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())