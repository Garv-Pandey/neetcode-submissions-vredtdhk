class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(set)

        for edge in edges:
            adj_map[edge[0]].add(edge[1])
            adj_map[edge[1]].add(edge[0])
        
        visited = set()
        nodes_seen = set()

        def dfs(node, prev_node):
            print(node)
            if node in visited:
                return False
            
            visited.add(node)
            nodes_seen.add(node)

            print(adj_map[node])
            for adj_node in adj_map[node]:
                if adj_node == prev_node:
                    continue
                if not dfs(adj_node, node):
                    return False
            
            visited.remove(node)
            return True

        # print(dfs(0))
        # print(nodes_seen)

        return dfs(0, -1) and (len(nodes_seen) == n)