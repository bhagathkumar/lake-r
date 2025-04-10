# generate_parquet.py

import pandas as pd
# Read the CSV
df = pd.read_csv("data/sample1.csv")
# Save as Parquet
df.to_parquet("data/sample1.parquet", index=False)

# Read the Parquet
df = pd.read_parquet("data/sample1.parquet")
# Print the first few rows
print(df.head())



