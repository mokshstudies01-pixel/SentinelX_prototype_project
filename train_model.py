import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

print("Loading dataset...")

data = pd.read_csv("dataset/combined.csv")
data.columns = data.columns.str.strip()

data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.dropna(inplace=True)

print("Total rows:", len(data))

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Show mapping (IMPORTANT)
print("\nAttack Label Mapping:")
for i, label in enumerate(le.classes_):
    print(i, "=", label)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

print("\nTraining model...")

model = RandomForestClassifier(
    n_estimators=50,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nModel Performance:\n")
print(classification_report(y_test, predictions))



import joblib

# Save model and label encoder
joblib.dump(model, "model/threat_model.pkl")
joblib.dump(le, "model/label_encoder.pkl")

print("\nModel saved successfully!")
