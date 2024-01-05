#!/usr/bin/env python
# -*- coding: utf8 -*-
""" entry systems """
from typing import Union, Literal

from turtle_trading.entries.breakouts.breakout import getbreakouts, check_if_breakout
from turtle_trading.entries.breakouts.last_breakout import get_last_breakout, get_last_breakout_profitability
from turtle_trading.dataframe_loader import DataFrameLoader


def getsignal(dataframe: DataFrameLoader, system: Union[Literal[1], Literal[2]]) -> bool:
  """ shortcut function for class: EntrySignal """
  dataframe.reset()
  return EntrySignal(dataframe, system).signal


class EntrySignal:
  """ this class represents an entry signal, true for a valid entry, false for invalid """
  def __init__(self, dataframe: DataFrameLoader, system: Union[Literal[1], Literal[2]]):
    self.dataframe = dataframe
    self.system = system

    self.signal = self.get_signal()

  def get_signal(self) -> bool:
    """ get the entry signal """
    if self.system == 2:
      breakout_tuple = getbreakouts(self.dataframe, 55, include_current_extrema=True)

      if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]):
        return True
      else:
        return False
      
    if self.system == 1:

      breakout_tuple = getbreakouts(self.dataframe, 20, include_current_extrema=True)
      self.dataframe.reset()

      if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]):
        last_breakout = get_last_breakout(self.dataframe, 20)
        self.dataframe.reset()
        if get_last_breakout_profitability(self.dataframe, 2, last_breakout):
          return False
        
        else: return True