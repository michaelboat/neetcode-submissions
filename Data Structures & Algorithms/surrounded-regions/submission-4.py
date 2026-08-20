class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return board

        rows, cols = len(board), len(board[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        regions = set()
        queue = deque()

        def bfs(queue):
            reachable = set()
            while queue:
                r, c = queue.popleft()
                reachable.add((r, c))
                for dr, dc in offsets:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in reachable or board[nr][nc] == "X"):
                        continue
                    
                    queue.append((nr, nc))

            
            return reachable


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    regions.add((i, j))
                if board[i][j] == "O" and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    queue.append((i, j))

        unsafe = regions - bfs(queue)

        for r, c in unsafe:
            board[r][c] = "X"

    


        