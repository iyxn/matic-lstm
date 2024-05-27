import streamlit as st
from tensorflow.keras.models import load_model

from utils.get_data import get_hourly_price
from utils.preprocessing import make_hourly
from utils.preprocessing import inverter

import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "Dashboard Forecasting", layout = "wide")

st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Forecasting</h1>", unsafe_allow_html=True)

data_prep = get_hourly_price()
hourly_data, high_processed, low_processed, close_procesed = make_hourly(data_prep)
col1, col2 = st.columns(2)

@st.cache_resource
def model():
    high_model = load_model("model/best_model_high.h5")
    low_model = load_model("model/best_model_low.h5")
    close_model = load_model("model/best_model_close.h5")
    
    return high_model, low_model, close_model
def forecast():
    high_model, low_model, close_model = model()
    high_pred = high_model.predict(high_processed)
    low_pred = low_model.predict(low_processed)
    close_pred = close_model.predict(close_procesed)
    
    inverted_high, inverted_low, inverted_close = inverter(high_pred, low_pred, close_pred)

    chart(inverted_high[0][0], inverted_low[0][0], inverted_close[0][0])

def chart(high_pred, low_pred, close_pred):
    plt.style.use('dark_background')
    plt.figure(figsize=(8,4))
    plt.plot(hourly_data["timestamp"], hourly_data["close"], label = "Harga Matic")
    plt.axhline(high_pred, color = "g", linestyle = "-", label = "Prediksi High")
    plt.axhline(low_pred, color = "r", linestyle ="-", label = "Prediksi Low")
    plt.axhline(close_pred, color = "b", linestyle ="-", label = "Prediksi Close")
    plt.xlabel("Jam")
    plt.ylabel("Harga")
    plt.legend(loc = "best")
    with col1:
        st.subheader("Grafik Prediksi 1 Jam Kedepan")
        st.write("P.High:", high_pred, "P.low:", low_pred, "P.Close:", close_pred)
        st.pyplot(plt)

forecast()

with col2:
    st.subheader("Prediksi Hari Ini")  
    st.write("High: Low: Close: ")
    st.pyplot(plt)  

st.dataframe(hourly_data[["timestamp","open","high","low","close"]], height = 300, width = 450)