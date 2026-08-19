class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        rows, cols = len(grid), len(grid[0])

        # helper dfs function
        def dfs(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or\
            grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # run dfs
                    res = max(dfs(i, j), res)
                    #print(res)

        return res

    