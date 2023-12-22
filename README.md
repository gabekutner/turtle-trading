# turtle-trading
<br>

A Python Package of a collection Turtle Trading investing tools. All code is based on the ideas presented in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf). Page numbers are referenced in the code.

The package, currently, contains only one module: position_sizing.

Download using pip:

```batch
pip install turtle-trading
```

Examples using the `position_sizing` and `entries` modules:

```python
from turtle_trading.position_sizing import getn, getunit
from turtle_trading.entries import getsignal

# your account value
account = 1_000_000.00

# Chapter 3: Position Sizing
""" Get 'N' of an asset. """
asset = getn(asset="AAPL")
print(asset.N) # e.g. returns.. > 2.19987

""" Find the Unit Size of an asset. """
unit = getunit(asset="AAPL", N=asset.N, account_size=account)
print(unit.UNIT) # e.g. returns.. > 2334

# Chapter 4: Entries
""" Get an Entry Signal - True for long entry, False for short entry, None for no entry """
from yahoo_fin.stock_info import get_data, get_live_price
dataframe = get_data(ticker="AAPL", interval="1d")
price = get_live_price(ticker="AAPL")

signal_using_system_one = getsignal(price=price, dataframe=dataframe, system=1) 
signal_using_system_two = getsignal(price=price, dataframe=dataframe, system=2)

print(signal_using_system_one) # e.g. returns... > True
print(signal_using_system_two) # e.g. returns... > False
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).