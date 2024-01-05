#!/usr/bin/env python
# -*- coding: utf8 -*-
""" breakouts """
import datetime
import pandas as pd
from typing import Tuple, Optional

from turtle_trading.dataframe_loader import DataFrameLoader


def getbreakouts(dataframe: DataFrameLoader, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False) -> Tuple[float]:
  """ shortcut function for class: Breakout """
  dataframe.reset()
  return Breakout(dataframe, days, date, include_current_extrema).breakouts


def check_if_breakout(high: float, low: float, pos_high: float, pos_low: float) -> bool:
  """ shortcut function for checking a breakout """
  if pos_high >= high or pos_low <= low:
    return True


class Breakout:
  """ this class represents finding breakout numbers """
  def __init__(self, dataframe: DataFrameLoader, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False):
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
    """ find the extrema """
    maximum, minimum = self.dataframe['high'].max(), self.dataframe['low'].min()
    if self.include_current_extrema:
      pos_high, pos_low = self.dataframe.iloc[0]['high'], self.dataframe.iloc[0]['low']
      return (maximum, minimum, pos_high, pos_low)

    return (maximum, minimum)