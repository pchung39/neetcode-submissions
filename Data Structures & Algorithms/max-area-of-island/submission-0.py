class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row_count = len(grid)
        col_count = len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= row_count) or (c < 0 or c >= col_count) or grid[r][c] == 0:
                return 0

            if grid[r][c] == 1:
                grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    print(area)
                    maxArea = max(maxArea, area)

        return maxArea

        
