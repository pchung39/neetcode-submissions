class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # breadth first search
        # noticing: one banana will be rotten, that is our starting point. 
        queue = deque()
        fresh_count = 0
        row_count = len(grid)
        col_count = len(grid[0])
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == 2:
                    queue.append((row, col))     # every rotten orange starts in the queue
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        # what do we want: queue will give use BFS
        # pop item from BFS then check neighbors of node, if any have fresh fruit, add to queue
        # AND subtract freshcount by 1
        minutes = 1
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                item = queue.popleft()
                row, col = item[0], item[1]
                # check neighbors
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for pair in neighbors:
                    # neighbor is a fresh fruit
                    pair_row = pair[0]
                    pair_col = pair[1]
                    if (pair_row < 0 or pair_row >= row_count) or (pair_col < 0 or pair_col >= col_count):
                        print("here")
                        continue
                    print(pair)
                    if grid[pair[0]][pair[1]] == 1: 
                        fresh_count -= 1
                        grid[pair_row][pair_col] = 2
                        queue.append(pair)
            minutes += 1
        if fresh_count > 0:
            return -1
        return minutes - 1
