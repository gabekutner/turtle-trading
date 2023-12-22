#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Stop Placement
The Turtles placed their stops based on position risk. No trade could incur more than
2% risk.

Since 1 N of price movement represented 1% of Account Equity, the maximum stop
that would allow 2% risk would be 2 N of price movement. Turtle stops were set at 2
N below the entry for long positions, and 2 N above the entry for short positions.

In order to keep total position risk at a minimum, if additional units were added, the
stops for earlier units were raised by ½ N. This generally meant that all the stops for
the entire position would be placed at 2 N from the most recently added unit.
However, in cases where later units were placed at larger spacing either because of fast
markets causing skid, or because of opening gaps, there would be differences in the
stops.

For example:
Crude Oil
N = 1.20
55 day breakout = 28.30

              Entry Price   Stop
First Unit    28.30         25.90

              Entry Price   Stop
First Unit    28.30         26.50
Second Unit   28.90         26.50

              Entry Price   Stop
First Unit    28.30         27.10
Second Unit   28.90         27.10
Third Unit    29.50         27.10

              Entry Price   Stop
First Unit    28.30         27.70
Second Unit   28.90         27.70
Third Unit    29.50         27.70
Fourth Unit   30.10         27.70

Case where fourth unit was added at a higher price because the market opened gapping
up to 30.80:
              Entry Price   Stop
First Unit    28.30         27.70
Second Unit   28.90         27.70
Third Unit    29.50         27.70
Fourth Unit   30.80         28.40
"""
import pandas as pd

VERSIONS = ["reg", "whipsaw"]



def getstop(n: float,  entries: list[float], mode: str = "reg"):
  """Get Stop.

  Args: 
    n: 
    entries: A list of entry prices. Expected that they are in order.
    mode: 
  """
  return Stop(n=n, entries=entries, mode=mode)


class Stop:
  """Represents units and their corresponding stops.

  Args:
    n:
    entries: A list of entry prices. Expected that they are in order.
    mode:
  """
  def __init__(self, n: float, entries: list[float], mode: str = "reg"):
    num_of_units = len(entries)
    risk = 2.0 * n
    self.stops = self.stop_placement(entries=entries, risk=risk)


  def stop_placement(self, entries: list[float], risk: float):
    """
    """
    






# E.g. usage
if __name__ == "__main__":

  n = 1.20 # N @ $28.30 - the 55 day breakout
  standard = [28.30, 28.90, 29.50, 30.10]
  gap = [28.30, 28.90, 29.50, 30.80]

  first = getstop(n=n, entries=standard)

  second = getstop(n=n, entries=gap)