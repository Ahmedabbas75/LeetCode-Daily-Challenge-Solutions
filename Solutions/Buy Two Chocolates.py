class Solution:
    def buyChoco(self, prices, money: int) -> int:
        # sort list
        prices.sort()
        # return solution
        return money if (prices[0] + prices[1]) > money else money - ((prices[0] + prices[1]))
    