import pandas as pd
import joblib

high_scaler = joblib.load("model/matic_high_scaler.joblib")
low_scaler = joblib.load("model/matic_low_scaler.joblib")
close_scaler = joblib.load("model/matic_close_scaler.joblib")

def make_hourly(hourly_data):
	hourly_data["high_scaled"] = high_scaler.transform(hourly_data["high"].values.reshape(-1,1))
	hourly_data["low_scaled"] = low_scaler.transform(hourly_data["low"].values.reshape(-1,1))
	hourly_data["close_scaled"] = close_scaler.transform(hourly_data["close"].values.reshape(-1,1))

	high_processed = hourly_data["high_scaled"][-4:-1].values.reshape(1,3,1)
	low_processed = hourly_data["low_scaled"][-4:-1].values.reshape(1,3,1)
	close_processed = hourly_data["close_scaled"][-4:-1].values.reshape(1,3,1)
	return hourly_data, high_processed, low_processed, close_processed

def inverter(high, low, close):
	high_invert = high_scaler.inverse_transform(high)
	low_invert = low_scaler.inverse_transform(low)
	close_invert = close_scaler.inverse_transform(close)

	return high_invert, low_invert, close_invert