"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

>>> maxProfit([7,1,5,3,6,4])
7
>>> maxProfit([1,2,3,4,5])
4
>>> maxProfit([7,6,4,3,1])
0
"""

def maxProfit(prices):
        
    profit_options = []
    
    if len(prices) <= 1:
        return sum(profit_options)
    
    else:
        
        min_price = prices[0]
        
        for price in prices[1:]:
            if price > min_price:
                profit = price - min_price
                min_price = price
                profit_options.append(profit)
            
            else:
                min_price = price 
                
        return sum(profit_options)

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')