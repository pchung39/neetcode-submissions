from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(list(ransomNote))
        mag_dict = Counter(list(magazine))

        # whats our true condition, ransomNote should be empty dict
        subtract = ransom_dict - mag_dict

        if len(subtract) > 0:
            return False
        else:
            return True
        