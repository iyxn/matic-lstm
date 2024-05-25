import pandas as pd
import joblib

high_scaler = joblib.load("model/matic_high_scaler.h5")
low_scaler = joblib.load("model/matic_low_scaler.h5")
close_scaler = joblib.load("model/matic_close_scaler.h5")

def make_hourly(hourly_data):
	hourly_data["high_scaled"] = high_scaler.transform(hourly_data["high"].values.reshape(-1,1))
	hourly_data["low_scaled"] = low_scaler.transform(hourly_data["low"].values.reshape(-1,1))
	hourly_data["close_scaled"] = close_scaler.transform(hourly_data["close"].values.reshape(-1,1))

	return hourly_data

def inverter(high, low, close):
	high_invert = high_scaler.inverse_transform(high)
	low_invert = low_scaler.inverse_transform(low)
	close_invert = close_scaler.inverse_transform(close)

	return high_scaler, low_scaler, close