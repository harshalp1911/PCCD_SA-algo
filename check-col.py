# check-col.py
import pandas as pd

df = pd.read_excel("components.xlsx")
print("Columns in components.xlsx:")
print(df.columns.tolist())
print("\nSample data:")
print(df.head())
