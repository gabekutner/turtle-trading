#!/usr/bin/env python
# -*- coding: utf8 -*-
""" adding units """
from typing import Optional

def addunits(orig_breakout: float, orig_n: float, number_of_units: Optional[int] = 4):
  """ adding units to existing positions """
  units = [orig_breakout]
  for i in range(number_of_units-1):
    units.append(round((units[i] + 0.5 * orig_n), 4))

  return units