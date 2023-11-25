"""Put everything together.
"""
from n import calc_n
from units import dollar_volatility, unit


if __name__ == "__main__":
  asset = input("Enter a symbol: ")
  type = input("Enter 0.1 for futures, 1.1 for common stock: ")
  account = input("Enter account size: ")

  N = calc_n(asset)
  D = dollar_volatility(version=float(type), asset=asset, n=N)
  unit_size = unit(D, account)