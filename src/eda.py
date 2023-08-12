import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def eda (X_train, y_train, X_test, y_test):
    #filter all numeric columns
    print(X_train.shape)
    print(y_train.shape)

    print(X_train.describe())

    #Check missing values in X_train, X_test, y_train, y_test
    print('Missing values in X_train: ', X_train.isnull().sum().sum())
    print('Missing values in X_test: ', X_test.isnull().sum().sum())
    print('Missing values in y_train: ', y_train.isnull().sum().sum())
    print('Missing values in y_test: ', y_test.isnull().sum().sum())
   #fill missing values in X_train and X_test with 0
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)

    #reset index X_train and X_test
    X_train = X_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)

    X_train_numeric = X_train.select_dtypes(include=[np.number])
    

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

#plot box plot for X_train
    for i in X_train_numeric.columns:
        plt.figure(figsize=(10,5))
        plt.boxplot(X_train_numeric[i])
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