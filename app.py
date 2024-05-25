import streamlit as st
import joblib
import pandas as pd
from datetime import datetime
import ccxt
import matplotlib.pyplot as plt

from utils.preprocessing import make_weekly
from utils.get_data import get_weekly_price, get_fng

import streamviz

weekly_data, fng = get_weekly_price()


st.set_page_config(
    page_title = "Dashboard Utama", layout = "wide")



st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Utama</h1>", unsafe_allow_html=True)
st.subheader("Grafik Harga Matic 7 Hari Terakhir dan Index Fear And Greed")
st.write("Harga Saat Ini: ",str(data["Close"].iloc[-1]))

col1, col2 = st.columns(2)

def btc_line_chart():
	with col1:
		st.line_chart(data = data, x = "Date", y = "Close",use_container_width=True)
	
	with col2:
		streamviz.gauge(fng_last/100, gSize = "MED", gTitle = fng_class , gTheme = "White")

	
	st.subheader("Data Historis BTC/USD 30 Hari Terakhir")
	st.dataframe(data[["Date", "High", "Low", "Close","index","klasifikasi"]].sort_values(by="Date", ascending = False), width = 1500, height = 600)
btc_line_chart()

