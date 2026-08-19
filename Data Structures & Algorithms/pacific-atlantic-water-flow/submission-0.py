class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # water can flow in four directions from a cell to a 
        # neighbouring cell with height equal to or lower. water can also
        # flow into the ocean from cells adjacent to the ocean.

        # question: find all cells where water can flow from the cell to 
        # both the pacific and atlantic oceans.

        rows, cols = len(heights), len(heights[0])
        offsets = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific_queue.append((i, j))
                if i == rows-1 or j == cols-1:
                    atlantic_queue.append((i, j))

        p_reachable = set()
        #hashmap = {}
        res = []
        while pacific_queue:
            r, c = pacific_queue.popleft()
            p_reachable.add((r, c))
            for dr, dc in offsets:
                nr, nc = r+dr, c+dc
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in p_reachable or heights[nr][nc] < heights[r][c]):
                    continue
                pacific_queue.append((nr, nc))
                #visited.add((nr, nc))
                #hashmap[(r, c)] = (nr, nc) 

        a_reachable = set()
        #hashmap = {}
        #res = []
        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            a_reachable.add((r, c))
            for dr, dc in offsets:
                nr, nc = r+dr, c+dc
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in a_reachable or heights[nr][nc] < heights[r][c]):
                    continue
                atlantic_queue.append((nr, nc))


        return list(p_reachable.intersection(a_reachable))

        


        