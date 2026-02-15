import pandas as pd
import glob

# Find all CSV files in dataset folder
files = glob.glob("dataset/*.csv")

# Read and combine all files
df_list = []
for file in files:
    print("Loading:", file)
    temp = pd.read_csv(file)
    df_list.append(temp)

# Merge all files
data = pd.concat(df_list, ignore_index=True)

# Save combined dataset
data.to_csv("dataset/combined.csv", index=False)

print("\nAll files combined successfully!")
print("Total rows:", len(data))
