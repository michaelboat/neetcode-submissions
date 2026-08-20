class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        adj_ls = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            end, start = edge
            adj_ls[start].append(end)

        def dfs(node:int, inStack:list, visit:list) -> bool:

            if inStack[node]:
                return True

            if visit[node]:
                return False

            visit[node] = True
            inStack[node] = True

            for neighbor in adj_ls[node]:
                if dfs(neighbor, inStack, visit):
                    return True

            
            inStack[node] = False
            return False

        visit = [False]*numCourses
        inStack = [False]*numCourses
        for i in range(len(adj_ls)):
            if dfs(i, inStack, visit):
                return False

        return True
