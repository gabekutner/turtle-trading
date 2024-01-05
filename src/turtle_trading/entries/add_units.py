#!/usr/bin/env python
# -*- coding: utf8 -*-
""" adding units """
from typing import Optional

def addunits(breakout: float, n: float, unit_list: Optional[int] = 4):
  """ adding units to existing positions """
  units = [breakout]
  for i in range(unit_list-1):
    units.append(round((units[i] + 0.5 * n), 4))

  return units