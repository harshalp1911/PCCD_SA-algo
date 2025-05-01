import pandas as pd

df = pd.read_excel("components.xlsx")  # Update path if needed
print(df.columns)
print(df.head())