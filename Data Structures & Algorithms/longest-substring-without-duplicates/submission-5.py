class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_list = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            # check if z in dict and greater than 1
            while s[r] in dup_list:
                dup_list.remove(s[l])
                l += 1
            dup_list.add(s[r])
            longest = max(longest, r - l + 1)

        return longest