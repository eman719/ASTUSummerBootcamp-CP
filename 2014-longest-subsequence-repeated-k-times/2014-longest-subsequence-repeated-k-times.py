from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = Counter(s)
        chars = sorted([ch for ch, freq in counts.items() if freq >= k], reverse=True)
        
        def is_subseq(sub: str) -> bool:
            target = sub * k
            t_idx = 0
            for char in s:
                if char == target[t_idx]:
                    t_idx += 1
                    if t_idx == len(target):
                        return True
            return False

        q = deque([""])
        ans = ""

        while q:
            curr = q.popleft()
            for c in chars:
                candidate = curr + c
                if is_subseq(candidate):
                    if len(candidate) > len(ans) or (len(candidate) == len(ans) and candidate > ans):
                        ans = candidate
                    q.append(candidate)
                    
        return ans