# turtle-trading
A Python Package of a collection Turtle Trading investing tools. All code is based on the ideas presented in [_The Original Turtle Trading Rules_](https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf).

The package, currently, contains only one working beta module: position_sizing.

Download using pip:

```batch
pip install turtle-trading
```

Examples:

```python
from turtle_trading.position_sizing import units, adjusting_size

""" Create a Unit instance. """
unit = units.Unit(asset="AAPL", account_size=1_000_000)

""" Determine how many shares are in one unit. """
print(unit) # returns.. > AAPL: 20

""" See N, learn about this on page 12. """
print(unit.N) # returns.. > 2.19987
```

More will be published soon.

For issues, look [here](https://github.com/gabekutner/turtle-trading/blob/main/.github/ISSUE_TEMPLATE.md).