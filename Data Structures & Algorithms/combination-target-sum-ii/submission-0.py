class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        subset = []
        def dfs(index):
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            if index>=len(candidates) or sum(subset)>target:
                return
            
            subset.append(candidates[index])
            dfs(index+1)

            subset.pop()
            while index+1<len(candidates) and candidates[index+1] == candidates[index]:
                index+=1 
            dfs(index+1)
        
        dfs(0)
        return result