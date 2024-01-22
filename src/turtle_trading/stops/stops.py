#!/usr/bin/env python
# -*- coding: utf8 -*-
""" stop placement """
from itertools import cycle

from turtle_trading.config.exceptions import arg_equals


def getstops(stop_system: str, unit_list: list[float], n: float):
  """ shortcut function for class: Stop """
  arg_equals("stop_system", ("regular", "whipsaw"))
  return Stop(stop_system=stop_system, unit_list=unit_list, n=n).stops


class Stop:
  """ this class represents the process of calculating the stops for all units of position """
  def __init__(self, stop_system: str, unit_list: list[float], n: float):
    self.stop_system = stop_system
    self.unit_list = unit_list
    self.n = n

    self.half_n = .5 * n
    self.two_n = 2 * n
    self.third_n = 1.5 * n

    self.stops = self.check_system()

  def check_system(self):
    """ which system to use: whipsaw or regular """
    if self.stop_system == "regular":
      return self.regular_stops()

    if self.stop_system == "whipsaw":
      return self.whipsaw_stops()

  def whipsaw_stops(self):
    """ the whipsaw stop strategy """
    return [round(unit - self.half_n, 2) for unit in self.unit_list]
  

  def regular_stops(self):
    """ the regular stop strategy """
    # find difference between units
    diff_between_units = [round(elem, 2) for elem in [j-i for i, j in zip(self.unit_list[:-1], self.unit_list[1:])]]

    # if the difference between units for all units is the same, return the same stop per unit
    if all(i == diff_between_units[0] for i in diff_between_units):
      return [round(self.unit_list[-1] - self.two_n, 2) for i in range(len(self.unit_list))]
    
    if not all(i == diff_between_units[0] for i in diff_between_units):
      licycle = cycle(reversed(self.unit_list))
      nextelem = next(licycle)
      stops = []
      met = 0

      for index, unit in enumerate(reversed(self.unit_list)):
        
        if index+1 == len(self.unit_list): 
          stops.append(stops[-1]) 
          break

        thiselem, nextelem = nextelem, next(licycle)

        if round(thiselem - nextelem, 2) != self.half_n:
          stops.append(round(thiselem - self.two_n, 2))

        elif round(thiselem - nextelem, 2) == self.half_n and met == 0:
          met = met+1
          stops.append(round(thiselem - self.third_n, 2))
          
        elif round(thiselem - nextelem, 2) == self.half_n and met != 0:
          stops.append(stops[-1])

      return stops[::-1]