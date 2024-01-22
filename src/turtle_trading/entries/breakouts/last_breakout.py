#!/usr/bin/env python
# -*- coding: utf8 -*-
""" last breakouts and profitability """
import datetime
from typing import Tuple, Optional

from turtle_trading.config.breakouts.breakout import getbreakouts, check_if_breakout
from turtle_trading.position_sizing.algorithms.get_n import getn
from turtle_trading.dataframe_loader import DataFrameLoader
from turtle_trading.config.utils import reset_and_reverse


def get_last_breakout(dataframe: DataFrameLoader, days: int, skip: Optional[int] = 1) -> Tuple[datetime.date, bool]:
  """ get the last breakout date and direction """
  dataframe = reset_and_reverse(dataframe)

  for index, row in enumerate(dataframe.dataframe.iterrows()):

    date = dataframe.dataframe.iloc[index].name.date()
    breakout_tuple = getbreakouts(dataframe, days, date, True)
    
    if check_if_breakout(breakout_tuple) and index+1 > skip:
      # true if long breakout, false if short breakout
      return (date, index, True if breakout_tuple[2] >= breakout_tuple[0] else False)
      
    
def get_last_breakout_profitability(dataframe: DataFrameLoader, stand_devs: float, breakout_tuple: Tuple[datetime.date, int, bool]) -> bool:
  """ get the last breakout profitability """
  dataframe = reset_and_reverse(dataframe)

  breakout_n = getn(dataframe, breakout_tuple[0])
  breakout_price = dataframe.dataframe.iloc[breakout_tuple[1]].close
 
  for index, row in enumerate(dataframe.dataframe.iloc[:breakout_tuple[1]].iterrows()):
    
    if index == 10: # before a profitable 10-day exit
      break
    
    if breakout_tuple[2]: # if long breakout
      if any(ele <= breakout_price - (breakout_n * stand_devs) for ele in (row[1].high, row[1].low)):
        return False

    if not breakout_tuple[2]: # if short breakout
      if any(ele >= breakout_price + (breakout_n * stand_devs) for ele in (row[1].high, row[1].low)):
        return False 
  
  return True