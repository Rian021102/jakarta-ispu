# Prologue
In the past few days, both news outlets and social media platforms have been consistently reporting the deteriorating air quality in Jakarta. Headlines such as "Jakarta: The Most Populated City" and "Jakarta Leads in Worst Air Pollution" have understandably raised significant concerns about public health. This alarming situation has captured my attention and motivated me to initiate a project addressing this issue. While the project does not aim to provide direct solutions for pollution reduction, it does present a straightforward approach for air quality prediction based on measurement data. Additionally, it proposes a method for forecasting these measurements several days in advance.

## Project Description
The primary objective of this project is to offer a user-friendly method for predicting air quality, relying on daily measurement data. Furthermore, the project introduces a means of forecasting these measurements for upcoming days. This innovative approach enables us to anticipate the potential air quality for the next day, week, or even month.

### Jakarta Air Quality Prediction
This project aims to provide accurate predictions based on daily measurements of various air quality parameters, including PM10, NO2, CO, O3, and SO2. Since these measurements vary on a daily basis, we can effectively classify the current air quality into three categories: "Baik" (good, indicating low pollution levels), "Sedang" (moderate, representing a state worse than 'good' but better than 'unhealthy'), and "Tidak Sehat" (unhealthy, indicating high pollution levels detrimental to health). The prediction process employs a REST API and leverages FastAPI to swiftly generate predictions, the results of which can be conveniently downloaded in JSON format.

### Air Quality Forecast
Furthermore, this project offers a reliable method for forecasting pollutant measurements over the span of the upcoming day up to the next 30 days. The forecasting approach involves the use of SARIMAX, which provides a robust mechanism for predicting future measurements.

## Dependencies
To enable forecasting using SARIMAX, it's essential to install the statsmodels library. You can install it by executing the following command:

Copy code
pip install statsmodels

## Areas for Improvement
It's worth noting that the forecasting process is still undergoing refinement. Occasionally, certain forecasts yield negative values. This issue could be attributed to the extreme nature of some data points used in predictions, leading to these undesirable negative outcomes. The project's associated notebooks also explore alternative forecasting methods such as ARIMA and LSTM. As solutions are developed to address these issues, the forecasts will be updated to ensure accuracy and reliability.
