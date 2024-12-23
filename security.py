# security.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

class Security:
    def __init__(self):
        pass

    def load_data(self, df):
        return df

    def prepare_features(self, df):
        X = df.drop(['Status'], axis=1)  # Assuming 'Status' is the target variable
        y = df['Status']  # Assuming 'Status' is the target variable
        return X, y

    def train_model(self, X, y):
        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def evaluate_model(self, X_test, y_test, X_new):
        self.model.predict(X_new)
        accuracy = accuracy_score(y_test, self.model.predict(X_test))
        return accuracy

# Usage:
df = pd.DataFrame({
    'Feature1': [1, 2, 3],
    'Feature2': [4, 5, 6],
    'Status': ['Normal', 'Under Maintenance', 'Failed']
})

a = Security()
X, y = a.prepare_features(df)
a.train_model(X, y)

# Then you can use your model to make predictions
def predict_status(self, X_new):
    return self.model.predict(X_new)

# Usage:
new_data = pd.DataFrame({
    'Feature1': [7],
    'Feature2': [8]
})
predicted_status = a.predict_status(new_data)
print(predicted_status)