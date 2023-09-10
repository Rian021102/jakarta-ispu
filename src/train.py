import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle

def train_model(X_train,X_test,y_train,y_test):
    # Train model using random forest classifier
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)

    # Predict using model
    y_pred = model.predict(X_test)

    # Print accuracy score and classification report
    print('Accuracy score: ', accuracy_score(y_test, y_pred))
    print('Classification report: \n', classification_report(y_test, y_pred))

    # Save model as pickle file
    with open('/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/model/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    

    return {'accuracy_score': accuracy_score,
            'classification_report': classification_report,
            'model': model}