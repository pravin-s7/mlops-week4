from sklearn.metrics import accuracy_score
import numpy as np

def test_accuracy_metric():
    y_true = np.array([0, 1, 2])
    y_pred = np.array([0, 1, 2])
    assert accuracy_score(y_true, y_pred) == 1.0
