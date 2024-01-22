#!/usr/bin/env python
# -*- coding: utf8 -*-
""" breakouts """
import datetime
import pandas as pd
from typing import Tuple, Optional

from turtle_trading.dataframe_loader import DataFrameLoader
from turtle_trading.config.utils import is_market_open


def getbreakouts(dataframe: DataFrameLoader, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False) -> Tuple[float]:
  """ shortcut function for class: Breakout """
  dataframe.reset()
  return Breakout(dataframe, days, date, include_current_extrema).breakouts


def check_if_breakout(tuple: tuple[float]) -> bool:
  """ shortcut function for checking a breakout """
  if len(tuple) == 3:
    # market is open, using live price
    if tuple[2] >= tuple[0] or tuple[2] <= tuple[1]:
      return True
    
  if len(tuple) == 4:
    # market is closed, using high x low
    if tuple[2] >= tuple[0] or tuple[3] <= tuple[1]:
      return True


class Breakout:
  """ this class represents finding breakout numbers """
  def __init__(self, dataframe: DataFrameLoader, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False):
    self.dataframe_obj = dataframe
    self.dataframe = dataframe
    self.days = days
    self.date = date
    self.include_current_extrema = include_current_extrema

    self.edit_dataframe()
    self.breakouts = self.find_extrema()

  def edit_dataframe(self) -> pd.DataFrame:
    """ get dataframe """
    self.dataframe.edit_columns(['low', 'high'])
    self.dataframe.reverse()

    if not self.date:
      self.dataframe = self.dataframe.dataframe.head(self.days)
      return self.dataframe
    
    self.dataframe = self.dataframe.dataframe.loc[self.date:].head(self.days)
    return self.dataframe
  
  def find_extrema(self) -> Tuple[float]:
    """ find extrema """
    maximum, minimum = self.dataframe['high'].max(), self.dataframe['low'].min() # correct

    if self.include_current_extrema:
      if is_market_open(datetime.datetime.now()):
        return (maximum, minimum, self.dataframe_obj.live_price)

      else:
        pos_high, pos_low = self.dataframe.iloc[0]['high'], self.dataframe.iloc[0]['low']
        return (maximum, minimum, pos_high, pos_low)

    return (maximum, minimum)