class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                popped_idx = stack.pop()
                delta = i - popped_idx
                result[popped_idx] = delta
            stack.append(i)
        
        return result

        