# turtle-trading
<br>

A Python Package containing a collection of investing tools using the Turtle Traders Original Rules. All code is based on the ideas in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf). 

Download using pip:

```batch
pip install turtle-trading
```

### `position_sizing` module
```python
""" using the position_sizing module """
from turtle_trading.position_sizing import getn, getunit

import datetime
date = datetime.date(2023, 11, 10)

getn(ticker='aapl') # >>> 2.5725
getn(ticker='aapl', date=date) # >>> 2.9932

getunit(ticker='aapl', account=1000000, n=1.2) # >>> 44.8898
getunit(ticker='aapl', account=1000000, date=date) # >>> 17.9233
```

### `entries` module
```python
""" using the entries module """
from turtle_trading.entries import getsignal, addunits

getsignal(ticker='aapl', system=1) # >>> True
getsignal(ticker='aapl', system=2) # >>> True

addunits(breakout=310, n=2.50) # >>> [310, 311.25, 312.5, 313.75]
addunits(breakouts=310, n=2.50, units=6) # >>> [310, 311.25, 312.5, 313.75, 315.0, 316.25]
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).