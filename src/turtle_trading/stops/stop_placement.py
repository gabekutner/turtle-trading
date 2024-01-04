#!/usr/bin/env python
# -*- coding: utf8 -*-
""" stop placement """
from itertools import cycle
from typing import Literal, Union


def getstops(unit_list: list[float], n: float, stop_system: Union[Literal['regular'], Literal['whipsaw']] = "regular"):
  """ shortcut function for functions: get_whipsaw_stops and get_stops """
  if stop_system == 'regular':
    return get_stops(unit_list, n)
  
  if stop_system == 'whipsaw':
    return get_whipsaw_stops(unit_list, n)


def get_stops(unit_list: list[float], n: float):
  """ regular stop strategy """
  two_n = 2 * n
  half_n = .5 * n
  third_n = 1.5 * n

  diff_between_units = [round(elem, 2) for elem in [j-i for i, j in zip(unit_list[:-1], unit_list[1:])]]  # find difference between units
  
  if all(i == diff_between_units[0] for i in diff_between_units):
    return [round(unit_list[-1] - two_n, 2) for i in range(len(unit_list))]
  
  if not all(i == diff_between_units[0] for i in diff_between_units):

    licycle = cycle(reversed(unit_list))
    nextelem = next(licycle)
    stops = []
    met = 0

    for index, unit in enumerate(reversed(unit_list)):
      
      if index+1 == len(unit_list): 
        stops.append(stops[-1]) 
        break

      thiselem, nextelem = nextelem, next(licycle)

      if round(thiselem - nextelem, 2) != half_n:
        stops.append(round(thiselem - two_n, 2))

      elif round(thiselem - nextelem, 2) == half_n and met == 0:
        met = met+1
        stops.append(round(thiselem - third_n, 2))
        
      elif round(thiselem - nextelem, 2) == half_n and met != 0:
        stops.append(stops[-1])

        
    return stops[::-1]
  

def get_whipsaw_stops(unit_list: list[float], n: float):
  """ whipsaw stop strategy """
  half_n = .5 * n
  return [round(unit - half_n, 2) for unit in unit_list]