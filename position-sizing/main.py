"""Put everything together."""
from n import calc_n
from units import dollar_volatility, unit


if __name__ == "__main__":
  asset = input("Enter a symbol: ")
  type = input("Enter 0.1 for futures, 1.1 for common stock: ")
  which = input("Enter 1 for True Alpha, 2 for False Alpha: ")
  
  if which == 1:
    account = 1000.00
  if which == 2:
    account = 10000.00

  N = calc_n(asset)
  D = dollar_volatility(version=float(type), asset=asset, n=N)
  unit_size = unit(D, account)
  
  print("N: {!r}".format(N))
  print("Dollar Volatility: {!r}".format(D))
  print("Unit Size: {!r}".format(unit_size))