#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Adjusting Trading Size

There will be times when the market does not trend for many months. During these
times, it is possible to lose a significant percentage of the equity of the account.
After large winning trades close out, one might want to increase the size of the equity
used to compute position size.

The Turtles did not trade normal accounts with a running balance based on the initial
equity. We were given notional accounts with a starting equity of zero and a specific
account size. For example, many Turtles received a notional account size of $1,000,000
when we first started trading in February, 1983. This account size was then adjusted
each year at the beginning of the year. It was adjusted up or down depending on the
success of the trader as measured subjectively by Rich. The increase/decrease typically
represented something close to the addition of the gains or losses that were made in
the account during the preceding year.

The Turtles were instructed to decrease the size of the notional account by 20% each
time we went down 10% of the original account. So if a Turtle trading a $1,000,000
account was ever was down 10%, or $100,000, we would then begin trading as if we
had a $800,000 account until such time as we reached the yearly starting equity. If we
lost another 10% (10% of $800,000 or $80,000 for a total loss of $180,000) we were to
reduce the account size by another 20% for a notional account size of $640,000.

There are other, perhaps better strategies for reducing or increasing equity as the
account goes up or down. These are simply the rules that the Turtles used
"""


"""
The Turtles were instructed to decrease the size of the notional account by 20% each
time we went down 10% of the original account. So if a Turtle trading a $1,000,000
account was ever was down 10%, or $100,000, we would then begin trading as if we
had a $800,000 account until such time as we reached the yearly starting equity
"""
def decrease_size(account_size: float) -> float:
  """Return the new account size. This function is called if the account has suffered a 10% loss."""
  loss = 0.2 * account_size
  return account_size - loss