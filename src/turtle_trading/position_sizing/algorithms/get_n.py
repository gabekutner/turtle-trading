#!/usr/bin/env python
# -*- coding: utf8 -*-
""" the underlying volatility of an asset """
import warnings
import datetime
import pandas as pd
from typing import Optional

from yahoo_fin.stock_info import get_data

""" ignore Pandas Future Warning """
warnings.simplefilter(action='ignore', category=FutureWarning)


def getn(ticker: str, date: Optional[datetime.date] = None):
  """ shortcut function for class: N  """
  return N(ticker, date).n

class N:
  """ this class represents the process for calculating `N` """
  def __init__(self, ticker: str, date: Optional[datetime.date] = None):
    self.ticker = ticker.upper()
    self.date = date

    self.get_dataframe()
    self.append_new_columns()
    self.pdn = self.get_pdn()
    self.n = self.get_n()

  def get_dataframe(self) -> pd.DataFrame:
    """ get the dataframe """
    df = get_data(self.ticker, interval='1d')[['low', 'high', 'close']].loc[::-1]

    if not self.date:
      self.dataframe = df.head(20)
      return self.dataframe
    
    self.dataframe = df.loc[self.date:].head(20)
    return self.dataframe

  def append_new_columns(self) -> pd.DataFrame:
    """ create previous close and true range columns """
    self.dataframe['previous_close'] = self.dataframe['close'].shift(-1)
    self.dataframe['true_range'] = 0

    for index, row in enumerate(self.dataframe.iterrows()):
      
      # Set the last 'previous_close' to 0, otherwise will raise NoneType error
      if isinstance(row[1]['previous_close'], type(None)):
        row[1]['previous_close'] = 0

      maximum = max(
        row[1]['high'] - row[1]['low'], row[1]['high'] - row[1]['previous_close'], row[1]['previous_close'] - row[1]['low']
      ) 
      self.dataframe.iloc[index, self.dataframe.columns.get_loc('true_range')] = maximum

  def get_pdn(self) -> float:
    """ calculate the previous day's n """
    return sum(self.dataframe['true_range'][1:]) / 20
  
  def get_n(self) -> float:    
    """ calculate n """
    return round(((19 * self.pdn + self.dataframe['true_range'][-1]) / 20), 4)