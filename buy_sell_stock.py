def maxProfit(prices):
    """
    >>> maxProfit([7,1,5,3,6,4])
    5
    >>> maxProfit([7,6,4,3,1])
    0
    """
                    
#         for i, price in enumerate(prices):
#             for x in prices[i:]:
#                 profit = x - price
#                 if profit > max_profit:
#                     max_profit = profit
        
#         return max_profit

    max_profit = 0    
    
    if len(prices) == 0:
        return max_profit
    
    else:
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
    
    return max_profit

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')