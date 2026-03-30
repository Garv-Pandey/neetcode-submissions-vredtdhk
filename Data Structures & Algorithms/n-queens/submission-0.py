class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        diag_pos_set = set()
        diag_neg_set = set()

        result = []
        subset = []
        def dfs(i):
            if i == n:
                result.append(subset.copy())
                return 
            
            for j in range(n):
                diag_pos = i + j
                diag_neg = j - i

                if (j in col_set
                or diag_pos in diag_pos_set
                or diag_neg in diag_neg_set):
                    continue
                
                col_set.add(j)
                diag_pos_set.add(diag_pos)
                diag_neg_set.add(diag_neg)
                position = ""
                for _ in range(n):
                    if _ == j:
                        position += "Q"
                    else:
                        position += "."
                
                subset.append(position)
                dfs(i+1)

                subset.pop()
                col_set.remove(j)
                diag_pos_set.remove(diag_pos)
                diag_neg_set.remove(diag_neg)

        dfs(0)
        return result

