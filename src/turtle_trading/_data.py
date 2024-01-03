#!/usr/bin/env python
# -*- coding: utf8 -*- 
""" A module for retrieving asset information. 
Takes a ticker symbol and the asset type and returns the necessary data.

@param -  symbol : str 

"""
from typing import Any
import pandas as pd

from yahoo_fin.stock_info import get_data


class SymbolNotFound(Exception):
  """ If symbol does not exist. """


class DataFrameClass:
  """This class represents the base class for getting stock information.

  Args:
    asset: An asset's symbol.
  """
  def __init__(self, asset: str, *args, **kwargs) -> None:
    self.asset = asset
    self.dataframe = self.get_dataframe(*args, **kwargs)

  def get_dataframe(self, start_date: Any | None = None, end_date: Any | None = None, index_as_date: bool = True, interval: str = "1d", reverse: bool = False) -> pd.DataFrame:
    """Get the asset's dataframe.

    Args:
      start_date: Date to start
      end_date: Date to end
      index_as_date: Indices as dates or numbers, default is dates
      interval: Must be.. "1d", "1wk", "1mo", "1m"
    """
    try:
      dataframe = get_data(self.asset, start_date, end_date, index_as_date, interval)
    except AssertionError:
      raise SymbolNotFound

    if reverse is True: 
      return dataframe.loc[::-1] # reverse
    
    return dataframe