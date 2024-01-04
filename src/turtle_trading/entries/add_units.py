#!/usr/bin/env python
# -*- coding: utf8 -*-
"""  """
from typing import Optional

def addunits(breakout: float, n: float, units: Optional[int] = 4):
  """ adding units to existing positions """
  
  _units = [breakout]
  for i in range(units-1):
    _units.append(round((_units[i] + 0.5 * n), 4))

  return _units