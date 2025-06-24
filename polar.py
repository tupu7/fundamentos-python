import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/evareladev/evareladev.github.io/refs/heads/main/src/Dataset_ventas_v1.0.csv")

print(df.head())

print(df["nearest_warehouse"])

print(df.info())

df["date"] = pd.to_datetime(df["date"], format = "mixed")
print(df.info())

print(df["nearest_warehouse"].unique())

valores_corregidos = {"nickolson": "Nickolson", "thompson": "Thompson"}
df["nearest_warehouse"] = df["nearest_warehouse"].replace(valores_corregidos)

print(df["nearest_warehouse"].unique())

#df ["nearest_warehouse"] = df[]"neareswearhouse"].astype
deleted_columns = ["shopping_cart", "latest_customer_review"]
df = df.drop(deleted_columns, axis = 1)