#!/usr/bin/env python
# -*- coding: utf8 -*-
""" volatility adjusted position units """
import datetime
from typing import Optional

from turtle_trading.position_sizing.algorithms.get_n import getn
from turtle_trading.dataframe_loader import DataFrameLoader


def getunitsize(dataframe: DataFrameLoader, account: float, n: Optional[float] = None, date: Optional[datetime.date] = None):
  """ shortcut function for class: Unit """
  dataframe.reset()
  return Unit(dataframe, account, n, date).unit


class Unit:
  """ this class represents the process for calculating unit size """
  def __init__(self, dataframe: DataFrameLoader, account: float, n: Optional[float] = None, date: Optional[datetime.date] = None):
    self.dataframe = dataframe
    self.account = account
    self.n = n
    self.date = date

    if isinstance(n, type(None)) and isinstance(date, type(None)):
      raise AttributeError(f"Set either `n` or `date`.")
    
    if isinstance(n, float) and isinstance(date, datetime.date):
      raise AttributeError(f"Set only one of `n` or `date`.")

    self.dollar_volatility_adjustment()
    self.unit = self.get_unit_size()


  def dollar_volatility_adjustment(self) -> float: 
    """ calculating the dollar volatility of the asset """
    if self.date:

      price = self.dataframe.start_at(self.date).iloc[0]['close']
      n = getn(self.dataframe, self.date)
      self.dollar_volatility = n * price
      return self.dollar_volatility

    if not self.date:

      price = self.dataframe.live_price
      self.dollar_volatility = self.n * price
      return self.dollar_volatility
  

  def get_unit_size(self) -> float:
    """ calculating unit size  """
    return round(((0.01 * self.account) / self.dollar_volatility), 4)