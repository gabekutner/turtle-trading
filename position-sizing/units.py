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

# first, find Market Dollar Volatility
  # futures contract: the change in the asset for a 1$ change in the underlying commodity
  # stock: price per share of the stock
VERSIONS = {0.1, 1.1}
def dollar_volatility(version, asset, n):
  if version not in VERSIONS:
    raise ValueError("version must be one of %r." % VERSIONS)
    
  if version == 0.1:
    # futures
    pass
  if version == 1.1:
    # stock
    pps = get_live_price(asset)
    return n * pps
    

# second, find unit size
def unit(dollar_volatility, account_size):
  return (0.01 * account_size) / dollar_volatility


if __name__ == '__main__':
  asset = input("Enter the asset symbol: ")
  version = input("Enter 0.1 if the asset is a futures contract or 1.1 for common stock: ") 
  account = input("Enter the account size ($): ")
  
  

  
  