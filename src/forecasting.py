#import all needed library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import StandardScaler

def load_data(pathfile):
    df = pd.read_csv(pathfile)
    df_ISPU = df[['tanggal', 'stasiun', 'pm10', 'so2', 'co', 'o3', 'no2','categori']]
    # Assuming 'df' is your original DataFrame

    # First, convert 'tanggal' to datetime
    df_ISPU['tanggal'] = pd.to_datetime(df['tanggal'])

    # Then, convert the columns to numeric, replacing invalid values with NaN
    df_ISPU['pm10'] = pd.to_numeric(df['pm10'], errors='coerce')
    df_ISPU['so2'] = pd.to_numeric(df['so2'], errors='coerce')
    df_ISPU['co'] = pd.to_numeric(df['co'], errors='coerce')
    df_ISPU['o3'] = pd.to_numeric(df['o3'], errors='coerce')
    df_ISPU['no2'] = pd.to_numeric(df['no2'], errors='coerce')
    
    
    #select where categori is SEDANG, BAIK, TIDAK SEHAT, SANGAT TIDAK SEHAT, BERBAHAYA

    df_ISPU = df_ISPU[df_ISPU['categori'].isin(['SEDANG', 'BAIK', 'TIDAK SEHAT', 'SANGAT TIDAK SEHAT', 'BERBAHAYA'])]

    print(df_ISPU.head())

    #rename SANGAT TIDAK SEHAT and BERBAHAYA to TIDAK SEHAT

    df_ISPU['categori'] = df_ISPU['categori'].replace(['SANGAT TIDAK SEHAT', 'BERBAHAYA'], 'TIDAK SEHAT')
    return df_ISPU

filepath='/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/data/raw/merged_data.csv'
df_ispu=load_data(filepath)

def data_checking(df_ispu):
    print(df_ispu.shape)
    print(df_ispu.info())
    print(df_ispu.describe())
    print(df_ispu.isnull().sum())
    
    #plot boxplot
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(data=df_ispu, x='pm10', ax=axes[0])
    sns.boxplot(data=df_ispu, x='so2', ax=axes[0])
    sns.boxplot(data=df_ispu, x='co', ax=axes[1])
    sns.boxplot(data=df_ispu, x='o3', ax=axes[0])
    sns.boxplot(data=df_ispu, x='no2', ax=axes[1])
    plt.show()

    return df_ispu
data_checking(df_ispu)

def eda(df_ispu):
    #fill mising values of stasiun with "unknown"
    df_ispu['stasiun'].fillna('unknown', inplace=True)
    

    #impute all numerical columns with mean
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp_mean.fit(df_ispu[['pm10', 'so2', 'co', 'o3', 'no2']])
    df_ispu[['pm10', 'so2', 'co', 'o3', 'no2']] = imp_mean.transform(df_ispu[['pm10', 'so2', 'co', 'o3', 'no2']])

    #remove outlier using IsolationForest
    clf = IsolationForest(random_state=0, contamination=0.25)
    clf.fit(df_ispu[['pm10', 'so2', 'co', 'o3', 'no2']])
    outlier_label = clf.predict(df_ispu[['pm10', 'so2', 'co', 'o3', 'no2']])
    df_ispu['outlier_label'] = outlier_label
    df_ispu = df_ispu[df_ispu['outlier_label'] != -1]
    df_ispu.drop('outlier_label', axis=1, inplace=True)
    

    return df_ispu
eda(df_ispu)

def featuring(df_ispu):
    # group by date and aggregate by mean
    df_grouped = df_ispu.groupby('tanggal')[['pm10', 'so2', 'co', 'o3', 'no2']].mean().reset_index()
    print(df_grouped.head())

    #cap max value of each feature to 75th percentile
    #create a function to cap max value
    def cap_max_value(df, col, cap):
        df[col] = np.where(df[col] > cap, cap, df[col])
        return df
    
    #plot time series for all features into 5 subplots
    fig, axes = plt.subplots(5, 1, figsize=(15, 15))
    axes[0].plot(df_grouped['tanggal'], df_grouped['pm10'])
    axes[0].set_title('pm10')
    axes[1].plot(df_grouped['tanggal'], df_grouped['so2'])
    axes[1].set_title('so2')
    axes[2].plot(df_grouped['tanggal'], df_grouped['co'])
    axes[2].set_title('co')
    axes[3].plot(df_grouped['tanggal'], df_grouped['o3'])
    axes[3].set_title('o3')
    axes[4].plot(df_grouped['tanggal'], df_grouped['no2'])
    axes[4].set_title('no2')
    plt.tight_layout()
    plt.show()
    print("last date:", df_grouped.tail())
    return df_grouped
df_grouped=featuring(df_ispu)

def makenewdf(df_grouped):
    df_pm10 = df_grouped[['tanggal', 'pm10']]
    df_so2 = df_grouped[['tanggal', 'so2']]
    df_co = df_grouped[['tanggal', 'co']]
    df_o3 = df_grouped[['tanggal', 'o3']]
    df_no2 = df_grouped[['tanggal', 'no2']]
    #print head using for
    for i in [df_pm10, df_so2, df_co, df_o3, df_no2]:
        print(i.head())
    return df_pm10, df_so2, df_co, df_o3, df_no2
df_pm10, df_so2, df_co, df_o3, df_no2=makenewdf(df_grouped)



def forecast_pollutant(df, pollutant_column, order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30):
    # Train the SARIMAX model
    sarima = SARIMAX(df[pollutant_column],
                    order=order,
                    seasonal_order=seasonal_order)
    sarima_fit = sarima.fit()

    # Get the predictions from the trained model
    predictions = sarima_fit.predict()

    # Forecast the next `forecast_steps` days based on the predictions
    forecast_values = sarima_fit.get_forecast(steps=forecast_steps).predicted_mean

    # Create a DataFrame for the forecasted data (only index, no date)
    forecast_df = pd.DataFrame({
        f'Forecasted_{pollutant_column}': forecast_values
    })

    # Display the forecast DataFrame
    print(f"Forecasted {pollutant_column} Data:")
    print(forecast_df)

    # Plot the original data, predicted data, and forecasted data in one plot
    plt.figure(figsize=(10, 6))
    plt.plot(df[pollutant_column], label='Original Data', color='blue')
    plt.plot(predictions, label='Predicted Data', color='green')
    plt.plot(list(range(len(df), len(df) + len(forecast_values))), forecast_values, label='Forecasted Data', color='orange')
    plt.title(f'{pollutant_column} Forecasting')
    plt.xlabel('Index')
    plt.ylabel(pollutant_column)
    plt.legend()
    plt.show()

# Example usage
# Replace df_pm10 with your actual DataFrame and 'pm10' with the respective pollutant column name
# You can also adjust the order and seasonal_order as needed
forecast_pollutant(df_pm10, 'pm10', order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30)
forecast_pollutant(df_so2, 'so2', order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30)
forecast_pollutant(df_co, 'co', order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30)
forecast_pollutant(df_o3, 'o3', order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30)
forecast_pollutant(df_no2, 'no2', order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30)



