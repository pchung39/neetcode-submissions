class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # 1. Find the correct row where target could reside
        target_row = -1
        for idx, row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                target_row = idx
                break  # Stop as soon as we find the matching row layer
                
        if target_row == -1:
            return False
        
        # 2. Standard Binary Search on the target row
        left, right = 0, COLS - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False