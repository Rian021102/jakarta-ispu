import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle

def train_model(X_train, y_train, X_test, y_test):
    # Train model using random forest classifier
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)

    # Predict using model
    y_pred = model.predict(X_test)

    # Print accuracy score and classification report
    print('Accuracy score: ', accuracy_score(y_test, y_pred))
    print('Classification report: \n', classification_report(y_test, y_pred))

    # Save model as pickle file
    filename = 'model.pkl'
    pickle.dump(model, open(filename, 'wb'))

    return {'accuracy_score': accuracy_score,
            'classification_report': classification_report,
            'model': model}