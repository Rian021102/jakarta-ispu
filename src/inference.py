import pandas as pd
import numpy as np
import pickle


df=pd.read_csv('/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/data/raw/df_openweather.csv')

#load model
model = pickle.load(open('/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/model/model.pkl','rb'))

print(df.head(),df.columns)

# Rename the nested columns with 'component.' prefix
df.rename(columns={
    'components.pm10': 'pm10',
    'components.so2': 'so2',
    'components.co': 'co',
    'components.o3': 'o3',
    'components.no2': 'no2'
}, inplace=True)

# Print the column names to verify the changes
print(df.columns)
dfpred=df[['pm10','so2','co','o3','no2']]
print(dfpred.head())
pred=model.predict(dfpred)
print(pred)
df['pred']=pred
df.to_csv('/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/data/processed/openweather_pred.csv',index=False)
