class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        INF = (2**31)-1

        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))


        dist = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols
                    or grid[nr][nc] != INF):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))


                
        