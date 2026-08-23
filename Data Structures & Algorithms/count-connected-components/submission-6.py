class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_ls = [[] for _ in range(n)]
        visited = [0] * n

        for edge in edges:
            u, v = edge
            adj_ls[u].append(v)
            adj_ls[v].append(u)

        res = 0

        for i in range(n):
            if visited[i] == 1:
                continue
            res += 1
            stack = [i]
            visited[i] = 1
            while stack:
                node = stack.pop()
                for child in adj_ls[node]:
                    if visited[child] == 0:
                        stack.append(child)
                        visited[child] = 1
                        #adj_ls[child].remove(node)
        return res

                

        