import ccxt
import pandas as pd
from datetime import datetime, timedelta
from urllib.request import urlopen
import json

binance = ccxt.binance()

symbol = 'MATIC/USD'

now = datetime.utcnow()
start_of_today = datetime(now.year, now.month, now.day)

def time_config(tf):
	if tf == "1h":
		since = int(start_of_today.timestamp() * 1000)
		return since
	else:
		seven_days_ago = start_of_today - timedelta(days=7)
		since = int(seven_days_ago.timestamp() * 1000)
		return since

def get_hourly_price():
	timeframe = "1h"
	since = time_config(timeframe)
	ohlcv = binance.fetch_ohlcv(symbol, timeframe, since)
	
	df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
	
	data = df.sort_values(by="timestamp", ascending = True)
	data = data[["timestamp","high","low","close"]]

	return data

def get_weekly_price():
	timeframe = "1d"
	since = time_config(timeframe)
	ohlcv = binance.fetch_ohlcv(symbol, timeframe, since)
	
	df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
	
	data = df.sort_values(by="timestamp", ascending = True)
	data = data[["timestamp","high","low","close"]]
	fng = get_fng()

	return data[1:], fng

def get_fng():
	url = "https://api.alternative.me/fng/?limit=1&format=json&date_format=us"
	response = urlopen(url)
	data_json = json.loads(response.read())
	
	value = data_json['data'][0]['value']
	value_classification = data_json['data'][0]['value_classification']

	fng = [value, value_classification]
	
	return fng