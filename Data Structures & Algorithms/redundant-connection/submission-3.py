class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(src, visited, adj_ls, parent):
            nonlocal cycle_start
            visited[src] = True

            for child in adj_ls[src]:
                if not visited[child]:
                    parent[child] = src
                    dfs(child, visited, adj_ls, parent)
                elif child != parent[src] and cycle_start == -1:
                    cycle_start = child
                    parent[child] = src

        n = len(edges)
        visited = [False]*n
        parent = [-1]*n

        adj_ls = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adj_ls[u-1].append(v-1)
            adj_ls[v-1].append(u-1)

        cycle_start = -1
        dfs(0, visited, adj_ls, parent)
        cycle_nodes = {}
        node = cycle_start

        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == cycle_start:
                break


        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            if u-1 in cycle_nodes and v-1 in cycle_nodes:
                return edges[i]

        return []
                
        