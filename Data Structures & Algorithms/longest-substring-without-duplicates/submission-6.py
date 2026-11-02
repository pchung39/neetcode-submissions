class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_list = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            # check if s[r] in duplist
            while s[r] in dup_list:
                dup_list.remove(s[l])
                l += 1
            dup_list.add(s[r])
            longest = max(longest, r - l +1)
        
        return longest


        # add char list in dup_list
        
 










        # dup_list = set()
        # longest = 0
        # l = 0

        # for r in range(len(s)):
        #     while s[r] in dup_list:
        #         dup_list.remove(s[l])
        #         l += 1
        #     dup_list.add(s[r])
        #     longest = max(longest, r - l + 1)

        # return longest