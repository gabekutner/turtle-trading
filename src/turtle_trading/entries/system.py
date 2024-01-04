#!/usr/bin/env python
# -*- coding: utf8 -*-
""" entry systems """
from typing import Union, Literal

from yahoo_fin.stock_info import get_data
from turtle_trading.entries.breakouts.breakout import getbreakouts, check_if_breakout
from turtle_trading.entries.breakouts.last_breakout import get_last_breakout, get_last_breakout_profitability


def getsignal(ticker: str, system: Union[Literal[1], Literal[2]]):
  """ shortcut function for class: EntrySignal """
  return EntrySignal(ticker, system).signal


class EntrySignal:
  """ this class represents an entry signal, true for a valid entry, false for invalid """
  def __init__(self, ticker: str, system: Union[Literal[1], Literal[2]]):
    self.ticker = ticker
    self.system = system
    self.dataframe = get_data(ticker, interval='1d')

    self.signal = self.get_signal()

  def get_signal(self):
    """ get the entry signal """
    if self.system == 2:
      breakout_tuple = getbreakouts(self.ticker, 55, include_current_extrema=True)

      if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]):
        return True
      else:
        return False
      
    if self.system == 1:
      breakout_tuple = getbreakouts(self.ticker, 20, include_current_extrema=True)
      if check_if_breakout(breakout_tuple[0], breakout_tuple[1], breakout_tuple[2], breakout_tuple[3]):
        last_breakout = get_last_breakout(self.ticker, self.dataframe, 20)
        if get_last_breakout_profitability(self.ticker, self.dataframe, 2, last_breakout):
          return False
        
        else: return True