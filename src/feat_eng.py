import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer

def feature_eng(X_train, X_test, y_train, y_test):
    print("Before feature engineering:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)
    print(y_train.isnull().sum())
    print(y_test.isnull().sum())

    # Drop columns 'tanggal' and 'stasiun' from X_train
    X_train.drop(['tanggal','stasiun'], axis=1, inplace=True)
    X_test.drop(['tanggal','stasiun'], axis=1, inplace=True)

    # Impute missing values on X_train and X_test
    imputer = SimpleImputer(strategy='mean')
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)

    # Removing outliers on X_train using Isolation Forest
    clf = IsolationForest(random_state=42, contamination=0.15)
    clf.fit(X_train)
    y_pred_train = clf.predict(X_train)
    mask = y_pred_train != -1
    X_train = X_train[mask]
    y_train = y_train[mask]

    # Label encoding on y_train and y_test
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)

    print("After feature engineering:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    return X_train, X_test, y_train, y_test

