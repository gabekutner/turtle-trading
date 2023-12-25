# turtle-trading
<br>

A Python Package containing a collection of investing tools using the Turtle Traders Original Rules. All code is based on the ideas in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf). Page numbers are referenced in the code.

Download using pip:

```batch
pip install turtle-trading
```

Examples using the `position_sizing` and `entries` modules:

__NOTE__: The `exits` and `stops` modules aren't finished yet.

```python
from turtle_trading.position_sizing import getn, getunit
from turtle_trading.entries import getsignal, addunits

# your account value
account = 1_000_000.00


# Chapter 3: Position Sizing
""" Get 'N' of an asset. """
asset = getn(asset="AAPL")
print(asset) # e.g. returns.. > 2.19987

""" Find the Unit Size of an asset. """
unit = getunit(asset="AAPL", n=asset, account_size=account)
print(unit) # e.g. returns.. > 2334


# Chapter 4: Entries
""" Get an Entry Signal - True for long entry, False for short entry, None for no entry. """
from yahoo_fin.stock_info import get_data, get_live_price
dataframe = get_data(ticker="AAPL", interval="1d")
price = get_live_price(ticker="AAPL")

signal_using_system_one = getsignal(asset="AAPL", price=price, system=1) 
signal_using_system_two = getsignal(asset="AAPL", price=price, system=2)

print(signal_using_system_one) # e.g. returns... > True
print(signal_using_system_two) # e.g. returns... > False

""" Add Units to entries. """
n = 1.20
breakout = 28.30
new_units = addunits(n=n, breakout=breakout, units=4)
print(new_units) # e.g. returns... > [28.30, 28.90, 29.50, 30.10]
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).