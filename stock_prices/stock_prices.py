#!/usr/bin/python

import argparse


def find_max_profit(prices):
    """Calculates the best trade possible given sequential prices."""
    # Iterate over prices to find best trade
    price_high = None
    price_low = None
    best_profit = None
    for price_current in prices:
        # Find profit (or loss) from selling at current price
        if(price_low):  # No trade if starting price
            price_delta = price_current - price_low
            if(best_profit is None or price_delta > best_profit):
                best_profit = price_delta
        # If higher than last highest, reset high price
        if(price_high is None or price_high < price_current):
            price_high = price_current
        # If lower than last lowest, reset both high and low prices
        # (The user can't sell for the previous highest price, now superceded,
        # and any future high prices can be traded using the new low price.)
        if(price_low is None or price_low > price_current):
            price_low = price_current
            price_high = price_current
    # Return calculated profit
    return best_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument(
        'integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()
    msg = "A profit of ${profit} can be made from the stock prices {prices}."
    msg = result.format(
        profit=find_max_profit(args.integers), prices=args.integers)
    print(msg)
