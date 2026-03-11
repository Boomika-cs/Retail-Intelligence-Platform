import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Total revenue
total_revenue = df["TotalPrice"].sum()

# Top 10 products
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

# Top countries
top_countries = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)

print("Total Revenue:", total_revenue)

print("\nTop Products:")
print(top_products)

print("\nTop Countries:")
print(top_countries)