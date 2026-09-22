from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        c = sorted(set(nums))

        ans = 1
        compteur = 1
        for i in range(1, len(c)):
            if c[i] == c[i - 1] + 1:
                compteur += 1
            else:
                compteur = 1
            ans = max(ans, compteur)

        return ans