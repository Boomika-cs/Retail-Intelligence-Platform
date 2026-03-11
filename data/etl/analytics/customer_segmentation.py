import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Customer level aggregation
customer_data = df.groupby("CustomerID").agg({
    "TotalPrice": "sum",
    "InvoiceNo": "count",
    "Quantity": "sum"
}).reset_index()

customer_data.columns = ["CustomerID","TotalSpending","TotalOrders","TotalItems"]

print(customer_data.head())

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_data[["TotalSpending","TotalOrders","TotalItems"]])

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
customer_data["Cluster"] = kmeans.fit_predict(scaled_features)

print("\nCustomer Segments:")
print(customer_data.head())

# Save result
customer_data.to_csv("data/customer_segments.csv", index=False)

print("\nCustomer segmentation completed!")