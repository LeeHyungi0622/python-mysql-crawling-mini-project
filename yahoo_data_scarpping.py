import requests
from bs4 import BeautifulSoup
import yfinance as yf
import datetime

investments_list = ['BTC-USD']

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2022, 4, 6)

df = yf.download(investments_list, start=start, end=end)



print(df)
