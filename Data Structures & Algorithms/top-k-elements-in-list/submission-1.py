from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans = []
        for i in range(k):
            ans.append(max(d, key=d.get))
            d[max(d, key=d.get)] = 0

        return ans