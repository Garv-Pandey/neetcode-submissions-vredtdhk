class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        diag_pos_set = set()
        diag_neg_set = set()

        result = 0
        def dfs(i):
            nonlocal result
            if i == n:
                result += 1
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
                dfs(i+1)

                col_set.remove(j)
                diag_pos_set.remove(diag_pos)
                diag_neg_set.remove(diag_neg)
        
        dfs(0)
        return result
