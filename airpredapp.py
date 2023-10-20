import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from functools import lru_cache

@lru_cache(maxsize=1)
def load_model():
    with open('model/model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()


def plot(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    pollutants = df.columns[1:]  # Exclude the first column (index)
    for pollutant in pollutants:
        ax.plot(df[pollutant], label=pollutant)
    ax.set_title('Pollutant Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Pollutant')
    ax.legend()
    st.pyplot(fig)

def predict(df):
    df2 = df.copy()
    predictions = model.predict(df)
    predictions_labels = ['BAIK' if pred == 0 else 'SEDANG' if pred == 1 else 'TIDAK SEHAT' for pred in predictions]
    df2['Prediction'] = predictions_labels
    return df2

def main():
    st.title("Air Quality Prediction Using Machine Learning")

    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Display the original dataframe
        st.subheader("Original Data")
        st.write(df)

        # Plot columns
        st.subheader("Pollutant Data Plots")
        plot(df)

        # Make predictions and display the results
        if st.button('Predict'):
            predictions_df = predict(df)
            st.subheader("Predictions")
            st.write(predictions_df)
        
        #If prediction_df exist create count plot for each category (BAIK, SEDANG, TIDAK SEHAT), else write "Please click predict button"
        if 'predictions_df' in locals():
            st.subheader("Count Plot for Each Category")
            st.write(predictions_df['Prediction'].value_counts())
            st.bar_chart(predictions_df['Prediction'].value_counts())
        else:
            st.write("Please click predict button")
if __name__ == '__main__':
    main()
