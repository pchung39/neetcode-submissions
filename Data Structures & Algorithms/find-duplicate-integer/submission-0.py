class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dup_list = {}

        for num in nums:
            if num in dup_list:
                dup_list[num] += 1
            else:
                dup_list[num] = 1
        
        for key, val in dup_list.items():
            if val > 1:
                return key
        