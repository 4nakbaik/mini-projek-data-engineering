import pandas as pd
import os

input_path = "../data/raw/yellow_tripdata_2015-01.csv"
output_path = "../data/processed/sample_1.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError("Raw dataset not found.")

chunk_iter = pd.read_csv(input_path, chunksize=100000)

first_chunk = next(chunk_iter)
sample = first_chunk.head(1000)

sample.to_csv(output_path, index=False)

print("Sample extracted successfully.")