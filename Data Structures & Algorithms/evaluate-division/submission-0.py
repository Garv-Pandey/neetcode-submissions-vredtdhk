class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_map = defaultdict(list)

        for i, equation in enumerate(equations):
            a, b = equation 
            value = values[i]

            adj_map[a].append((b, value))
            adj_map[b].append((a, 1/value))
        

        print(adj_map)
        def dfs(numer, denom, visited):
            print(numer, denom)
            if numer not in adj_map or denom not in adj_map:
                return -1
            
            if numer == denom:
                print("reached")
                return 1
                
            visited.add(numer)

            for neighbor, weight in adj_map[numer]:
                if neighbor in visited:
                    print(f"visited {neighbor, denom}")
                    continue
                
                result = dfs(neighbor, denom, visited)

                if result != -1:
                    return weight * result
            
            return -1

        
        result = []
        for query in queries:
            result.append(dfs(query[0], query[1], set()))
        
        return result
            
