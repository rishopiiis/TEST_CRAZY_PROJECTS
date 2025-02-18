import pandas as pd
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

#pip install pandas numpy scikit-learn matplotlib

# Simulated daily schedule data
data = {
    "hour": list(range(24)),
    "activity": ["Sleep"]*6 + ["Exercise", "Work"]*8 + ["Relax", "Sleep"]
}

df = pd.DataFrame(data)
df["hour"] = df["hour"].astype(int)

X = df[["hour"]]
y = df["activity"]

model = RandomForestClassifier()
model.fit(X, y)

plt.figure(figsize=(5, 5))

while True:
    now = datetime.datetime.now()
    hour = np.array([[now.hour]])
    prediction = model.predict(hour)[0]

    plt.clf()
    plt.axis("off")
    plt.text(0.5, 0.5, prediction, ha="center", fontsize=20, color="blue")
    plt.pause(60)
