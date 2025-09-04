import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("Original Data:")
print(df)

# Drop rows where 'Name' is missing (essential field)
df = df.dropna(subset=["Name"])

# Fill missing ages with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing marks with 0
df["Marks"] = df["Marks"].fillna(0)

print("\nCleaned Data:")
print(df)

# Export cleaned data
df.to_csv("students_cleaned.csv", index=False)
