#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Position sizing is one of the most important but least understood components
of any trading system.

The Turtles used a position sizing algorithm that was very advanced for its day,
because it normalized the dollar volatility of a position by adjusting the position size
based on the dollar volatility of the market. This meant that a given position would
tend to move up or down in a given day about the same amount in dollar terms (when
compared to positions in other markets), irrespective of the underlying volatility of the
particular market.

This is true because positions in markets that moved up and down a large amount per
contract would have an offsetting smaller number of contracts than positions in
markets that had lower volatility.

This volatility normalization is very important because it means that different trades in
different markets tend to have the same chance for a particular dollar loss or a
particular dollar gain. This increased the effectiveness of the diversification of trading
across many markets.

Even if the volatility of a given market was lower, any significant trend would result in
a sizeable win because the Turtles would have held more contracts of that lower
volatility commodity.
"""

import math
import pandas as pd

from yahoo_fin.stock_info import get_data, get_live_price


class Unit(object):
  """A Volatitility Adjusted Position Unit. 
  Args:
    asset: The ticker or symbol of an asset.
    account_size: The total value of the account.
  """
  def __init__(self, asset: str, account_size: float, *args, **kwargs) -> None:
    self.asset = asset
    self.account_size = account_size
    self.__process()
    
  def __process(self):
    self.calculate_N()
    self.get_unit()

  def __str__(self):
    return f"{self.asset}: {self.unit}"

  def _get_dataframe(self) -> pd.DataFrame:
    """Add true range column to dataframe."""
    df = get_data(ticker=self.asset, interval='1d')

    dataframe = df[['low', 'high', 'close']].tail(21)
    dataframe['previous_close'] = dataframe['close'].shift(1)
    dataframe['true_range'] = 0

    for index, row in enumerate(dataframe.iterrows()):
      curr = dataframe.iloc[index]
      dataframe.iloc[index, dataframe.columns.get_loc('true_range')] = max(curr['high'] - curr['low'], curr['high'] - curr['previous_close'], curr['previous_close'] - curr['low'])

    self.dataframe = dataframe
    return dataframe

  def _pdn(self) -> float:
    """Calculate the Previous Day's N."""
    return (sum(self.dataframe['true_range'][1:])) / 20
  
  def calculate_N(self) -> float:
    """Calculate N."""
    dataframe = self._get_dataframe()
    pdn = self._pdn()
    true_range = dataframe['true_range'][-1]

    self.N = (19 * pdn + true_range) / 20
    return self.N

  def _dollar_volatility(self) -> float:
    """Calculate the market dollar volatility of the asset."""
    # add in functionality for futures contract.
    pps = get_live_price(self.asset)
    return self.N * pps
    
  def get_unit(self) -> float:
    """Calculate the volatility adjusted unit size."""
    dollar_volatility = self._dollar_volatility()
    self.unit = math.trunc((0.01 * self.account_size) / dollar_volatility)
    return self.unit

if __name__ == '__main__':
  unit = Unit(asset="AAPL", account_size=1_000_000.00)
  print(unit)