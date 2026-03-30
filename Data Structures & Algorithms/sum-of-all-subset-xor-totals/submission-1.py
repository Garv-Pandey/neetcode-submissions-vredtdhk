class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) == 0:
            return 0
        
        def dfs(index, total):
            if index == len(nums):
                return total

            return dfs(index+1, total ^ nums[index]) + dfs(index+1, total)
        
        return dfs(0, 0)
