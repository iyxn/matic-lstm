import streamlit as st
from tensorflow.keras.models import load_model
import plotly.graph_objects as go
from utils.get_data import get_hourly_price
from utils.preprocessing import make_hourly, inverter
from utils.forecast_data import make_historical

import matplotlib.pyplot as plt

st.set_page_config(
    page_title = "Dashboard Forecasting", layout = "wide")

st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Forecasting</h1>", unsafe_allow_html=True)

data_prep = get_hourly_price()
hourly_data, high_processed, low_processed, close_procesed = make_hourly(data_prep)


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
    predicted_data = [inverted_high[0][0], inverted_low[0][0], inverted_close[0][0]]
    
    make_historical(hourly_data, predicted_data)

    chart(predicted_data)

def chart(predicted_data):
    matic_now = hourly_data.iloc[-1]
    # Create candle chart
    candle_chart = go.Candlestick(x=hourly_data["timestamp"],
                                  open=hourly_data["open"],
                                  high=hourly_data["high"],
                                  low=hourly_data["low"],
                                  close=hourly_data["close"])

    # Create line chart from predicted data
    line_chart = go.Scatter(x=hourly_data["timestamp"],
                            y=[predicted_data[0]] * len(hourly_data["timestamp"]),
                            name="Prediksi High",
                            line=dict(color="green", width=2))

    line_chart_low = go.Scatter(x=hourly_data["timestamp"],
                               y=[predicted_data[1]] * len(hourly_data["timestamp"]),
                               name="Prediksi Low",
                               line=dict(color="red", width=2))

    line_chart_close = go.Scatter(x=hourly_data["timestamp"],
                                y=[predicted_data[2]] * len(hourly_data["timestamp"]),
                                name="Prediksi Close",
                                line=dict(color="blue", width=2))

    fig = go.Figure(data=[candle_chart, line_chart, line_chart_low, line_chart_close])
    fig.update_layout(xaxis_rangeslider_visible=False)

    st.subheader("Grafik Prediksi 1 Jam Kedepan")
    st.write("Harga Sekarang:", matic_now["close"])
    st.write("Prediksi=","High:", predicted_data[0], "Low:", predicted_data[1], "Close:", predicted_data[2])
    st.plotly_chart(fig)

forecast()
st.subheader("Grafik Prediksi Hari Ini")
st.write("Coming Soon!")

st.subheader("Data Harga MATIC Hari Ini")
st.dataframe(hourly_data[["timestamp","open","high","low","close"]], height = 300, width = 450)