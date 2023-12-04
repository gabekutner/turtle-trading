# Class for determining volatility adjust position units.
import math
from yahoo_fin.stock_info import get_data, get_live_price


class Unit(object):
  """A Volatitility Adjusted Position Unit. 
  Args:
    asset: The ticker or symbol of an asset.
    version: 0.1 for futures, 1.1 for common stock
  """
  def __init__(self, asset: str, account_size: float, version: float = 1.1) -> None:
    """"""
    self.asset = asset
    self.account_size = account_size

    VERSIONS = {0.1, 1.1}
    if version in VERSIONS:
      self.version = version
    else:
      raise ValueError("version must be one of %r" % VERSIONS)
        
    self.__process()
    
  def __process(self):
    self.calculate_N()
    self.get_unit()

  def __str__(self):
    return f"{self.asset}: {self.unit}"

  def _get_dataframe(self):
    """Add true range column to dataframe."""
    df = get_data(ticker=self.asset, interval='1d')
    dataframe = df[['low', 'high', 'close']].tail(21)
    dataframe['previous_close'] = dataframe['close'].shift(1)
    dataframe['true_range'] = dataframe['high'] - dataframe['low']

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
    """Calculate the market dollar volatility."""
    if self.version == 0.1:
      # futures
      print("Futures feature not finished.")
    
    if self.version == 1.1:
      pps = get_live_price(self.asset)
      return self.N * pps
    
  def get_unit(self) -> float:
    """Calculate the volatility adjusted unit size."""
    dollar_volatility = self._dollar_volatility()
    self.unit = math.trunc((0.01 * self.account_size) / dollar_volatility)
    return self.unit