#
#
"""  """
import requests
from bs4 import BeautifulSoup

futures_url_keymap = [{
  'US00:CBOT': 'https://www.marketwatch.com/investing/future/us00', # 30 year treasury bond
  'TY00:CBOT': 'https://www.marketwatch.com/investing/future/ty00', # 10 year treasury note

  'KC00:CSCE': 'https://www.marketwatch.com/investing/future/kc00', # coffee
  'CC00:CSCE': 'https://www.marketwatch.com/investing/future/cc00', # cocoa
  'SB00:CSCE': 'https://www.marketwatch.com/investing/future/sb00', # sugar
  'CT00:CSCE': 'https://www.marketwatch.com/investing/future/ct00', # cotton

  'SFC00:CME': 'https://www.marketwatch.com/investing/future/sfc00', # swiss franc
  '': '', # deutschmark
  'BP00:CME': 'https://www.marketwatch.com/investing/future/bp00', # british pound
  '': '', # french franc
  'JY00:CME': 'https://www.marketwatch.com/investing/future/jy00',
  'CD00:CME': 'https://www.marketwatch.com/investing/future/cd00', # canadian dollar
  'SP00:CME': 'https://www.marketwatch.com/investing/future/sp00', # s&p 500 stock index
  'ED00:CME': 'https://www.marketwatch.com/investing/future/ed00', # eurodollar
  '': '', # 90 day .s. treasury bill
  
  'GC00:COMEX': 'https://www.marketwatch.com/investing/future/gc00', # gold
  'SI00:COMEX': 'https://www.marketwatch.com/investing/future/si00', # silver
  'HG00:COMEX': 'https://www.marketwatch.com/investing/future/hg00', # copper
 
  'CL00:NYMEX': 'https://www.marketwatch.com/investing/future/cl00', # crude oil
  'HO00:NYMEX': 'https://www.marketwatch.com/investing/future/ho00', # heating oil
  'RB00:NYMEX': 'https://www.marketwatch.com/investing/future/rb00', # unleaded gas
}]


symbol = 'rb00'

r = requests.get('https://www.marketwatch.com/investing/future/'+symbol)
soup = BeautifulSoup(r.content, 'html.parser')


def get_live_price(soup: BeautifulSoup):
  """ get the live price """
  live_price = soup.find("bg-quote", {"class": "value"})
  return live_price.text


def get_data(soup):
  """ get price history """
  table_wrapper = soup.find("div", {"class": "download-data"}).find("div", {"class": "overflow--table"})
  print(table_wrapper.table)