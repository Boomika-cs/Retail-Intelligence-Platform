import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("data/raw/OnlineRetail.csv", encoding="latin1")

# Step 2: Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Step 3: Show dataset structure
print("\nDataset information:")
print(df.info())