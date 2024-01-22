#!/usr/bin/env python
# -*- coding: utf8 -*-
""" exits

To exit from a System 1 trade, if the 10 day high (short trade) was broken, that meant close the trade. 
Likewise if the 10 day low (long trade) was broken, close the trade. To exit from a System 2 trade, 
a 20 day breakout in the opposite direction would signal the end of the trade.
"""
import datetime
from typing import Literal, Union

from turtle_trading.dataframe_loader import DataFrameLoader
from turtle_trading.utils import reset_and_reverse
from turtle_trading.entries import getbreakouts


def shortcut_check_breakout(df: DataFrameLoader, system: Union[Literal[1], Literal[2]], direction: bool, date: datetime.date = None,) -> bool:
  """ shortcut func """
  dir = 10 if system == 1 else 20
  print(dir)
  breakout_tuple = getbreakouts(dataframe=df, days=dir, date=date, include_current_extrema=True)
  print(breakout_tuple)

  if direction is True: # long pos 
    if breakout_tuple[3] <= breakout_tuple[1]: # if short breakout
      return True

  if direction is False: # short pos
    if breakout_tuple[2] >= breakout_tuple[0]: # if long breakout
      return True
    
  return False


def getdecision(df: DataFrameLoader, system: Union[Literal[1], Literal[2]], direction: bool, date: datetime.date = None) -> bool:
  """ Get the exit decision.

  Returns:
    True: exit
    False: no exit 

  df: DataFrameLoader
  date: Date the position was entered
  system: 10-day (1) or 20-day (2)
  direction: short (f) or long (t)
  """
  if system == 1: # 10-day
    return shortcut_check_breakout(df, date, system, direction)
  
  if system==2: # 20-day
    return shortcut_check_breakout(df, date, system, direction)