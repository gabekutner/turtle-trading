#!/usr/bin/env python
# -*- coding: utf8 -*-
""" volatility adjusted position units """
import datetime
import pandas as pd
# from typing import Optional

from yahoo_fin.stock_info import get_data
from turtle_trading.position_sizing.get_n import getn


def getunit(ticker: str, account: float, **kwargs):
  """ shortcut function for class: Unit """
  return Unit(ticker, account, **kwargs).unit


class Unit:
  """ this class represents the process for calculating unit size """
  def __init__(self, ticker: str, account: float, **kwargs):
    self.ticker = ticker.upper()
    self.account = account

    if 'n' in kwargs:
      self.n = kwargs.get('n')
      self.date = None

    if 'date' in kwargs:
      self.date = kwargs.get('date')
      self.n = None

    if 'n' and 'date' in kwargs:
      raise AttributeError(f'Set only one of `n` or `date`')

    self.dollar_volatility_adjustment()
    self.unit = self.get_unit_size()

  def dollar_volatility_adjustment(self) -> float: 
    """ calculating the dollar volatility of the asset """
    if self.date:
      price = get_data(self.ticker, start_date=self.date).iloc[0]['close']
      n = getn(self.ticker, self.date)
      self.dollar_volatility = n * price
      return self.dollar_volatility

    if not self.date:
      price = get_data(self.ticker, end_date=pd.Timestamp.today() + pd.DateOffset(10)).close[-1]
      self.dollar_volatility = self.n * price
      return self.dollar_volatility
  
  def get_unit_size(self) -> float:
    """ calculating unit size  """
    return round(((0.01 * self.account) / self.dollar_volatility), 4)