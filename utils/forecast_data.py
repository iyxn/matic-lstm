import pandas as pd
import os

def make_historical(hourly_data, forecast_data):
    file_path = 'dataset/history_forecast.xlsx'
    timestamp = hourly_data["timestamp"].values[-1]
    pred_high = forecast_data[0]
    pred_low = forecast_data[1]
    pred_close = forecast_data[2]
    
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        print(str(timestamp))
        print(df["timestamp"].astype(str).tolist())
        if timestamp not in df["timestamp"].tolist():
            df.loc[len(df)] = {"timestamp": timestamp,  "pred_high": pred_high, "pred_low": pred_low, "pred_close": pred_close}
            df.to_excel(file_path, index=False)
    else:
        df = pd.DataFrame({"timestamp":timestamp, "pred_high":pred_high, "pred_low":pred_low, "pred_close":pred_close})
        df.to_excel(file_path, index=False)
