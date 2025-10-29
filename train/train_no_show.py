import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load your real dataset for training
df = pd.read_csv('../data/appointments.csv')
features = ["age", "past_no_shows", "weekday", "lead_days", "has_reminder"]
target = "no_show"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Test accuracy: {accuracy:.3f}")

joblib.dump(model, '../app/models/no_show_model.pkl')
print("Model saved")
