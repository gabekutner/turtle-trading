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
""" using the position_sizing module """
from turtle_trading.position_sizing import getn

import datetime
date = datetime.date(2023, 11, 10)

getn(ticker='aapl') # >>> 2.5725
getn(ticker='aapl', date=date) # >>> 2.9932

# updating getunit
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).