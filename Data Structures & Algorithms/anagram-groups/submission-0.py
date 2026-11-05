class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for chars in strs:
            clean_string = "".join(sorted(chars))

            if clean_string in groups:
                groups[clean_string].append(chars)
            else:
                groups[clean_string] = [chars]
        
        return list(groups.values())