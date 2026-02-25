import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "data/raw/yellow_tripdata_2015-01.csv")
output_path = os.path.join(BASE_DIR, "data/processed/sample_1.csv")

df = pd.read_csv(input_path, nrows=1000)
df.to_csv(output_path, index=False)

print("Sample extracted successfully.")