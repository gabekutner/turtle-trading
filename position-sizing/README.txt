## Position Sizing Module

Position sizing is one of the most important but least understood components
of any trading system.

The Turtles used a position sizing algorithm that was very advanced for its day,
because it normalized the dollar volatility of a position by adjusting the position size
based on the dollar volatility of the market. This meant that a given position would
tend to move up or down in a given day about the same amount in dollar terms (when
compared to positions in other markets), irrespective of the underlying volatility of the
particular market.

This is true because positions in markets that moved up and down a large amount per
contract would have an offsetting smaller number of contracts than positions in
markets that had lower volatility.

This volatility normalization is very important because it means that different trades in
different markets tend to have the same chance for a particular dollar loss or a
particular dollar gain. This increased the effectiveness of the diversification of trading
across many markets.

Even if the volatility of a given market was lower, any significant trend would result in
a sizeable win because the Turtles would have held more contracts of that lower
volatility commodity.

## Volatility - The Meaning of N

The Turtles used a concept that Richard Dennis and Bill Eckhardt called N to
represent the underlying volatility of a particular market.

N is simply the 20-day exponential moving average of the True Range, which is now
more commonly known as the ATR. Conceptually, N represents the average range in
price movement that a particular market makes in a single day, accounting for opening
gaps. N was measured in the same points as the underlying contract.

To compute the daily true range:

TRUE RANGE = Maximum(H-L,H-PDC,PDC-L)

Where:

H - Current High
L - Current Low
PDC - Previous Day Close

To compute N use the following formula:

N = (19 * PDN * TR) / 20

Where: 

PDN - Previous Day's N
TR - Current Day's True Range

Since this formula requires a previous day’s N value, you must start with a 20-day
simple average of the True Range for the initial calculation.