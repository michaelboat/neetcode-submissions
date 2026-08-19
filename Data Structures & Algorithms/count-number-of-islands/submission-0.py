from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        rows = len(grid)
        cols = len(grid[0])
        offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # bfs helper function
        def bfs(row:int, col:int):

            queue = deque()
            grid[row][col] = "0"
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in offsets:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    # run bfs
                    bfs(i, j)
                    res += 1

        return res


        




        