#!/usr/bin/env python
# -*- coding: utf8 -*-
""" entry systems - results come as booleans: True for a long breakout, False for a short breakout, None for no breakout  """
from turtle_trading.entries.last_breakout import get_last_breakout, get_last_breakout_profitability
from turtle_trading.dataframe_loader import DataFrameLoader
from turtle_trading._data.dataframe_loader import DataFrameLoader as dfl
from turtle_trading._config.breakout import getbreakouts, check_if_breakout
from turtle_trading._config.exceptions import arg_equals


def getentry(dataframe: dfl, system: int) -> bool:
  """ shortcut function for class: EntrySignal """
  arg_equals("system", (1, 2))
  dataframe.reset()
  
  return EntrySignal(dataframe, system).signal


class EntrySignal:
  """ this class represents an entry signal, true for a valid long entry, false for valid short entry, none for invalid. """
  def __init__(self, dataframe: dfl, system: int):
    self.dataframe = dataframe
    self.days = 20 if system == 1 else 55

    breakout_tuple = self.get_breakout_tuple()
    breakout_tuple = [float(i) for i in breakout_tuple]
    if self.days == 20:
      self.signal = self.system_one(breakout_tuple)
    elif self.days == 55:
      self.signal = self.system_two(breakout_tuple)
    else:
      raise ValueError("@param system should equal to one of (1, 2).")
    
  def get_breakout_tuple(self) -> tuple:
    """ get breakout numbers """
    breakout_tuple = getbreakouts(self.dataframe, self.days, include_current_extrema=True)
    return breakout_tuple

  def system_two(self, breakout_tuple):
    """ use system two """
    if check_if_breakout(breakout_tuple):
      # valid entry: true for long, false for short
      return True if breakout_tuple[2] >= breakout_tuple[0] else False
    
    return None

  def system_one(self, breakout_tuple):
    """ use system one """
    if check_if_breakout(breakout_tuple):
      last_breakout = get_last_breakout(self.dataframe, 20)

      if not get_last_breakout_profitability(self.dataframe, 2, last_breakout): # if false -> losing pos
        # valid entry: return direction for entry
        return last_breakout[2] 
        
      elif get_last_breakout_profitability(self.dataframe, 2, last_breakout): 
        # invalid entry: last pos was winning
        return None 
      
    return None