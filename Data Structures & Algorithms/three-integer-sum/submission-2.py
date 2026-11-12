class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # [-4, -1, -1, 0, 2]

        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                summed = nums[i] + nums[j] + nums[k]
                
                if summed == 0:
                    combo = [nums[i], nums[j], nums[k]]
                    if combo not in res:
                        res.append(combo)
                    k -= 1
                    j += 1
                if summed > 0:
                    k -= 1
                if summed < 0:
                    j += 1
        return res
            



















        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res