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
from itertools import groupby
from collections.abc import Iterable
from collections import deque 


def all_equal(iterable: Iterable): 
  """ helper method """
  g = groupby(iterable)
  return next(g, True) and not next(g, False)

def stop_placement(n: float, units: list[float]):
  """
   
  Args:
    n: 
    units:
  """
  _two_n = 2 * n
  _i = round(abs(units[0] - units[1]), 2)

  diff_between_units = [round(elem, 2) for elem in [j-i for i, j in zip(units[:-1], units[1:])]]  # find difference between units
  res = all_equal(diff_between_units) # check if all the same
  
  stops = deque([])
  if not res:

    sentinel = units[0]
    iterable = iter(units[::-1])
    
    for i, ele in enumerate(iterable):
      
      if ele - iterable[i+1] != _i:
        pass
      
    #   if isinstance(next(iterable), type(None)):
    #     print('nigga')

    # for unit in enumerate(units[::-1]):
      
    #   if 
      
    #   if unit - units[i+1] != _i:
    #     except IndexError:
      
    #     print('ra')

    #     print(f"unit: {unit}")
    #     print(f"next: {units[i-1]}")
    #     stops.append(round(unit - _two_n, 2))
    #     continue
      
    #   stops.append(round(unit - _two_n, 2))
      
    # return stops.reverse()

  return round(units[-1] - _two_n, 2)
  
  


 

if __name__ == "__main__":
  
  n = 1.20
#   breakout = 28.30
  units = [28.30, 28.90, 29.50, 30.80]

  stop = stop_placement(n, units)
  print(stop)