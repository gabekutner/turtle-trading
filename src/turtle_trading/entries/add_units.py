#!/usr/bin/env python
# -*- coding: utf8 -*-
""" adding units """
from typing import Optional

def addunits(breakout: float, n: float, units_num: Optional[int] = 4):
  """ adding units to existing positions """
  units = [breakout]
  for i in range(units_num-1):
    units.append(round((units[i] + 0.5 * n), 4))

  return units