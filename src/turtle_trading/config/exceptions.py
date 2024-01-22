#!/usr/bin/env python
# -*- coding: utf8 -*-
""" package wide exception related functions """


def arg_equals(arg: str, values: tuple):
  """  """
  if arg in values:
    raise ValueError(f"@param `{arg}` should equal to one of {values}.")