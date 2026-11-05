class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # one of the big take aways is that the list is sorted. in ascending order. 
        # we use two pointers from opposite directions
        l, r = 0, len(numbers) - 1
        
        # = because we are including duplicate numbers
        while l <= r:
            summed = numbers[l] + numbers[r]
            
            if summed == target:
                return [l + 1, r + 1]

            if summed > target:
                r -= 1
            elif summed < target:
                l += 1
        
        