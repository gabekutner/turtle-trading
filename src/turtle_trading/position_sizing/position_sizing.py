#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Volatility - The Meaning of N
The Turtles used a concept that Richard Dennis and Bill Eckhardt called N to 
represent the underlying volatility of a particular market.

N is simply the 20-day exponential moving average of the True Range, which is now
more commonly known as the ATR. Conceptually, N represents the average range in
price movement that a particular market makes in a single day, accounting for opening
gaps. N was measured in the same points as the underlying contract.

To compute the daily true range:
  True Range = Maximum(H-L, H-PDC, PDC-L)
where:
  H - Current High
  L - Current Low
  PDC - Previous Day's Close

To compute N use the following formula:
  N = (19 * PDN + TR) / 20
where:
  PDN - Previous Day's N
  TR - Current Day's True Range

Since this formula requires a previous day's N value, you must start with a 20-day
simple average of the True Range for the initial calculation.

Dollar Volatility Adjustment
The first step in determining the position size was to determine the dollar volatility
represented by the underlying market's price volatility (defined by its N).

This sounds more complicated than it is. It is determined using the simple formula:
  Dollar Volitility = N * Dollars per Point

Volatility Adjusted Position Units
The Turtles built positions in pieces which we called Units. Units were sized so that 1
N represented 1% of the account equity.

Thus, a unit for a given market or commodity can be calculated using the following
formula:
  Unit = 1% of Account / Market Dollar Volatility
  or 
  Unit = 1% of Account / N * Dollars per Point

...

Units as a measure of Risk
The limits were:
Level       Type                            Maximum Units
1           Single Market                   4 Units
2           Closely Correlated Markets      6 Units
3           Loosely Correlated Markets      10 Units
4           Single Direction                12 Units

Single Markets - A maximum of four Units per market.

Closely Correlated Markets - For markets that were closely correlated there could be
a maximum of 6 Units in one particular direction (i.e.6 long units or 6 short units).
Closely correlated markets include: heating oil and crude oil; gold and silver; Swiss
franc and Deutschmark; TBill and Eurodollar, etc.

Loosely Correlated Markets - For loosely correlated markets, there could be a
maximum of 10 Units in one particular direction. Loosely correlated markets included:
gold and copper; silver and copper, and many grain combinations that the Turtles did
not trade because of positions limits.

Single Direction - The maximum number of total Units in one direction long or short
was 12 Units. Thus, one could theoretically have had 12 Units long and 12 Units short
at the same time.
"""
import math
import pandas as pd
from types import NoneType

from yahoo_fin.stock_info import get_data

""" ignore Pandas Future Warning """
pd.options.mode.chained_assignment = None  # default='warn'


class SingleMarketsException(Exception):
  """ Single Markets - A maximum of 4 Units per market. """


class CloselyCorrelatedMarketsException(Exception):
  """ Closely Correlated Markets - A maximum of 6 Units in one particular direction. """


class LooselyCorrelatedMarketsException(Exception):
  """ Loosely Correlated Markets - A maximum of 10 Units in one particular direction. """


class SingleDirectionException(Exception):
  """ Single Direction - A maximum of 12 Units in one direction, long or short.  """


def getn(asset: str, dataframe: pd.DataFrame = None):
  """Calculate N.

  Args:
    asset: An asset's symbol.
    dataframe: A pandas dataframe, if no query is required.
  """
  return N(asset=asset, dataframe=dataframe).n


def getunit(asset: str, n: float, account_size: float):
  """Get Unit Size.

  Args:
    asset: An asset's symbol.
    n: An asset's underlying volatility.
  """
  return Unit(asset=asset, n=n, account_size=account_size)



class N:
  """This class represents an asset's underlying volatility.

  Args:
    asset: An asset's symbol.
    dataframe: A pandas dataframe, if no query is required.
  """
  def __init__(self, asset: str, dataframe: pd.DataFrame = None):
    self.dataframe = self._dataframe(asset, dataframe)
    self.true_range = self._true_range(self.dataframe)
    self.pdn = self._pdn(self.true_range)
    self.n = self._n(self.pdn, self.true_range)


  def _dataframe(self, asset: str, dataframe: pd.DataFrame = None) -> pd.DataFrame:
    """Get the asset's pandas dataframe. 

    Args:
      asset: An asset's symbol.
      dataframe: A pandas dataframe, if no query is required.
    """
    if dataframe is None:
      dataframe = get_data(ticker=asset, interval="1d")[["low", "high", "close"]].tail(21).astype(object)
    
    else:
      dataframe = dataframe[["low", "high", "close"]].astype(object)

    dataframe["previous_close"] = dataframe["close"].shift(1)
    dataframe["true_range"] = 0
    return dataframe


  def _true_range(self, dataframe: pd.DataFrame) -> pd.Series:
    """Create and return the true range column.

    Args:
      dataframe: The asset's dataframe.
    """
    for index, row in enumerate(dataframe.iterrows()):
      # Set last previous close to 0, otherwise will NoneType error
      if isinstance(row[1]["previous_close"], NoneType):
        row[1]["previous_close"] = 0

      maximum = max(row[1]["high"] - row[1]["low"], row[1]["high"] - row[1]["previous_close"], row[1]["previous_close"] - row[1]["low"])
      dataframe.iloc[index, dataframe.columns.get_loc('true_range')] = maximum

    return dataframe["true_range"]
  

  def _pdn(self, true_range: pd.Series) -> float:
    """Get the previous day's N. 

    Args:
      true_range: The true range column. 
    """
    return sum(true_range[1:]) / 20
  

  def _n(self, pdn: float, true_range: pd.Series) -> float:
    """Get 'N'.
    
    Args:
      pdn: The previous day's 'N'.
      true_range: The true range column. 
    """
    return (19 * pdn + true_range[-1]) / 20
  
  

class Unit:
  """This class represents an asset's units size.

  Args:
    asset: An asset's symbol.
    N: An asset's underlying volatility.
  """
  def __init__(self, asset: str, n: float, account_size: float):
    self.dollar_volatility = self._dollar_volatility(asset, n)
    self.unit = self._unit_size(self.dollar_volatility, account_size)


  def _dollar_volatility(self, asset: str, n: float) -> float:
    """Get the market dollar volatility of an asset.

    Args:
      asset: An asset's symbol.
    """
    # get the live price
    dataframe = get_data(ticker=asset, end_date=pd.Timestamp.today() + pd.DateOffset(10))
    pps = dataframe.close[-1]

    # multiply N and the live price
    return n * pps
  

  def _unit_size(self, dollar_volatility, account_size):
    """Get the volatility adjusted unit size.
    
    Args:
      dollar_volatility: The market dollar volatility of an asset.
    """
    return math.trunc((0.01 * account_size) / dollar_volatility)