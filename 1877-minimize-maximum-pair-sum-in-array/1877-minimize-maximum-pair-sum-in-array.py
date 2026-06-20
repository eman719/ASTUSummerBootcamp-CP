class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max=0
        n=len(nums)
        for i in range(n//2):
            current = nums[i]+nums[n-i-1]
            if current > max:
                max = current
        return max