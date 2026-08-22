class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegrees = [0]*numCourses
        adj_ls = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            v, u = edge
            adj_ls[u].append(v)
            indegrees[v] += 1

        res = []
        queue = deque()
        for i, val in enumerate(indegrees):
            if val == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)
            
            for child in adj_ls[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        return res if len(res)==numCourses else []
        