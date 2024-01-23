Usage
=====

Install the **turtle-trading** library using pip:

.. code-block:: console

  (.venv) $ pip install turtle-trading


Before we start using the **turtle-trading** modules, initialize a DataFrameLoader class. 
This loads the given ticker's price data. 

.. note:: We'll need this for most of the rest of the **turtle-trading** functions.

.. code-block:: Python
  :linenos:
  :emphasize-lines: 3

  from turtle_trading import DataFrameLoader

  dataframe = DataFrameLoader('aapl')


the Position Sizing module
--------------------------
The **turtle_trading.position_sizing** module has two main functionalities.

* Get the underlying volatility of a particular asset - N.
* Calculate the position size, or how many shares represents 1 unit.


.. code-block:: Python
  :linenos:

  from turtle_trading.position_sizing import getn, getunits

  import datetime
  date = datetime.date(2023, 11, 10)

  getn(dataframe) # >>> 2.7421
  other_n = (dataframe, date) # >>> 2.9932

  one_unit = getunits(dataframe, 1000000, n=n) # >>> 20.0475
  one_unit = getunits(dataframe, 1000000, date=date) # >>> 17.9233

  # NOTE: Passing in a date and n argument to the getunits function will raise an AttributeError.


Also in the **position_sizing** module are exceptions, to be raised by your own discretion.
They are risk management rules.

* **SingleMarketsException**: A maximum of 4 Units per market (position).

* **CloselyCorrelatedMarketsException**: A maximum of 6 Units in one particular direction, for closely correlated markets.

* **LooselyCorrelatedMarketsException**: A maximum of 10 Units in one particular direction, for loosely correlated markets.

* **SingleDirectionException**: A maximum of 12 Units in one direction, long or short.

.. code-block:: Python
  :linenos:

  from turtle_trading.exceptions import (
    SingleMarketsException,
    CloselyCorrelatedMarketsException,
    LooselyCorrelatedMarketsException,
    SingleDirectionException
  )

  if units_of_aapl > 4:
    raise SingleMarketsException 

  if closely_correlated_units > 6:
    raise CloselyCorrelatedMarketsException

  if loosely_correlated_units > 10:
    raise LooselyCorrelatedMarketsException

  if long_units > 12:
    raise SingleDirectionException


the Entries module
------------------
The **turtle_trading.entries** module has two main functionalities.

* Get an entry signal, if there is one.
* Add units to an already existing position.

There are two systems you can use for entry signals. They are explained in the `The Original Turtle Trading Rules <https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf>`_.
Quickly, there are two systems: 1 and 2. System 1 is more complicated than System 2.

* **System 1**: based on a 20-day breakout, unless the previous breakout resulted in a winning trade. 
* **System 2**: based on a 55-day breakout, regardless of the outcome of the previous breakout. 

The results of the **getentry** function are in booleans.

* True means enter long. 
* False means enter short.
* None means don't enter.

.. code-block:: Python
  :linenos:

  from turtle_trading.entries import getentry

  getentry(dataframe, system=1) # >>> True
  getentry(dataframe, system=2) # >>> True


The **addunits** function takes in the entry price (orig_breakout) and N at that entry price (orig_n).

.. code-block:: Python
  :linenos:

  from turtle_trading.entries import addunits

  addunits(orig_breakout=310, orig_n=2.50) # >>> [310, 311.25, 312.5, 313.75]
  addunits(orig_breakout=310, orig_n=2.50, number_of_units=6) # >>> [310, 311.25, 312.5, 313.75, 315.0, 316.25]

  # DISCLAIMER: In the rules, no more than 4 more units are allowed for a single position.


the Stops module
----------------
The **turtle_trading.stops** module has one main functionality.

* Calculate the stops for each unit of a position. 

There are two strategies you can use for calculating stops: the regular stop strategy and the whipsaw stop strategy. 

* The regular stop strategy: Each stop is the same, the stop being the difference between the last unit added unit and 2N.
* The whipsaw stop strategy: Each stop is the difference between the unit and 2N.

For gapped units, meaning units manually added not according to the **addunits** function, the results are a little 
different - but only for the regular stop strategy.



.. code-block:: Python
  :linenos:

  from turtle_trading.stops import getstops

  units = [28.3, 28.9, 29.5, 30.1]

  getstops(stop_system="regular", unit_list=units, orig_n=1.20) # >>> [27.7, 27.7, 27.7, 27.7]
  getstops(stop_system="whipsaw", unit_list=units, orig_n=1.20) # >>> [27.7, 28.3, 28.9, 29.5]

  gapped_units = [28.3, 28.9, 29.5, 30.8]

  getstops(stop_system="regular", unit_list=gapped_units, orig_n=1.20) # >>> [27.7, 27.7, 27.7, 28.4]
  getstops(stop_system="whipsaw", unit_list=gapped_units, orig_n=1.20) # >>> [27.7, 28.3, 28.9, 30.2]


the Exits module
----------------
The **turtle_trading.exits** module has one main functionality.

* Get a stop signal, if there is one.

There are two systems you can use for entry signals. They are explained in the `The Original Turtle Trading Rules <https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf>`_.
Quickly, there are two systems: 1 and 2. System 1 is more complicated than System 2.

* **System 1**: based on a 10-day low for long positions and a 10-day high for short positions.
* **System 2**: based on a 20-day low for long positions and a 20-day high for short positions.

.. code-block:: Python
  :linenos:

  from turtle_trading.exits import getexit

  getexit(dataframe=dataframe, system=1, pos_direction=True) # >>> True

  getexit(dataframe=dataframe, system=1, pos_direction=True, date=datetime.date(2023, 11, 10)) # >>> False