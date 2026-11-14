import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())
print(df.describe)
print("\nOriginal Dataset Shape",df.shape)
df=df.drop_duplicates()
print(df.isna().sum())
df=df.drop_duplicates()
df.columns=df.columns.str.strip().str.lower()
print("Available Column:",df.columns.tolist())

 #Quantity Analysis

print("\n===== QUANTITY ANALYSIS =====")

print("Total Quantity Sold:", df["quantity"].sum())
print("Average Quantity:", df["quantity"].mean())
print("Maximum Quantity:", df["quantity"].max())
print("Minimum Quantity:", df["quantity"].min())

print("\nStatistical Summary:")
print(df.describe())
print("\n===== PRODUCT ANALYSIS =====")

product_sales = df.groupby("product")["quantity"].sum()

print(product_sales)

print("\nBest Selling Product:")
print(product_sales.idxmax())
print("\n===== CITY ANALYSIS =====")

city_sales = df.groupby("city")["quantity"].sum()

print(city_sales)
# PRODUCT-WISE SALES GRAPH

import matplotlib.pyplot as plt
import pandas as pd

df["quantity"] = pd.to_numeric(
    df["quantity"], errors="coerce"
)

product_sales = df.groupby("product")["quantity"].sum()

plt.figure(figsize=(10, 5))
plt.bar(product_sales.index, product_sales.values)

plt.title("Product-wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

