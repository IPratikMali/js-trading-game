import yfinance as yf
import time

while True:
    msft = yf.Ticker('AAPL')
    hist = msft.history(period='60m', interval='1m')
    hist.rename(str.lower, axis='columns').to_json('data.json', orient='records')
    print("data collected")
    time.sleep(60)
