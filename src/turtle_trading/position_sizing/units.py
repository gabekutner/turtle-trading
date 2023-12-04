"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Dollar Volatility Adjustment
The first step in determining the position size was to determine the dollar volatility
represented by the underlying market's price volatility (defined by its N).

This sounds more complicated than it is. It is determined using the simple formula:
  Dollar Volatility = N * Dollars per Point

Volatility Adjusted Position Units
The Turtles built positions in pieces which we called Units. Unites were sized so that 1 N
represented 1% of the account equity.

Thus, a unit for a given market or commodity can be calculated using the following
formula: 
  Unit = (1% of Account) / Market Dollar Volatility
  or
  Unit = (1% of Account) / N * Dollars per Point
"""
from yahoo_fin.stock_info import get_live_price


VERSIONS = {0.1, 1.1}
def dollar_volatility(asset, n, version):
    """Calculate the market dollar volatility."""
    if version not in VERSIONS:
      raise ValueError("version must be one of %r" % VERSIONS)
    
    if version == 0.1:
      # futures
      print("Futures feature not finished.")
    
    if version == 1.1:
      pps = get_live_price(asset)
      return n * pps
    
def unit(account_size: float, n: float, asset: str):
  """Calculate the volatility adjusted unit size."""
  dollar_volatility = dollar_volatility(asset=asset, n=n, version=1.1)
  return (0.01 * account_size) / dollar_volatility