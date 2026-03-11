import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Top 10 products
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

# Top countries by revenue
top_countries = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)

# Plot settings
sns.set(style="whitegrid")

# Plot 1 — Top Products
plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Quantity Sold")
plt.ylabel("Quantity")
plt.xticks(rotation=75)
plt.show()

# Plot 2 — Revenue by Country
plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.title("Top Countries by Revenue")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

print("Visualization completed!")