"""https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf

Dollar Volatility Adjustment
The first step in determining the position size was to determine the dollar volatility
represented by the underlying market's price volatility (defined by its N).

This sounds more complicated than it is. It is determined using the simple formula:
  Dollar Volatility = N * Dollars per Point

Volatility Adjusted Position Units
The Turtles built positions in pieces which we called Units. Unites were sized so that 1 N
represented 1% of the account equity.

Thus, a unit for a given market or commodity can be calculated using the following
formula: 
  Unit = (1% of Account) / Market Dollar Volatility
  or
  Unit = (1% of Account) / N * Dollars per Point
"""




if __name__ == '__main__':
    # print("Enter the account size ($): ")
    inp = input("Enter the account size ($): ")
    print(inp)