class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            
            if char in d:
                if not stack:
                    return False

                popped = stack.pop()
                if popped != d[char]:
                    return False
        
        if len(stack) != 0:
            return False
        return True
