#!/usr/bin/env python
# -*- coding: utf8 -*-
""" last breakouts and profitability """
import datetime
from typing import Tuple, Optional

from turtle_trading.entries.breakouts.breakout import getbreakouts, check_if_breakout
from turtle_trading.position_sizing.algorithms.get_n import getn
from turtle_trading.dataframe_loader import DataFrameLoader


def get_last_breakout(dataframe: DataFrameLoader, days: int, skip: Optional[int] = 1) -> Tuple[datetime.date, bool]:
  """ get the last breakout date and direction """
  dataframe.reset()
  dataframe.reverse()

  for index, row in enumerate(dataframe.dataframe.iterrows()):

    date = dataframe.dataframe.iloc[index].name.date()
    breakout_tuple = getbreakouts(dataframe, days, date, True)
    
    if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]) and index+1 > skip:
      return (date, index, True if breakout_tuple[2] >= breakout_tuple[0] else False)
      
    
def get_last_breakout_profitability(dataframe: DataFrameLoader, stand_devs: float, breakout_tuple: Tuple[datetime.date, int, bool]) -> bool:
  """ get the last breakout profitability """
  dataframe.reset()
  dataframe.reverse()
  n = getn(dataframe, breakout_tuple[0])
  price = dataframe.dataframe.iloc[breakout_tuple[1]].close
 
  for index, row in enumerate(dataframe.dataframe.iloc[:breakout_tuple[1]].iterrows()):

    if index == 10: # before a profitable 10-day exit
      break

    if breakout_tuple[2]:
      if row[1]['high'] - price >= n * stand_devs:
        return False
      
    if not breakout_tuple[2]:
      if row[1]['low'] - price <= n * stand_devs:
        return False
    
  return True