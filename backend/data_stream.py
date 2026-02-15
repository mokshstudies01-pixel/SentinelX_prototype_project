import pandas as pd
import random

# Load dataset
data = pd.read_csv("dataset/combined.csv", nrows=50000)
data.columns = data.columns.str.strip()

# Separate features and labels
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Attack rows (not BENIGN)
attack_indices = data[data.iloc[:, -1] != "BENIGN"].index
benign_indices = data[data.iloc[:, -1] == "BENIGN"].index

def get_next_row():

    # 70% chance attack, 30% benign
    if random.random() < 0.7:
        idx = random.choice(attack_indices)
    else:
        idx = random.choice(benign_indices)

    row = X.iloc[idx:idx+1]
    return row
