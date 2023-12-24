#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

System 1 - A shorter-term system based on a 20-day breakout.

System 2 - A simpler long-term system based on a 55-day breakout.

Breakouts
A breakout is defined as the price exceeding the high or low of a particular number of
days. Thus a 20-day breakout would be defined as exceeding the high or low of the
preceding 20 days.

Turtles always traded at the breakout when it was exceeded during the day, and did not
wait until the daily close or the open of the following day. In the case of opening gaps,
the Turtles would enter positions on the open if a market opened through the price of
the breakout.

System 1 Entry - Turtles entered positions when the price exceeded by a single tick the
high or low of the preceding 20 days. If the price exceeded the 20-day high, then the
Turtles would buy one Unit to initiate a long position in the corresponding
commodity. If the price dropped one tick below the low of the last 20-days, the Turtles
would sell one Unit to initiate a short position.

System 1 breakout entry signals would be ignored if the last breakout would have
resulted in a winning trade. NOTE: For the purposes of this test, the last breakout was
considered the last breakout in the particular commodity irrespective of whether or not
that particular breakout was actually taken, or was skipped because of this rule. This
breakout would be considered a losing breakout if the price subsequent to the date of
the breakout moved 2N against the position before a profitable 10-day exit occurred.

The direction of the last breakout was irrelevant to this rule. Thus, a losing long
breakout or a losing short breakout would enable the subsequent new breakout to be
taken as a valid entry, regardless of its direction (long or short).

However, in the event that a System 1 entry breakout was skipped because the
previous trade had been a winner, an entry would be made at the 55-day breakout to
avoid missing major moves. This 55-day breakout was considered the Failsafe
Breakout point.

At any given point, if you were out of the market, there would always be some price
which would trigger a short entry and another different and higher price which would
trigger a long entry. If the last breakout was a loser, then the entry signal would be
closer to the current price (i.e. the 20 day breakout), than if it had been a winner, in
which case the entry signal would likely be farther away, at the 55 day breakout.

System 2 Entry - Entered when the price exceeded by a single tick the high or low of
the preceding 55 days. If the price exceeded the 55 day high, then the Turtles would
buy one Unit to initiate a long position in the corresponding commodity. If the price
dropped one tick below the low of the last 55 days, the Turtles would sell one Unit to
initiate a short position.

