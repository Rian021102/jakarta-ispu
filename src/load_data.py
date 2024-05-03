import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def load_data(pathfile):
    df = pd.read_csv(pathfile)
    
    
    df_ISPU = df[['tanggal','stasiun','pm10', 'so2', 'co', 'o3', 'no2','categori']]
    # First, convert 'tanggal' to datetime
    df_ISPU['tanggal'] = pd.to_datetime(df['tanggal'])

    # Then, convert the columns to numeric, replacing invalid values with NaN
    df_ISPU['pm10'] = pd.to_numeric(df['pm10'], errors='coerce')
    df_ISPU['so2'] = pd.to_numeric(df['so2'], errors='coerce')
    df_ISPU['co'] = pd.to_numeric(df['co'], errors='coerce')
    df_ISPU['o3'] = pd.to_numeric(df['o3'], errors='coerce')
    df_ISPU['no2'] = pd.to_numeric(df['no2'], errors='coerce')
    
    
    #select where categori is BAIK to GOOD, SEDANG to FAIR, TIDAK SEHAT to MODERATE, SANGAT TIDAK SEHAT to POOR, BERBAHAYA to VERY POOR

    df_ISPU = df_ISPU[df_ISPU['categori'].isin(['SEDANG', 'BAIK', 'TIDAK SEHAT', 'SANGAT TIDAK SEHAT', 'BERBAHAYA'])]
    #df_ISPU['categori'] = df_ISPU['categori'].replace(['BAIK','SEDANG','TIDAK SEHAT','SANGAT TIDAK SEHAT','BERBAHAYA'],['GOOD','FAIR','MODERATE','POOR','VERY POOR'])

    print(df_ISPU.head())

    #rename SANGAT TIDAK SEHAT and BERBAHAYA to TIDAK SEHAT

    df_ISPU['categori'] = df_ISPU['categori'].replace(['SANGAT TIDAK SEHAT', 'BERBAHAYA'], 'TIDAK SEHAT')

    X=df_ISPU.drop(['categori'],axis=1)
    y=df_ISPU['categori']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
