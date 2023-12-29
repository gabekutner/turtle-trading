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


futures = [
  # CBOT
  "", # 30 Year U.S. Treasury Bond
  "ZN=F", # 10 Year U.S. Treasury Note

  # CSCE
  "KC=F", # Coffee
  "CC=F", # Cocoa
  "SB=F", # Sugar
  "CT=F", # Cotton

  # CME
  "6S=F", # Swiss Franc
  "", # Deutschmark
  "", # British Pound
  "", # French Franc
  "6J=F", # Japanese Yen
  "6C=F", # Canadian Dollar
  "", # S&P 500 Stock Index
  "", # Eurodollar
  "", # 90 Day U.S. Treasury Bill

  # Comex
  "GC=F", # Gold
  "SI=F", # Silver
  "HG=F", # Copper

  # NYMEX
  "CL=F", # Crude Oil
  "HO=F", # Heating Oil
  "RB=F" # Unleaded Gas
]