#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Units as a measure of Risk

Since the Turtles used the Unit as the base measure for position size, and since those
units were volatility risk adjusted, the Unit was a measure of both the risk of a position,
and of the entire portfolio of positions.

The Turtles were given risk management rules that limited the number of Units that
we could maintain at any given time, on four different levels. In essence, these rules
controlled the risk that a trader could carry, and these limits minimized losses
during prolonged losing periods, as well as during extraordinary price movements.

An example of an extraordinary price movement was the day after the October, 1987
stock market crash. The U.S. Federal Reserve lowered interest rates by several
percentage points overnight to boost the confidence of the stock market and the
country. The Turtles were loaded long in interest rate futures: Eurodollars, TBills and
Bonds. The losses the following day were enormous. In some cases, 20% to 40% of
account equity was lost in a single day. But these losses would have been
correspondingly higher without the maximum position limits.

The limits were: 
Level    Type                                Maximum Units
1        Single Market                       4 units
2        Closely Correlated Markets          6 units
3        Loosely Correlated Markets          10 units
4        Single Direction -- Long or Short   12 units
"""


"""Single Markets - A maximum of four Units per market."""
class SingleMarketsException(Exception):
    pass

"""Closely Correlated Markets -
For markets that were closely correlated and there could be
a maximum of 6 Units in one particular direction (i.e. 6 long units or 6 short units).
Closely correlated markets include: heating oil and crude oil; gold and silver; Swiss
franc and Deutschmark; TBill and Eurodollar, etc.
"""
class CloselyCorrelatedMarketsException(Exception):
    pass

"""Loosely Correlated Markets - 
For loosely correlated markets, there could be a
maximum of 10 Units in one particular direction. Loosely correlated markets included:
gold and copper; silver and copper, and many grain combinations that the Turtles did
not trade because of positions limits.
"""
class LooselyCorrelatedMarketsException(Exception):
    pass

"""Single Direction - 
The maximum number of total Units in one direction long or short
was 12 Units. Thus, one could theoretically have had 12 Units long and 12 Units short
at the same time.
"""
class SingleDirectionException(Exception):
    pass