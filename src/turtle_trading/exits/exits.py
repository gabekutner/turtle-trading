# #!/usr/bin/env python
# # -*- coding: UTF8 -*-
# """https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

# Exits
# The Turtles used breakout based exits for profitable positions.

# There is an old saying: "you can never go broke taking a profit." The 
# Turtles would not agree with this statement. Getting out of winning positions
# too early, i.e. "taking a profit" too early, is one of the most common mistakes
# when trading trend following systems.

# Prices never go straight up; therefore it is necessary to let the prices go against you if
# you are going to ride a trend. Early in a trend this can often mean watching decent
# profits of 10% to 30% fade to a small loss. In the middle of a trend, it might mean
# watching a profit of 80% to 100% drop by 30% to 40%. The temptation to lighten the 
# position to "lock in profits" can be very great.

# The Turtles knew that where you took a profit could make the difference between
# winning and losing.

# The Turtle System enters on breakouts. Most breakouts do not result in trends. This
# means that most of the trades that the Turtles made resulted in losses. If the winning
# trades did not earn enough on average to offset these losses, the Turtles would have
# lost money. Every profitable trading system has a different optimal exit point.

# Consider the Turtle System; if you exit winning positions at a 1 N profit while you
# exited losing positions at a 2 N loss you would need twice as many winners to offset
# the losses from the losing trades.

# There is a complex relationship between the components of a trading system. This
# means that you can't consider the proper exit for a profitable position without
# considering the entry, money management and other factors.

# The proper exit for winning positions is one of the most important aspects of trading,
# and the least appreciated. Yet it can make the difference between winning and losing.

# Turtle Exits

# The System 1 exit was a 10 day low for long positions and a 10 day high for short
# positions. All the Units in the position would be exited if the price went against the
# position for a 10 day breakout.

# The System 2 exit was a 20 day low for long positions and a 20 day high for short
# positions. All the Units in the position would be exited if the price went against the
# position for a 20 day breakout.

# As with entries, the Turtles did not typically place exit stop orders, but instead watched
# the price during the day, and started to phone in exit orders as soon as the price traded
# through the exit breakout price.
# """

# # n
# # breakout
# # long or short: bool

# def getexit(n, breakout, type: bool):
#   """Return a decision on whether to exit or not.

#   Args:
#     n: 'N' of the breakout.
#     breakout: The breakout price, i.e. the first unit entered.
#     units: How many units in that same position there are.
#   """
#   return Exit(n=n, breakout=breakout, type=type)


# class Exit:
#   def __init__(self, n, breakout, type: bool):

#     self.exit_signal = self.signal()
  
  

#   def signal(self) -> bool:
#     """Return a boolean determing whether to exit or not.

#     Args:
      

#     Returns:
#       True to exit, False to not. 
#     """
#     # First, get the  