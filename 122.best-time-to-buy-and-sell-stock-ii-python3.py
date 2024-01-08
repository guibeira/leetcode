# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_take = prices.pop(0)
        total = 0
        index = 0
        while index != len(prices):
            price = prices[index]

            if price_take < price:
                total += price - price_take
                prices.pop(index)
                index -= 1

            price_take = price
            index += 1
        return total


# @leet end
