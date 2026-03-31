class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #blank canvas for recreating the graph, using map instead of list
        adj_map = defaultdict(set)

        # check for cycle in graph
        def dfs(node, parent_node):
            if node in visited:
                # cycle detected 
                return True
            
            visited.add(node)

            for adj_node in adj_map[node]:
                if adj_node == parent_node:
                    continue
                
                if dfs(adj_node, node):
                    return True
            
            return False
        
        # adding edges one by one and checking for cycle each time
        for edge in edges:
            adj_map[edge[0]].add(edge[1])
            adj_map[edge[1]].add(edge[0])

            visited = set()
            if dfs(edge[0], -1): #first node had no parrent therefore, -1
                return [edge[0], edge[1]]
        
        return []
            
            