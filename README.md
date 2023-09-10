# Prologue
In the past few days, both news outlets and social media platforms have been consistently reporting the deteriorating air quality in Jakarta. Headlines such as "Jakarta: The Most Populated City" and "Jakarta Leads in Worst Air Pollution" have understandably raised significant concerns about public health. This alarming situation has captured my attention and motivated me to initiate a project addressing this issue. While the project does not aim to provide direct solutions for pollution reduction, it does present a straightforward approach for air quality prediction based on measurement data. Additionally, it proposes a method for forecasting these measurements several days in advance.

# Problem Statement
Given the alarming poor quality of air in Jakarta, there is an urgent need to develop tools for predicting air quality based on daily measurements. This will provide the public with continuous updates on Jakarta's air quality, allowing them to make necessary preparations, such as wearing masks when engaging in outdoor activities. Additionally, a forecasting system is required to help the public monitor air quality not only for the current day but also for the next one, two, or even up to a week ahead. 

# Objective
The primary objective of this project is to offer a user-friendly method for predicting air quality, relying on daily measurement data. Furthermore, the project introduces a means of forecasting these measurements for upcoming days. This innovative approach enables us to anticipate the potential air quality for the next day, week, or even month.

## Jakarta Air Quality Prediction
This project aims to provide accurate predictions based on daily measurements of various air quality parameters, including PM10, NO2, CO, O3, and SO2. Since these measurements vary on a daily basis, we can effectively classify the current air quality into three categories: "Baik" (good, indicating low pollution levels), "Sedang" (moderate, representing a state worse than 'good' but better than 'unhealthy'), and "Tidak Sehat" (unhealthy, indicating high pollution levels detrimental to health). The prediction process employs a REST API and leverages FastAPI to swiftly generate predictions, the results of which can be conveniently downloaded in JSON format.

## Air Quality Forecast
Furthermore, this project offers a reliable method for forecasting pollutant measurements over the span of the upcoming day up to the next 30 days. The forecasting approach involves the use of SARIMAX, which provides a robust mechanism for predicting future measurements.

# Methodology
## Data Collection
The dataset used for this project was obtained from:
https://data.jakarta.go.id/organization/badan-pengelolaan-lingkungan-hidup-daerah
The collected data spans from 2010 to 2021. The data was merged into a single dataset, which was subsequently divided into training and testing sets.

## Data Cleaning
The merged dataset underwent a cleaning process, where unnecessary data was removed. Missing values were imputed with the mean, and outliers were addressed using the Isolation Forest method. The target variable was transformed into numeric data before being passed to the model for training.

## Training Model
The preprocessed training and testing datasets were then used to train the model, which was subsequently validated using the test dataset. The trained model was saved for later use in making predictions.

## Model Deployment
The model was deployed using two methods:

1. FastAPI hosted on AWS
Address: http://43.218.104.79:8080

2. Huggingface with Gradio and FastAPI
Address: https://huggingface.co/spaces/Rianknow/air-quality



## Forecasting
This project also offers forecasting capabilities, utilizing the Sarimax time series forecasting model. Users have the flexibility to adjust the number of timesteps, enabling them to make forecasts for varying timeframes. The results are displayed alongside real data, including forecasted values. Additionally, a dataframe table is provided, offering detailed information on pollutant values. The forecasting feature is accessible via Streamlit at the following address: 
https://standard-index-air-jakarta.streamlit.app/



## Dependencies
To enable forecasting using SARIMAX, it's essential to install the statsmodels library. You can install it by executing the following command:

Copy code
pip install statsmodels

## Areas for Improvement
It's worth noting that the forecasting process is still undergoing refinement. Occasionally, certain forecasts yield negative values. This issue could be attributed to the extreme nature of some data points used in predictions, leading to these undesirable negative outcomes. The project's associated notebooks also explore alternative forecasting methods such as ARIMA and LSTM. As solutions are developed to address these issues, the forecasts will be updated to ensure accuracy and reliability.
