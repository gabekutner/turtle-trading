#!/usr/bin/env python
# -*- coding: utf8 -*-
"""  """
import datetime
import pandas as pd
from typing import Union, Literal

from turtle_trading.dataframe_loader import DataFrameLoader


def price_against_position(dataframe: DataFrameLoader, day: int, date_entered: datetime.date):
  """  """
  dataframe.reset()

  dataframe.start_at(date_entered)

  for index, row in enumerate(dataframe.dataframe.iterrows()):
    if index+1 == day:
      return False
    