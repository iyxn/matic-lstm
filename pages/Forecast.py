import streamlit as st
from tensorflow.keras.models import load_model

from utils.get_data import get_hourly_price
from utils.preprocessing import make_hourly
from utils.preprocessing import inverter

import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "Dashboard Forecasting", layout = "wide") 

data_prep = get_hourly_price()
hourly_data, high_processed, low_processed, close_procesed = make_hourly(data_prep)

high_model = load_model("model/best_model_high.h5")
low_model = load_model("model/best_model_low.h5")
close_model = load_model("model/best_model_close.h5")

def forecast():
    high_pred = high_model.predict(high_processed)
    low_pred = low_model.predict(low_processed)
    close_pred = close_model.predict(close_procesed)
    
    inverted_high, inverted_low, inverted_close = inverter(high_pred, low_pred, close_pred)

    chart(inverted_high[0][0], inverted_low[0][0], inverted_close[0][0])

def chart(high_pred, low_pred, close_pred):
    plt.style.use('dark_background')
    plt.figure(figsize=(10,6))
    plt.plot(hourly_data["timestamp"], hourly_data["close"], label = "Harga Matic")
    plt.axhline(high_pred, color = "g", linestyle = "-", label = "Prediksi High")
    plt.axhline(low_pred, color = "r", linestyle ="-", label = "Prediksi Low")
    plt.axhline(close_pred, color = "b", linestyle ="-", label = "Prediksi Close")
    plt.xlabel("Jam")
    plt.ylabel("Harga")
    plt.legend(loc = "upper right")
    st.pyplot(plt)

forecast()

st.dataframe(hourly_data)




