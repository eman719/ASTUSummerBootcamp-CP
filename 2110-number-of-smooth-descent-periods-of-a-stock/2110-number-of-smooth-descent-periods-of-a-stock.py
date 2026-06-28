class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total_periods = 1
        current_len = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                current_len += 1
            else:
                current_len = 1
            total_periods += current_len
            
        return total_periods  