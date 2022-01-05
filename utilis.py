import joblib
import numpy as np
import pandas as pd
import test
from sklearn.preprocessing import StandardScaler


def preprocess(variables):
    imp_variables = [variables[0], variables[1], variables[2], variables[3]]
    other_variables = test.test
    all_variables = [imp_variables + other_variables]

    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(all_variables)

    return prediction
