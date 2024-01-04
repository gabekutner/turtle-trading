#!/usr/bin/env python
# -*- coding: utf8 -*-
""" breakouts """
import datetime
import pandas as pd
from typing import Tuple, Optional

from yahoo_fin.stock_info import get_data


def getbreakouts(ticker: str, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False):
  """ shortcut function for class: Breakout """
  return Breakout(ticker, days, date, include_current_extrema).breakouts


def check_if_breakout(high: float, low: float, pos_high: float, pos_low: float):
  """ shortcut function for checking a breakout """
  if pos_high >= high or pos_low <= low:
    return True


class Breakout:
  """ this class represents finding breakout numbers """
  def __init__(self, ticker: str, days: int, date: Optional[datetime.date] = None, include_current_extrema: Optional[bool] = False):
    self.ticker = ticker.upper()
    self.days = days
    self.date = date
    self.include_current_extrema = include_current_extrema

    self.get_dataframe()
    self.breakouts = self.find_extrema()

  def get_dataframe(self) -> pd.DataFrame:
    """ get dataframe """
    df = get_data(self.ticker, interval='1d')[['low', 'high']].loc[::-1]
    if not self.date:
      self.dataframe = df.head(self.days)
      return self.dataframe
    
    self.dataframe = df.loc[self.date:].head(self.days)
    return self.dataframe
  
  def find_extrema(self) -> Tuple[float]:
    """ find the extrema """
    maximum, minimum = self.dataframe['high'].max(), self.dataframe['low'].min()
    if self.include_current_extrema:
      pos_high, pos_low = self.dataframe.iloc[0]['high'], self.dataframe.iloc[0]['low']
      return (maximum, minimum, pos_high, pos_low)

    return (maximum, minimum)