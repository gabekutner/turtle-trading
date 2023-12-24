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



def getstop(n: float,  entries: list[float], stand_devs: float = 2.00, mode: str = "reg"):
  """Get the Stop Prices.

  Args: 
    n: The N of the first entry.
    entries: A list of entry prices. Use addunits function from entries module.
    mode: The regular stop strategy or the whipsaw.
  """
  return Stop(n=n, entries=entries, stand_devs=stand_devs, mode=mode)


class Stop:
  """Represents units and their corresponding stops.

  Args:
    n:
    entries: A list of entry prices. Expected that they are in order.
    mode:
  """
  def __init__(self, n: float, entries: list[float], stand_devs: float = 2.00, mode: str = "reg"):
    risk = stand_devs * n

    if mode == "reg":
      self.stop = self.stop_placement(entries=entries, risk=risk, n=n)

  def stop_placement(self, entries: list[float], risk: float, n: float):
    """

    Args:
      entries:
      risk: 
    """
    diff = round(.5 * n, 2)
    print(diff)

    # the differences between all the entries
    check = [round(elem, 2) for elem in [j-i for i, j in zip(entries[:-1], entries[1:])]] 
    print(check)

    if all(i == diff for i in check): # if no gaps
      num_of_units = len(entries)
      stop = entries[num_of_units-1] - risk
      return stop
    
    else: # if a gap(s)
      
      # find gapped numbers
      gapped_entries = [i for i in check if i != diff]
      # print(gapped_entries)
      
      # get the indices for all gapped numbers
      indices: list = []
      for i in gapped_entries:
        ele = check.index(i)+1
        indices.append(ele)
      
      # now, get the stops
      stops: list = []
      for index, entry in enumerate(entries):
        if index in indices:
          pass

        # fucking this is annoying, I don't wanna do it rn moving on to exits
        



      





     
    

"""
Alternate Stop Strategy - The Whipsaw

The Turtles were told of an alternate stop strategy that resulted in better profitability,
but that was harder to execute because it incurred many more losses, which resulted in 
a lower win/loss ratio. This strategy was called the Whipsaw.

Instead of taking a 2% risk on each trade, the stops were placed at 1/2 N for 1/2%
account risk. If a given Unit was stopped out, the Unit would be re-entered if the
market reached the original entry price. A few Turtles traded this method with good
success.

The Whipsaw also had the added benefit of not requiring the movement of stops for
earlier Units as new Units were added, since the total risk would never exced 2% at 
the maximum four Units.

For example, using Whipsaw stops, the Crude Oil entry stops would be:

Crude Oil
N = 1.20
55 day breakout = 28.30

              Entry Price   Stop
First Unit    28.30         27.70

              Entry Price   Stop
First Unit    28.30         27.70
Second Unit   28.90         28.30

              Entry Price   Stop
First Unit    28.30         27.70
Second Unit   28.90         28.30
Third Unit    29.50         28.90

              Entry Price   Stop
First Unit    28.30         27.70
Second Unit   28.90         28.30
Third Unit    29.50         28.90
Fourth Unit   30.10         29.50
"""




# E.g. usage
if __name__ == "__main__":

  n = 1.20 # N @ $28.30 - the 55 day breakout
  standard = [28.30, 28.90, 29.50, 30.10]
  gap = [28.30, 28.90, 29.50, 30.80]

  gap_ = [28.30, 28.90, 30.80, 31.40, 35.50]

  stop = getstop(n, gap_)
  print(stop.stop)