#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Chapter 4, Page 23

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
import pandas as pd

from turtle_trading.position_sizing import getn
from yahoo_fin.stock_info import get_data

SYSTEM = {1: 20, 2: 55}


def getsignal(asset: str, price: float, system: int):
  """Get an entry signal, if there is one.

  Args:
    asset: An asset's symbol.
    price: An asset's price.
    system: System 1 or System 2.

  Returns:
    True if a long breakout, False if a short breakout, None if there's no breakout.
  """
  return Signal(asset=asset, price=price, system=system).result

def get_breakout_prices(asset: str, day: int = 20) -> tuple[float, float]:
  """Find the next breakout price for short and long positions.

  Args:
    asset: An asset's symbol.
    day: 20-day or 55-day breakout.
  """
  return Breakout(asset, day).result


class Breakout:
  """This class represents the process of finding the next breakout prices.

  Args:
    asset: An asset's symbol.
    day: 20-day or 55-day breakout.
  """
  def __init__(self, asset: str, day: int = 20) -> None:
    dataframe = self.get_dataframe(asset, day)
    self.result = self.find_extrema(dataframe)

  def get_dataframe(self, asset: str, day: int = 20):
    """Get the dataframe, reversed, with the `day` being the .head() value.

    Args:
      asset: An asset's symbol.
      day: 20-day or 55-day breakout. 
    """
    dataframe = get_data(asset, interval="1d")
    dataframe = dataframe.loc[::-1] # reverse
    return dataframe.head(day)[["high", "low"]]

  def find_extrema(self, dataframe: pd.DataFrame) -> tuple[float, float]:
    """Find the min and max of the dataframe.
    
    Args:
      dataframe: An asset's pandas dataframe.
    """
    maximum = dataframe["high"].max()
    minimum = dataframe["low"].min()
    return (maximum, minimum)



class Signal:
  """This class represents the process of finding an entry signal, if there is one.
  
  Args:
    asset: An asset's symbol.
    system: System 1 or System 2.
  """
  def __init__(self, asset: str, price: float, system: int) -> None:
    if system not in (1, 2):
      raise AssertionError("System's gotta be 1 or 2.")

    dataframe = self.get_dataframe(asset=asset)
    self.result = self.get_system(system=system, price=price, dataframe=dataframe)

  def get_dataframe(self, asset: str) -> pd.DataFrame:
    """Get the asset's pandas dataframe, reversed.
    
    Args:
      asset: An asset's symbol.
    """
    dataframe = get_data(asset, interval="1d")
    dataframe = dataframe.loc[::-1] # reverse
    return dataframe

  def get_breakout(self, price: float, dataframe: pd.DataFrame, days: int) -> bool or None:
    """Determine if the price is a breakout price.
    
    Args:
      price: The asset's current price.
      dataframe: The asset's get_data() dataframe.
      days: The number of days.

    Returns:
      True if a long breakout, False if a short breakout, None if there's no breakout.
    """
    if all(_ <= price for _ in dataframe.head(days+1)["high"].tolist()): return True
  
    elif all(_ >= price for _ in dataframe.head(days+1)["low"].tolist()): return False 

    else: return None

  def get_last_breakout(self, dataframe: pd.DataFrame, stand_devs: float = 2.0, days: int = 20, skip: int = 1) -> bool:
    """Get the result of the last breakout, winning or losing.
    
    Args:
      dataframe: An asset's full dataframe.
      n: An asset's underlying volatility.
      stand_devs: The number of standard deviations.
      days: The number of days.
      skip: How many breakouts to skip. 

    Returns:
      True if winning position, False if losing position.
    """
    for index, row in enumerate(dataframe.iterrows()):
      last_twenty = dataframe.iloc[index+1: index+days+1]
      _breakout = self.get_breakout(price=row[1]["close"], dataframe=last_twenty, days=20)
  
      if isinstance(_breakout, bool) and index > skip: # if a breakout
        loc, direction, last_twenty_dataframe = index, True if _breakout is True else False, last_twenty
        break

    N = getn(asset="", dataframe=last_twenty_dataframe)
    breakout_price = dataframe.iloc[loc]["close"] # the last breakout price

    for index, row in enumerate(dataframe.iloc[:loc+1].iloc[::-1].iterrows()):  
      if index == 10: break # before a profitable 10-day exit

      if direction: # if a long position
        if row[1]["close"] - breakout_price >= stand_devs * N:
          return False

      if not direction: # if a short position
        if row[1]["close"] - breakout_price <= -(stand_devs * N):
          return False
    
    return True # if not False, return True

  def get_system(self, system: int, price: float, dataframe: pd.DataFrame) -> bool or None:
    """Get the system to use and entry results using that system.
    
    Args:
      system: System 1 or System 2.
    """
    if system == 2:
      breakout = self.get_breakout(price=price, dataframe=dataframe, days=55)
      if isinstance(breakout, bool):
        return breakout
      
    elif system == 1:
      breakout = self.get_breakout(price=price, dataframe=dataframe, days=20)
      if isinstance(breakout, bool):
        
        last_breakout = self.get_last_breakout(dataframe=dataframe) # get last breakout
        if last_breakout: # if winning
          return breakout

        elif not last_breakout: # if losing
          if isinstance(self.get_breakout(price=price, dataframe=dataframe, days=55), bool): # if this breakout is a 55 day breakout
            return (breakout, 55)

    else:
      raise AssertionError("System's gotta be 1 or 2.")