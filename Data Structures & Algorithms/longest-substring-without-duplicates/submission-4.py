class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        duplicate is any character that appears more than once in a string
        if that's the case we want to detect when a character appears more
        than once. substring can be at any point in the string. we need to keep track of indexes
        and we need to keep track of substring length

        immediate solution is hash table (more space but speed stays relatively the same)
        or can save space but do an increased log number of checks

        i would go with hash table because alphabet is 26 chars max
        '''

        char_list = {}
        # what do we need to keep track of
        start_pointer = 0

        longest_length = 0
        for end_pointer in range(len(s)):
            if s[end_pointer] in char_list and char_list[s[end_pointer]] >= start_pointer:
                start_pointer = char_list[s[end_pointer]] + 1
            char_list[s[end_pointer]] = end_pointer
            longest_length = max(longest_length, end_pointer - start_pointer + 1)

        return longest_length
        