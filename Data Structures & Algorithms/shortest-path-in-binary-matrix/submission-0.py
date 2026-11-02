class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1                                   # blocked start or end

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]      # 8 directions, diagonals included
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        length = 1                                      # the start cell counts as 1

        while queue:
            for _ in range(len(queue)):                 # one level = one more cell of path
                row, col = queue.popleft()
                if row == n - 1 and col == n - 1:
                    return length
                for row_step, col_step in directions:
                    next_row, next_col = row + row_step, col + col_step
                    if (0 <= next_row < n and 0 <= next_col < n
                            and grid[next_row][next_col] == 0
                            and (next_row, next_col) not in visited):
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
            length += 1

        return -1     
