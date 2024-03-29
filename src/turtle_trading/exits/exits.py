#!/usr/bin/env python
# -*- coding: utf8 -*-
""" exit signals """
import datetime
from typing import Optional

from turtle_trading._data.dataframe_loader import DataFrameLoader as dfl
from turtle_trading._config.breakout import getbreakouts
from turtle_trading._config.exceptions import arg_equals


def getexit(dataframe: dfl, system: int, pos_direction: bool, date: Optional[datetime.date] = None):
  """ shortcut function for class: Exit """
  arg_equals("system", (1, 2))
  dataframe.reset()

  return Exit(dataframe=dataframe, system=system, pos_direction=pos_direction, date=date).exit


class Exit:
  """ this class represents an exit signal, True to exit, False to not """
  def __init__(self, dataframe: dfl, system: int, pos_direction: bool, date: Optional[datetime.date] = None):
    self.dataframe = dataframe
    self.days = 10 if system == 1 else 20
    self.pos_direction = pos_direction
    self.date = date

    self.exit = self.get_exit_decision()

  def get_exit_decision(self) -> bool:
    """ return the an exit decision """
    breakout_tuple = getbreakouts(dataframe=self.dataframe, days=self.days, date=self.date, include_current_extrema=True)
    breakout_tuple = [float(i) for i in breakout_tuple]

    if self.pos_direction is True: # long pos 
      try:
        if breakout_tuple[3] <= breakout_tuple[1]: # if short breakout
          return True
      except IndexError:
        if breakout_tuple[2] <= breakout_tuple[1]: # if short breakout
          return True

    elif self.pos_direction is False: # short pos
      if breakout_tuple[2] >= breakout_tuple[0]: # if long breakout
        return True        
    
    return False