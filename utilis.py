import joblib
import numpy as np
import pandas as pd
import test
import random


def preprocess(variables):
    imp_variables = [variables[0], variables[1], variables[2], variables[3]]

    other_variables = test.test_dumy

    # row manipulation
    #rows_id = random.sample(range(0, other_variables.shape[1] - 1), 1)

    # display random rows
    #rows = other_variables[rows_id, :]

    all_variables = [imp_variables + other_variables]

    # using standardscaler for transformation
    scaler = joblib.load('scaler.pkl')
    X_scaler = scaler.transform(all_variables)

    # using saved model
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(X_scaler)

    return prediction
