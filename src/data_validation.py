import pandas as pd

def validate_data(filepath):
    df = pd.read_csv(filepath)
    expected_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    return list(df.columns) == expected_columns