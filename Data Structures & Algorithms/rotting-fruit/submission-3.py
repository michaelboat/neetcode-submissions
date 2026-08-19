class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_ct = 0
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_ct += 1

        if fresh_ct == 0: return 0

        res = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in offsets:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] != 1):
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh_ct -= 1

            res += 1
            

        return res if fresh_ct == 0 else -1