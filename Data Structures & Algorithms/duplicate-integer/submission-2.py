from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = defaultdict(int)

        for n in nums:
            if h[n] == 1:
                return True
            h[n] += 1
        
        return False