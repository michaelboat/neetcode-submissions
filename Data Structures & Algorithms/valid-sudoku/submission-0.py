class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                idx = (r//3) * 3 + c // 3
                if board[r][c] in boxes[idx]:
                    return False
                boxes[idx].add(board[r][c])

        
        return True
        
        