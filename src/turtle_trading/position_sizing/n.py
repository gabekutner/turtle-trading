"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Volatility - The Meaning of N
The Turtles used a concept that Richard Dennis and Bill Eckhardt called N to
represent the underlying volatility of a particular market.

N is simply the 20-day exponential moving average of the True Range, which is now
more commonly known as the ATR. Conceptually, N represents the average range in
price movement that a particular market makes in a single day, accounting for opening
gaps. N was measured in the same points as the underlying contract.

To compute the daily true range:
  TRUE RANGE = Maximum(H-L, H-PDC, PDC-L)

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
"""
from yahoo_fin.stock_info import get_data


def get_dataframe(ticker: str, version: float):
  """Add true range column to dataframe."""
  df = get_data(ticker=ticker, interval='1d')
  dataframe = df[['low', 'high', 'close']].tail(21)

  dataframe['previous_close'] = dataframe['close'].shift(1)
  dataframe['true_range'] = dataframe['high'] - dataframe['low']

  # print(dataframe)

  if version == 1.1:
    # dataframe = df[['low', 'high', 'close']].tail(21)
    x = ""
    # high_low = float(dataframe['high'] - dataframe['low'])
    # high_pc = float(dataframe['high'] - dataframe['previous_close'])
    # pc_low = float(dataframe['previous_close'] - dataframe['low'])
    # # dataframe['true_range'] = max(dataframe['high'] - dataframe['low'], dataframe['high'] - dataframe['previous_close'], dataframe['previous_close'] - dataframe['low'])
    # # print(dataframe['close'].shift(1) - dataframe['low'])
    # dataframe['true_range'] = max(high_low, high_pc, pc_low)

  return dataframe

def calc_pdn(dataframe):
  """Calculate the Previous Day's N."""
  return (sum(dataframe['true_range'][1:])) / 20

def calc_n(asset):
  """Calculate N."""
  dataframe = get_dataframe(asset, version=1.1)
  pdn = calc_pdn(dataframe)
  
  true_range = dataframe['true_range'][-1]
  return (19 * pdn + true_range) / 20

if __name__ == '__main__':
  inp = input("Enter asset: ")

  print(calc_n(inp))