class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None:
            return []
        
        result = []
        subset = []
        def dfs(index):
            if sum(subset)==target:
                result.append(subset.copy())
                return 
            
            if index>=len(nums) or sum(subset)>target:
                return
            
            subset.append(nums[index])
            dfs(index)
            subset.pop()
            dfs(index+1)
        
        dfs(0)
        return result