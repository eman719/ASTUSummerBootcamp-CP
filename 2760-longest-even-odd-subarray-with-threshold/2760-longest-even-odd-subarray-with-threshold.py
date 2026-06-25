class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        longest = 0
        i = 0
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                    length += 1
                    j += 1
                longest = max(longest, length)
            i += 1
        return longest
