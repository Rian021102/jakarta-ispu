import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import imputer
from sklearn.impute import SimpleImputer


def eda (X_train, y_train, X_test, y_test):
    
    print(X_train.shape)
    print(y_train.shape)

    print(X_train.describe())

    #print X_train, X_test, y_train, y_test data types
    print('X_train data types: ', X_train.dtypes)
    print('X_test data types: ', X_test.dtypes)
    print('y_train data types: ', y_train.dtypes)
    print('y_test data types: ', y_test.dtypes)

    #Check missing values in X_train, X_test, y_train, y_test
    print('Missing values in X_train: ', X_train.isnull().sum().sum())
    print('Missing values in X_test: ', X_test.isnull().sum().sum())
    print('Missing values in y_train: ', y_train.isnull().sum().sum())
    print('Missing values in y_test: ', y_test.isnull().sum().sum())

    #check all the columns in X_train and X_test with missing values
    print('Columns in X_train with missing values: ', X_train.columns[X_train.isnull().any()])
    print('Columns in X_test with missing values: ', X_test.columns[X_test.isnull().any()])


    #select all column with numeric data type
    X_train_numeric = X_train.select_dtypes(include=np.number)
    

    plt.figure(figsize=(30,30))
    for i, col in enumerate(X_train_numeric.columns):
        plt.subplot(5,5,i+1)
        plt.hist(X_train_numeric[col])
        plt.title(col)  
    plt.show()  

    X_grouped = X_train.groupby('tanggal')[['pm10', 'co', 'o3', 'no2', 'so2']].mean().reset_index()
    print(X_grouped.head())

#plot all the features from X_grouped with for
    for i in X_grouped.columns[1:]:
        plt.figure(figsize=(30,5))
        plt.plot(X_grouped['tanggal'], X_grouped[i])
        plt.title(i)
    plt.show()


    #concat x_train and y_train
    df_train = pd.concat([X_train, y_train], axis=1)

    sns.countplot(x='categori',data=df_train)

    #plot heatmap correlation from df_train
    plt.figure(figsize=(10,10))
    sns.heatmap(df_train.corr(),annot=True,fmt='.2f',cmap='coolwarm')
    plt.show()


    return X_train, y_train, X_test, y_test