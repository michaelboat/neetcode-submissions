class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # a graph is a valid if it has no cycles
        # and it is fully connected(i.e all nodes can be visited)
        # from one traversal search

        adj_ls = [[] for i in range(n)]

        for edge in edges:
            u, v = edge
            adj_ls[u].append(v)
            adj_ls[v].append(u)

        stack, visited = [], set()
        stack.append(0)
        visited.add(0)
        ct = 0

        while stack:
            ct += 1
            node = stack.pop()
            for child in adj_ls[node]:
                if child in visited:
                    return False
                stack.append(child)
                visited.add(child)
                adj_ls[child].remove(node)

        return ct==n

            
