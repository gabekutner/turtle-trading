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
import sys
from pathlib import Path

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from position_sizing.position_sizing import SingleDirectionException

def add_units(N: float, breakout: float, units: int = 4):
  """Returns the next four units.

  COMMENT: The maximum 
  
  Args:
    N: The 'N' at the breakout price.
    breakout: The breakout price.
    units: Optional, how many units to add. 
  """
  if units > 4:
    raise SingleDirectionException

  _units = [breakout]
  for i in range(units-1):
    to_be = _units[i] + 0.5 * (N)
    _units.append(to_be)

  return _units