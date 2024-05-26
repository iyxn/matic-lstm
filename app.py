import streamlit as st
import pandas as pd
from datetime import datetime
import ccxt
import matplotlib.pyplot as plt

from utils.get_data import get_weekly_price, get_fng

import streamviz

weekly_data, fng = get_weekly_price()
fng_value = int(fng[0])
fng_class = fng[1]

st.set_page_config(
    page_title = "Dashboard Utama", layout = "wide")

st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Utama</h1>", unsafe_allow_html=True)
st.subheader("Grafik Harga Matic 7 Hari Terakhir dan Index Fear And Greed")
st.write("Harga Saat Ini: ",str(weekly_data["close"].iloc[-1]))

col1, col2 = st.columns(2)

def btc_line_chart():
	with col1:
		st.line_chart(data = weekly_data, x = "timestamp", y = "close",use_container_width=True)
	
	with col2:
		streamviz.gauge(fng_value/100, gSize = "MED", gTitle = fng_class , gTheme = "White")

	
	st.subheader("Data Historis MATIC/USD 7 Hari Terakhir")
	st.dataframe(weekly_data.sort_values(by="timestamp", ascending = True), width = 1500, height = 400)


btc_line_chart()