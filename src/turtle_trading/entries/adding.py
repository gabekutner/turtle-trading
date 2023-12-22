# #!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Adding Units
Turtles entered single Unit long positions at the breakouts and added to those
positions at 1/2 N intervals following their initial entry. This 1/2 N interval was based on 
the actual fill price of the previous order. So if an initial breakout order slipped by 1/2 N, 
then the new order would be 1 full N past the breakout to account for the 1/2 N
slippage, plus the normal 1/2 N unit add interval.

This would continue right up to the maximum permitted number of units. If the
market moved quickly enough it was possible to add the maximum four Units in a 
single day.

Example: 
Gold
N = 2.50
55 day breakout = 310

First Unit added    310.00
Second Unit         310.00 + 1/2 (2.50) or 311.25
Third Unit          311.25 + 1/2 (2.50) or 312.50
Fourth Unit         312.50 + 1/2 (2.50) or 313.75

Crude Oil
N = 1.20
55 day breakout = 28.30

First Unit added    28.30
Second Unit         28.30 + 1/2 (1.20) or 28.90
Third Unit          28.90 + 1/2 (1.20) or 29.50
Fourth Unit         29.50 + 1/2 (1.20) or 30.10
"""

def addunits(N: float, breakout: float, units: int = 4):
  """Returns the next four units.

  COMMENT: The maximum units allowed by the Turtle Trading system on one position is 4.

  Args:
    N: The 'N' at the breakout price.
    breakout: The breakout price.
    units: Optional, how many units to add. 
  """
  _units = [breakout]
  for i in range(units-1):
    _units.append(_units[i] + 0.5 * (N))

  return _units