All breakouts for System 2 would be taken whether the previous breakout had been a
winner or not.
"""
import sys
import pandas as pd
from pathlib import Path

""" Avoid import errors while importing 'getn' function """
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from position_sizing.position_sizing import getn


def getsignal(price: float, dataframe: pd.DataFrame, system: int) -> bool:
  """Get an entry signal.

  COMMENT(s): 
    Consider removing dataframe arg and doing that inside function.
    Move from function to class?

  Args:
    price: The asset's current price.
    dataframe: The asset's get_data() dataframe.
    system: Which system to use, 1 or 2.
  """
  if system not in (1, 2):
    raise AssertionError("System must be of of 1 or 2.")
  
  # reverse the dataframe
  dataframe = dataframe.loc[::-1]

  if system == 1:
    return system_one(price=price, dataframe=dataframe)
  elif system == 2:
    return system_two(price=price, dataframe=dataframe) 


def breakout(price: float, dataframe: pd.DataFrame, days: int) -> bool:
  """Determine if the price is a breakout price.
  
  A breakout is defined as the price exceeding the high or low of a particular number of
  days. Thus a 20-day breakout would be defined as exceeding the high or low of the
  preceding 20 days.

  Turtles always traded at the breakout when it was exceeded during the day, and did not
  wait until the daily close or the open of the following day. In the case of opening gaps,
  the Turtles would enter positions on the open if a market opened through the price of
  the breakout.

  Args: 
    price: The asset's current price.
    dataframe: The asset's get_data() dataframe.
    days: The number of days.
    
  Returns:
    True if long breakout, False if short breakout, None if no breakout.
  """
  if all(_ <= price for _ in dataframe.head(days+1)["high"].tolist()): # if all the highs are lower than the price
    return True # long
  
  elif all(_ >= price for _ in dataframe.head(days+1)["low"].tolist()): # if all the lows are higher than the price
    return False # short

  return None # no breakout
  

def last_breakout(dataframe: pd.DataFrame, stand_devs: float = 2.0, days: int = 20, skip: int = 1):
  """Get the last breakout and determine if it was a losing or winning position.

  System 1 breakout entry signals would be ignored if the last breakout would have
  resulted in a winning trade. NOTE: For the purposes of this test, the last breakout was
  considered the last breakout in the particular commodity irrespective of whether or not 
  that particular breakout was actually taken, or was skipped because of this rule. This
  breakout would be considered a losing breakout if the price subsequent to the date of
  the breakout moved 2N against the position before a profitable 10-day exit occurred.

  Args:
    dataframe: An asset's full dataframe.
    n: 'N' of the asset at the price. 
    stand_devs: The number of standard deviations.
    days: The number of days.
    skip: How many breakouts to skip. 

  Returns:
    True if the last breakout was a winning position, False if losing.
  """
  # 1: Find the last breakout.
  loc: int # the location of the last breakout
  direction: bool # long or short 
  n_dataframe: pd.DataFrame

  for index, row in enumerate(dataframe.iterrows()):
    last_twenty = dataframe.iloc[index+1: index+days+1] # the last twenty days
    _breakout = breakout(price=row[1]["close"], dataframe=last_twenty, days=20) # is the first row a breakout
 
    if isinstance(_breakout, bool) and index > skip: # if a breakout
      loc, direction, n_dataframe = index, True if _breakout is True else False, last_twenty
      break

  # 2: Find 'N' of the last breakout.
  N = getn(asset="", dataframe=n_dataframe)
  
  # 3: Determine if winning or losing position.
  breakout_price = dataframe.iloc[loc]["close"] # the last breakout price

  for index, row in enumerate(dataframe.iloc[:loc+1].iloc[::-1].iterrows()):  
    # if the difference between the close and breakout price is greater than num * n, return False
    if index == 10: break

    if direction: # if a long position, True
      if row[1]["close"] - breakout_price >= stand_devs * N:
        return False

    if not direction: # if a short position, False
      if row[1]["close"] - breakout_price <= -(stand_devs * N):
        return False
  
  # if False not returned, position is winning.. return True
  return True


def system_one(price: float, dataframe: pd.DataFrame) -> bool or None or tuple[bool, int]:
  """System One Entry

  Turtles entered positions when the price exceeded by a single tick the
  high or low of the preceding 20 days. If the price exceeded the 20-day high, then the
  Turtles would buy one Unit to initiate a long position in the corresponding
  commodity. If the price dropped one tick below the low of the last 20-days, the Turtles
  would sell one Unit to initiate a short position.

  System 1 breakout entry signals would be ignored if the last breakout would have
  resulted in a winning trade. NOTE: For the purposes of this test, the last breakout was
  considered the last breakout in the particular commodity irrespective of whether or not
  that particular breakout was actually taken, or was skipped because of this rule. This
  breakout would be considered a losing breakout if the price subsequent to the date of
  the breakout moved 2N against the position before a profitable 10-day exit occurred.

  The direction of the last breakout was irrelevant to this rule. Thus, a losing long
  breakout or a losing short breakout would enable the subsequent new breakout to be
  taken as a valid entry, regardless of its direction (long or short).

  However, in the event that a System 1 entry breakout was skipped because the
  previous trade had been a winner, an entry would be made at the 55-day breakout to
  avoid missing major moves. This 55-day breakout was considered the Failsafe
  Breakout point.

  Args:
    price: The asset's current price.
    dataframe: The asset's full dataframe.

  Returns: 
    True if long breakout, False if short breakout, None if no breakout.
  """
  _breakout = breakout(price=price, dataframe=dataframe, days=20) # is the current price a 20-day breakout
  if isinstance(_breakout, bool): # if a breakout...
    previous_breakout = last_breakout(dataframe=dataframe, stand_devs=2.00) # get last breakout
    if previous_breakout: # if last breakout was losing, continue 
      return _breakout # true or false
    elif not previous_breakout: # if last breakout was winning, ignore
      if isinstance(breakout(price=price, dataframe=dataframe, days=55), bool): # if this breakout is a 55 day breakout
        return (_breakout, 55)


def system_two(price: float, dataframe: pd.DataFrame) -> bool or None:
  """System Two Entry

  Entered when the price exceeded by a single tick the high or low of
  the preceding 55 days. If the price exceeded the 55 day high, then the Turtles would
  buy one Unit to initiate a long position in the corresponding commodity. If the price
  dropped one tick below the low of the last 55 days, the Turtles would sell one Unit to
  initiate a short position.

  All breakouts for System 2 would be taken whether the previous breakout had been a
  winner or not.

  Args:
    price: The asset's current price.
    dataframe: The asset's full dataframe.

  Returns:
    True if long breakout, False if short breakout, None if no breakout.
  """
  _breakout = breakout(price=price, dataframe=dataframe, days=55) # is the current price is a 55-day breakout
  if isinstance(_breakout, bool): # if a breakout...
    return _breakout