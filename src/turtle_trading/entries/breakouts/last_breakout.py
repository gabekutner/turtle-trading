#!/usr/bin/env python
# -*- coding: utf8 -*-
""" last breakouts and profitability """
import datetime
import pandas as pd
from typing import Tuple, Optional

from turtle_trading.entries.breakouts.breakout import getbreakouts, check_if_breakout
from turtle_trading.position_sizing.algorithms.get_n import getn


def get_last_breakout(ticker: str, df: pd.DataFrame, days: int, skip: Optional[int] = 1) -> Tuple[datetime.date, bool]:
  """ get the last breakout date and direction """
  df = df.loc[::-1] # reverse
  for index, row in enumerate(df.iterrows()):

    date = df.iloc[index].name.date()
    breakout_tuple = getbreakouts(ticker, days, date, True)
    
    if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]) and index+1 > skip:
      return (date, index, True if breakout_tuple[2] >= breakout_tuple[0] else False)
      
    
def get_last_breakout_profitability(ticker: str, df: pd.DataFrame, stand_devs: float, breakout_tuple: Tuple[datetime.date, int, bool]):
  """ get the last breakout profitability """
  df = df.iloc[::-1] # reverse

  n = getn(ticker, breakout_tuple[0])
  price = df.iloc[breakout_tuple[1]].close
 
  for index, row in enumerate(df.iloc[:breakout_tuple[1]].iterrows()):

    if index == 10: # before a profitable 10-day exit
      break

    if breakout_tuple[2]:
      if row[1]['high'] - price >= n * stand_devs:
        return False
      
    if not breakout_tuple[2]:
      if row[1]['low'] - price <= n * stand_devs:
        return False
    
  return True