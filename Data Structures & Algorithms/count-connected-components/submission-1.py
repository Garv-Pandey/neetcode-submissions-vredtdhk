class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_map = defaultdict(set)
        for edge in edges:
            adj_map[edge[0]].add(edge[1])
            adj_map[edge[1]].add(edge[0])
        
        print(adj_map)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for adj_node in adj_map[node]:
                dfs(adj_node)
        
        result = 0
        for edge_no in range(n):
            if edge_no not in visited:
                result +=1
                dfs(edge_no)
        
        return result


