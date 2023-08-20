import pandas as pd
import numpy as np
#import logistic regression
from sklearn.linear_model import LogisticRegression
#import ensemble
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
#import xgboost
from xgboost import XGBClassifier
#import cross validation
from sklearn.model_selection import cross_val_score
#import accuracy score
from sklearn.metrics import accuracy_score
#import classification report
from sklearn.metrics import classification_report

#make baseline model using logistic regression
def model_baseline(X_train,X_test,y_train,y_test):
    #make model
    lr = LogisticRegression()
    #fit model
    lr.fit(X_train,y_train)
    #predict
    y_pred = lr.predict(X_test)
    #accuracy score
    acc = accuracy_score(y_test,y_pred)
    #classification report
    cr = classification_report(y_test,y_pred)
    #cross validation
    cv = cross_val_score(lr,X_train,y_train,cv=5)
    print('Logistic Regression')
    print('Accuracy Score:',acc)
    print('Classification Report:',cr)
    print('Cross Validation:',cv)
    return lr

#train all models
def model_exp(X_train,X_test,y_train,y_test):
    models=['random forest',RandomForestClassifier(),'gradient boosting',GradientBoostingClassifier(),
            'xgboost',XGBClassifier()]
    for i in range(0,len(models),2):
        model = models[i+1]
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test,y_pred)
        cr = classification_report(y_test,y_pred)
        cv = cross_val_score(model,X_train,y_train,cv=5)
        print(models[i])
        print('Accuracy Score:',acc)
        print('Classification Report:',cr)
        print('Cross Validation:',cv)
        print('--------------------------------------------------')
  

