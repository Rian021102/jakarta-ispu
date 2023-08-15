import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

def main():
    st.title('Pollutant Forecasting Streamlit App')
    st.subheader('Forecasting Pollutant in Jakarta')
    filepath = '/data/processed/df_processed.csv'

    def load_data(pathfile):
        df_ISPU = pd.read_csv(pathfile)   
        return df_ISPU
    df_ISPU = load_data(filepath)

    def makenewdf(df_ISPU):
        df_pm10 = df_ISPU[['tanggal', 'pm10']]
        df_so2 = df_ISPU[['tanggal', 'so2']]
        df_co = df_ISPU[['tanggal', 'co']]
        df_o3 = df_ISPU[['tanggal', 'o3']]
        df_no2 = df_ISPU[['tanggal', 'no2']]
        return df_pm10, df_so2, df_co, df_o3, df_no2
    
    df_pm10, df_so2, df_co, df_o3, df_no2 = makenewdf(df_ISPU)

    def forecast_pollutant(df, pollutant_column, order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), forecast_steps=30):
        sarima = SARIMAX(df[pollutant_column], order=order, seasonal_order=seasonal_order)
        sarima_fit = sarima.fit(disp=False)  # Set disp=False to suppress fitting result output

        predictions = sarima_fit.get_prediction(start=-forecast_steps)
        forecast_values = predictions.predicted_mean

        forecast_df = pd.DataFrame({f'Forecasted_{pollutant_column}': forecast_values})
        st.subheader(f'Forecasted {pollutant_column} Data:')
        st.write(forecast_df)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df[pollutant_column], label='Original Data', color='blue')
        ax.plot(predictions.predicted_mean, label='Predicted Data', color='green')
        ax.plot(predictions.conf_int(), color='gray', alpha=0.2)
        ax.set_title(f'{pollutant_column} Forecasting')
        ax.set_xlabel('Index')
        ax.set_ylabel(pollutant_column)
        ax.legend()
        st.pyplot(fig)  # Show the plot using Streamlit

    st.write('## Pollutant Forecasting')
    forecast_days = st.number_input('Number of Days to Forecast', value=30, min_value=1, max_value=365)
    if st.button('Forecast'):
        forecast_pollutant(df_pm10, 'pm10', forecast_steps=forecast_days)
        forecast_pollutant(df_so2, 'so2', forecast_steps=forecast_days)
        forecast_pollutant(df_co, 'co', forecast_steps=forecast_days)
        forecast_pollutant(df_o3, 'o3', forecast_steps=forecast_days)
        forecast_pollutant(df_no2, 'no2', forecast_steps=forecast_days)

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning
    main()
