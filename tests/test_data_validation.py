import pandas as pd

def test_column_names():
    df = pd.read_csv("data/iris.csv")
    expected_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    assert list(df.columns) == expected_cols
