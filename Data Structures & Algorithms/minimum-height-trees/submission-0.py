class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # counting distance from the far end to start
        def dfs(node, parent):
            farthest_node = node
            max_distance = 0
            for nei in adj[node]:
                if nei != parent:
                    nei_node, nei_distance = dfs(nei, node)
                    if nei_distance + 1 > max_distance: # +1 is the distance from neighbor to the current node (backwards dirction)
                        max_distance = nei_distance + 1
                        farthest_node = nei_node
            return farthest_node, max_distance

        node_a, _ = dfs(0, -1)
        node_b, diameter = dfs(node_a, -1)

        centroids = []

        def find_centroids(node, parent):
            if node == node_b:
                centroids.append(node)
                return True
            for nei in adj[node]:
                if nei != parent:
                    if find_centroids(nei, node): # will only be true if the furthes node on the path is node_b
                        centroids.append(node)
                        return True
            return False

        find_centroids(node_a, -1)
        print(centroids)
        L = len(centroids)
        if diameter % 2 == 0:
            return [centroids[L // 2]]
        else:
            return [centroids[L // 2 - 1], centroids[L // 2]]