from src.turtle_trading.position_sizing import calc_n, units

if __name__ == "__main__":
    n = calc_n("AAPL")
    unit_size = units.unit(1000000.00, n, "AAPL")

    print("N: {!r}".format(n))
    print("Unit size: {!r}".format(unit_size))