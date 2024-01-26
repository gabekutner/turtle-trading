#!/usr/bin/env python
# -*- coding: utf8 -*-
""" The underlying volatility of an asset. """
import warnings
import datetime
import pandas as pd
from typing import Optional

from turtle_trading._data.dataframe_loader import DataFrameLoader as dfl
from turtle_trading._config.utils import reset_and_reverse

""" ignore Pandas Future Warning and SettingWithCopyWarnings """
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)


def getn(dataframe: dfl, date: Optional[datetime.date] = None):
  """A shortcut function for class: N.
  
  :param dataframe: A DataFrameLoader object.
  :param date: Optional, a datetime.date object.

  :returns: N of an asset in the given time date.
  """
  dataframe.reset()
  return N(dataframe, date).n


class N:
  """This class represents the process for calculating N.
  
  :param dataframe: A DataFrameLoader object.
  :param date: Optional, a datetime.date object.
  """
  def __init__(self, dataframe: dfl, date: Optional[datetime.date] = None):
    self.dataframe = dataframe
    self.date = date

    self.type = dataframe.type

    # Private
    self._edit_dataframe() # converted to dataframe
    self._append_new_columns()

    # Public
    self.pdn = self.get_pdn()
    self.n = self.get_n()


  def _edit_dataframe(self) -> pd.DataFrame:
    """ Configure dataframe for calculating N. """
    self.dataframe = reset_and_reverse(self.dataframe)
    self.dataframe.edit_columns(['low', 'high', 'close'])

    if not self.date:
      self.dataframe = self.dataframe.dataframe.head(20)
      return self.dataframe
    
    self.dataframe = self.dataframe.dataframe[self.date:].head(20)
    return self.dataframe


  def _append_new_columns(self) -> pd.DataFrame:
    """ Create previous close and true range columns. """
    self.dataframe['previous_close'] = self.dataframe['close'].shift(-1)
    self.dataframe['true_range'] = 0
  
    for index, row in enumerate(self.dataframe.iterrows()):
      
      # Set the last 'previous_close' to 0, otherwise will raise NoneType error
      if isinstance(row[1]['previous_close'], type(None)):
        row[1]['previous_close'] = 0
        
      maximum = max(
        row[1]['high'] - row[1]['low'], row[1]['high'] - row[1]['previous_close'], row[1]['previous_close'] - row[1]['low']
      ) 

      self.dataframe.iloc[index, self.dataframe.columns.get_loc('true_range')] = maximum


  def get_pdn(self) -> float:
    """ Calculate the previous day's N. """
    return sum(self.dataframe['true_range'][1:]) / 20
  

  def get_n(self) -> float:
    """ Calculate N. """
    return round(((19 * self.pdn + self.dataframe['true_range'][-1]) / 20), 4)
  

  def check_answer(self):
    """ Prints to console proof of answer. """
    # later ..
    print(self.dataframe)