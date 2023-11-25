"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Calculate N - represents the underlying volatility of a particular market.

N is simply the 20-day exponential moving average of the True Range, which is now
more commonly known as the ATR. Conceptually, N represents the average range in
price movement that a particular market makes in a single day, accounting for opening
gaps. N was measured in the same points as the underlying contract.

To compute the True Range:
  True Range = Maximum(H-L, H-PDC, PDC-L)

where:
  H - Current High
  L - Current Low
  PDC - Previous Day's Close

To compute N:
  N = (19 * PDN + TR) / 20

where:
  PDN - Previous Day's N
  TR - Current Day's True Range

Since this formula requires a previous day's N value, you must start with a 20-day 
simple average of the True Range for the initial calculation.
"""
from yahoo_fin.stock_info import get_data


def get_dataframe(ticker: str):
  """Get dataframe and add true range."""
  df = get_data(ticker=ticker, interval='1d')
  dataframe = df[['low', 'high', 'close']].tail(21)
  # using high - low 
  dataframe['true_range'] = dataframe['high'] - dataframe['low']
  return dataframe

def calc_pdn(dataframe):
  """Calculate the Previous Day's N."""
  return (sum(dataframe['true_range'][1:])) / 20

def calc_n(pdn, dataframe):
  """Calculate N."""
  true_range = dataframe['true_range'][-1]
  return (19 * pdn + true_range) / 20


if __name__ == '__main__':
  print("Enter stock ticker: ")
  inp = input()

  dataframe = get_dataframe(inp)
  pdn = calc_pdn(dataframe)
  N = calc_n(pdn, dataframe)
  print("N: {!r}".format(N))