# turtle-trading
<br>

A Python Package containing a collection of investing tools using the Turtle Traders Original Rules. All code is based on the ideas in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf). 

Download using pip:

```batch
pip install turtle-trading
```

__USAGE__: First, initialize a `DataFrameLoader` class to pass as an argument to most `turtle_trading` functions as shown below.
```python
from turtle_trading import DataFrameLoader

ticker = 'aapl'
dataframe = DataFrameLoader(ticker)
```

### `position_sizing` module
```python
""" using the position_sizing module """
from turtle_trading.position_sizing import getn, getunitsize

import datetime
date = datetime.date(2023, 11, 10)

getn(dataframe) # >>> 2.7421
getn(dataframe, date=date) # >>> 2.9932

getunitsize(dataframe=dataframe, account=1000000, n=2.7421) # >>> 20.0475
getunitsize(dataframe=dataframe, account=1000000, date=date) # >>> 17.9233
```

### `entries` module
```python
""" using the entries module """
from turtle_trading.entries import getentry_signal, addunits

getsignal(dataframe=dataframe, system=1) # >>> True
getsignal(dataframe=dataframe, system=2) # >>> True

addunits(breakout=310, n=2.50) # >>> [310, 311.25, 312.5, 313.75]
addunits(breakout=310, n=2.50, units_num=6) # >>> [310, 311.25, 312.5, 313.75, 315.0, 316.25]
```

### `stops` module
```python 
""" using the stops module """
from turtle_trading.entries import addunits
from turtle_trading.stops import getstops

units = addunits(breakout=28.30, n=1.20) # >>> [28.3, 28.9, 29.5, 30.1]

getstops(stop_system="regular", unit_list=units, n=1.20) # >>> [27.7, 27.7, 27.7, 27.7]
getstops(stop_system="whipsaw", unit_list=units, n=1.20) # >>> [27.7, 28.3, 28.9, 29.5]


gapped_units = [28.3, 28.9, 29.5, 30.8]

getstops(stop_system="regular", unit_list=gapped_units, n=1.20) # >>> [27.7, 27.7, 27.7, 28.4]
getstops(stop_system="whipsaw", unit_list=gapped_units, n=1.20) # >>> [27.7, 28.3, 28.9, 30.2]
```

### `exits` module
```python
import datetime
from turtle_trading.exits import getexit_signal

getexit_signal(dataframe=dataframe, system=1, pos_direction=True) # >>> True

getexit_siganl(dataframe=dataframe, system=1, pos_direction=True, date=datetime.date(2023, 11, 10)) # >>> False
```

Official documentation coming soon...

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).