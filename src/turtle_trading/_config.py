#!/usr/bin/env
# -*- coding: UTF8 -*-
""" The _config module holds package-wide configurables. """
import warnings
from typing import Union, Literal

# Warning Class
class UnitsWarning(Warning):
  """ A warning for any of the Markets Exceptions. """


warning_mode = "warn" # default value of the 'warning_mode' configuration setting
warning_type = Union[Literal["warn"], Literal[None]]
warnings.simplefilter(action="always", category=UnitsWarning)

def warning_assignment(warning_mode: warning_type = warning_mode, message: str = f"MarketsException"):
  if isinstance(warning_mode, type(None)):
    return warnings.simplefilter(action="ignore", category=UnitsWarning)

  return warnings.warn(message, UnitsWarning)