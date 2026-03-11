import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/OnlineRetail.csv", encoding="latin1")

print("Original dataset shape:", df.shape)

# Remove missing values
df = df.dropna()

# Remove negative quantities
df = df[df['Quantity'] > 0]

# Remove negative prices
df = df[df['UnitPrice'] > 0]

print("Cleaned dataset shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_retail.csv", index=False)

print("Cleaned dataset saved successfully!")