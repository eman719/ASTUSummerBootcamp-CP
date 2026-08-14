class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        i = j = k
        min_val = nums[k]
        max_score = nums[k]
        n = len(nums)

        while i > 0 or j < n - 1:
            left_val = nums[i - 1] if i > 0 else -1
            right_val = nums[j + 1] if j < n - 1 else -1

            if left_val >= right_val:
                i -= 1
                min_val = min(min_val, nums[i])
            else:
                j += 1
                min_val = min(min_val, nums[j])

            max_score = max(max_score, min_val * (j - i + 1))

        return max_score