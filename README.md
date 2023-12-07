# turtle-trading
A Python Package of a collection Turtle Trading investing tools. All code is based on the ideas presented in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf). Page numbers are referenced in the code.

The package, currently, contains only one module: position_sizing.

Download using pip:

```batch
pip install turtle-trading
```

Examples using the `position_sizing` module:

```python
from turtle_trading.position_sizing import units, adjusting_size, risk_management

# your account value
account = 1_000_000.00

""" Create a Unit instance. """
unit = units.Unit(asset="AAPL", account_size=account)


""" See N: the underlying volatility of a particular market 
Pg. 12
"""
print(unit.N) # returns.. > 2.19987


""" See Volatility Adjusted Position Units
Pg. 18
"""
print(unit.get_unit) # returns.. > 20
# or 
print(unit.unit) # returns.. > AAPL: 20


""" Adjusting Trading Size
pg. 21
"""
print(adjusting_size.decrease_size(account)) # returns.. > 800_000
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).