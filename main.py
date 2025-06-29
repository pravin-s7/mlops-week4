from src.train_model import train_and_save_model
from src.predict import predict_species

def main():
    print("Training model...")
    train_and_save_model('data/iris.csv', 'model.pkl')
    
    print("Training complete. Now predicting sample input...")
    sample = [[5.1, 3.5, 1.4, 0.2]] 
    prediction = predict_species(sample, 'model.pkl')
    
    print(f"Predicted species: {prediction[0]}")

if __name__ == "__main__":
    main()
