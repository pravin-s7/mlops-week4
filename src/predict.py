import joblib
import pandas as pd

def load_model(model_path='model.pkl'):
    model, encoder = joblib.load(model_path)
    return model, encoder

def predict_species(input_data, model_path='model.pkl'):
    """
    Predict the species of iris flowers given input data.
    
    Parameters:
        input_data (list of lists): e.g., [[5.1, 3.5, 1.4, 0.2]]
        model_path (str): Path to saved model file
    
    Returns:
        List of predicted species names
    """
    model, encoder = load_model(model_path)
    df = pd.DataFrame(input_data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    preds = model.predict(df)
    return encoder.inverse_transform(preds)

if __name__ == "__main__":
    # Example usage
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = predict_species(sample)
    print(f"Predicted species: {prediction[0]}")