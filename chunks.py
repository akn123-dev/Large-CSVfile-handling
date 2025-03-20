# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 09:31:14 2025

@author: akhil.nair
"""

import os
import pandas as pd

# Input file path
csv_file = "CSV file path"  # Change this to your actual CSV file path

# Output folder (Updated to C:\Chunks-2)
output_folder = "output folder"
os.makedirs(output_folder, exist_ok=True)

# Approximate bytes per row (Adjust if needed)
sample_rows = pd.read_csv(csv_file, nrows=100, low_memory=False, dtype=str)  
bytes_per_row = sample_rows.memory_usage(index=True, deep=True).sum() / 100
target_size = 1 * 1024 * 1024 * 1024  # 1GB
rows_per_chunk = int(target_size / bytes_per_row)

# Read CSV in chunks and save them in the new folder
for i, chunk in enumerate(pd.read_csv(csv_file, chunksize=rows_per_chunk, dtype=str, low_memory=False)):
    chunk_file = os.path.join(output_folder, f"chunk_{i}.csv")
    chunk.to_csv(chunk_file, index=False)
    print(f"✅ Saved {chunk_file}")

print("✅ CSV Splitting Complete! Chunks saved")
