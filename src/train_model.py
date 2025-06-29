import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model(csv_path='data/iris.csv', model_path='model.pkl'):
    # Load dataset
    df = pd.read_csv(csv_path)

    # Feature and label separation
    X = df.drop('species', axis=1)
    y = df['species']

    # Encode labels (setosa = 0, versicolor = 1, virginica = 2)
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X, y_encoded)

    # Save the model and encoder
    joblib.dump((model, encoder), model_path)
    print(f"Model and encoder saved to {model_path}")

if __name__ == '__main__':
    train_and_save_model()
