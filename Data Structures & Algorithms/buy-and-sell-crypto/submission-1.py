class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        top = 0 
        while j < len(prices):
            if prices[i] < prices[j]:
                top = max(top, prices[j] - prices[i])
                j+=1
            else:
                i =j
                j+=1 
            print(top)
        return top