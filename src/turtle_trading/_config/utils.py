#!/usr/bin/env python
# -*- coding: utf8 -*-
""" package wide utility functions """
import pytz
import datetime


def is_market_open(dt: datetime.datetime) -> bool:
  """ get market status """
  dt = dt.astimezone(pytz.timezone("America/New_York"))
  return 0 <= dt.weekday() <= 4 and 9*60+30 <= dt.hour*60+dt.minute <= 16*60

def reset_and_reverse(df):
  """ reset and reverse DataFrameLoader obj """
  df.reset()
  df.reverse()
  return df