#!/usr/bin/env python
# -*- coding: utf8 -*-
"""  """
import requests
import pandas as pd
from bs4 import BeautifulSoup

""" avoid SSL Error """
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

futures_url_keymap = [{
  'us00': 'https://www.marketwatch.com/investing/future/us00', # 30 year treasury bond, US00:CBOT
  'ty00': 'https://www.marketwatch.com/investing/future/ty00', # 10 year treasury note, TY00:CBOT

  'kc00': 'https://www.marketwatch.com/investing/future/kc00', # coffee, KC00:CSCE
  'cc00': 'https://www.marketwatch.com/investing/future/cc00', # cocoa, CC00:CSCE
  'sb00': 'https://www.marketwatch.com/investing/future/sb00', # sugar, SB00:CSCE
  'ct00': 'https://www.marketwatch.com/investing/future/ct00', # cotton, CT00:CSCE

  'sfc00': 'https://www.marketwatch.com/investing/future/sfc00', # swiss franc, SFC00:CME
  '': '', # deutschmark
  'bp00': 'https://www.marketwatch.com/investing/future/bp00', # british pound, BP00:CME
  '': '', # french franc
  'jy00': 'https://www.marketwatch.com/investing/future/jy00', # japanese yen, JY00:CME
  'cd00': 'https://www.marketwatch.com/investing/future/cd00', # canadian dollar, CD00:CME
  'sp00': 'https://www.marketwatch.com/investing/future/sp00', # s&p 500 stock index, SP00:CME
  'ed00': 'https://www.marketwatch.com/investing/future/ed00', # eurodollar, ED00:CME
  '': '', # 90 day .s. treasury bill
  
  'gc00': 'https://www.marketwatch.com/investing/future/gc00', # gold, GC00:COMEX
  'si00': 'https://www.marketwatch.com/investing/future/si00', # silver, SI00:COMEX
  'hg00': 'https://www.marketwatch.com/investing/future/hg00', # copper, HG00:COMEX
 
  'cl00': 'https://www.marketwatch.com/investing/future/cl00', # crude oil, CL00:NYMEX
  'ho00': 'https://www.marketwatch.com/investing/future/ho00', # heating oil, HO00:NYMEX
  'rb00': 'https://www.marketwatch.com/investing/future/rb00', # unleaded gas, RB00:NYMEX
}]


class FuturesData:
  def __init__(self, ticker: str):
    self.ticker = ticker
    self.base_url = 'https://www.marketwatch.com/investing/future/'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

  def _make_request(self, url):
    """ make request """
    r = requests.get(url, headers=self.headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return r.status_code, soup
  
  def get_futures_live_price(self):
    """ get live price """
    url = f"{self.base_url}{self.ticker}"
    status_code, soup = self._make_request(url)

    try:
      live_price = soup.find(
        "div", {"class": "intraday__data"}).find(
          "h2", {"class": "intraday__price"}).find(
            "bg-quote", {"class": "value"}
        )
      return live_price.text
    
    except AttributeError:
      raise ValueError(f'ticker {self.ticker} not found')
  
  def get_futures_data(self):
    """ get price dataframe """
    url = f"{self.base_url}{self.ticker}/download-data?startDate=1/2/2023&endDate=1/23/2024"
    status_code, soup = self._make_request(url)
    try:
      download_url = soup.find("mw-downloaddata", {"id": "download-data-tabs"}).find("a")['href']
    except AttributeError:
      raise ValueError(f'ticker {self.ticker} not found')
    download_url = download_url.replace(" ", "%")

    start_date = "01/02/2023"
    new_url = download_url[:download_url.find("startdate=")+len("startdate=")] + start_date + download_url[download_url.find("startdate=")+len("startdate="):][download_url[download_url.find("startdate=")+len("startdate="):].find("%"):]
    new_url = new_url.replace("00:00:00", "2000:00:00")
    new_url = new_url.replace("23:59:59", "2000:00:00")

    df = pd.read_csv(new_url)

    # dataframe formatting
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.rename(columns={"High": "high", "Low": "low", "Close": "close", "Open": "open"})
    df.set_index('Date', inplace=True)
    return df