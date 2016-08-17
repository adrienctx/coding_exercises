"""
Suppose you are given an array stock_prices_yesterday of the prices of a stock over time.
Write an efficient algorithm for computing the best profit you can make from first buying 1 share of the stock,
and then selling that 1 share later.  Note that you must buy before you sell (no "sorting").
For example, if stock_prices_yesterday=[5, 6, 4, 7, 9, 8, 8], then the correct answer is to buy the stock at $4,
and then sell it at $9, for a profit of $5.
"""
import sys


def find_best_trade(stock_prices):
    # initialize important variables - we call i the index that iterates the price array, from left to right
    # this is the lowest price found on the left of the current index i
    lowest_price_on_left = sys.maxint
    # this is the currently best trade (i.e. doable up to time/index i)
    best_trade = -sys.maxint
    # the index of the lowest price on the left (i.e. the recommended buy-time, if we only know prices until i)
    buy_on_left = 0

    # iterate through the price array, and use the above variables to get the best trade, as well as buy/sell indices
    for i in range(len(stock_prices)):
        if stock_prices[i] < lowest_price_on_left:
            # we found a new lowest price: any best trade happening after i cannot buy at a time i' < i, since it would
            # be strictly worse than buying at i
            lowest_price_on_left = stock_prices[i]
            buy_on_left = i
        elif (stock_prices[i] - lowest_price_on_left) > best_trade:
            # Using the up-to-date lowest price on left, we found a better trade, so we update our results
            best_trade = stock_prices[i] - lowest_price_on_left
            buy = buy_on_left
            sell = i

    return best_trade, buy, sell
