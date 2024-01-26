#!/usr/bin/env python
# -*- coding: utf8 -*-
""" initialize a dataframe """
import warnings
import datetime

from yahoo_fin.stock_info import get_data, get_live_price
from turtle_trading._data.futures_query import FuturesData, futures_url_keymap

""" ignore Pandas Future Warning and SettingWithCopyWarnings """
warnings.simplefilter(action='ignore', category=FutureWarning)


class DataFrameLoader:
  """This class builds the pd.DataFrame used for turtle_trading functionalities. 

  :param ticker: A ticker symbol.
  :param type: Optional, stock or futures.
  """
  def __init__(self, ticker: str):
    self.ticker = ticker.upper()

    if ticker.lower() in list(futures_url_keymap[0].keys()):
      self.type = "futures"
    else:
      self.type = None

    self.dataframe = self.__initalize(self.type)
    self.base_dataframe = self.dataframe # back up 

  def __initalize(self, type: str):
    """ initialize dataframe """
    if type is not None:
      self.futures_loader = FuturesData(self.ticker)
      dataframe = self.futures_loader.get_futures_data()
    else: 
      dataframe = get_data(self.ticker, interval='1d')
    return dataframe
  
  def edit_columns(self, columns: list[str]):
    """ get specific columns """
    self.dataframe = self.dataframe[columns]
    return self.dataframe
    
  
  def reverse(self):
    """ reverse dataframe """
    self.dataframe = self.dataframe.iloc[::-1]
    return self.dataframe
  
  def start_at(self, date: datetime.date):
    """ start dataframe at a location """
    if self.type is not None:
      self.dataframe = self.dataframe[:date]
    else:
      self.dataframe = self.dataframe[date:]
    return self.dataframe
  
  @property
  def live_price(self):
    """ get live price """
    if self.type is not None:
      return self.futures_loader.get_futures_live_price()
    else:
      return get_live_price(self.ticker)

  def reset(self):
    """ reset dataframe """
    self.dataframe = self.base_dataframe
    return self.dataframe
  
  def get_price(self, date: datetime.date): 
    """ get price based on date """
    if str(self.dataframe.iloc[0].name).split("-")[0] != str(datetime.datetime.now().year):
      # will work if ticker became public before current year, else will not work
      self.reverse()
    
    return self.start_at(date).iloc[0]['close']